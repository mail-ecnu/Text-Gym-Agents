import sys
import numpy as np
import torch
from torch import nn
sys.path.insert(0, sys.path[0]+"/../")
from typing import (
    Any,
    Dict,
    List,
    Optional,
    Sequence,
    Tuple,
    Type,
    Union,
    no_type_check,
)
import torch.nn as nn
from tianshou.utils.net.discrete import NoisyLinear
ModuleType = Type[nn.Module]
import random
from collections import namedtuple, deque
from itertools import count
import math
import torch
import torch.optim as optim
from transformers import AutoModel, AutoTokenizer
import torch.nn.functional as F
from tianshou.utils.net.common import ModuleType, Net, MLP


def bert_embedding(x, max_length=512, device='cuda'):
    from transformers import logging
    logging.set_verbosity_error()
    model_name = 'bert-base-uncased'
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    bert_model = AutoModel.from_pretrained(model_name)
    text = x
    if isinstance(text, np.ndarray):
        text = list(text)
    tokens = tokenizer(text, max_length=max_length, padding='max_length', truncation=True, return_tensors='pt')
    input_ids = tokens['input_ids']
    attention_mask = tokens['attention_mask']
    with torch.no_grad():
        outputs = bert_model(input_ids, attention_mask=attention_mask)
        embeddings = outputs.last_hidden_state
    return embeddings

class Net_GRU(nn.Module):

    def __init__(self, input_size, n_actions, hidden_dim, n_layers, dropout, bidirectional):
        super(Net_GRU, self).__init__()
        self.input_size = input_size
        self.hidden_dim = hidden_dim
        self.num_classes = n_actions
        self.n_layers = n_layers
        self.dropout = dropout
        self.bidirectional = bidirectional
        
        # Layers
        self.gru = nn.GRU(self.input_size, self.hidden_dim, self.n_layers, 
                          batch_first=True, dropout=self.dropout, bidirectional=self.bidirectional)
        self.final_layer = nn.Linear(self.hidden_dim*(1 + int(self.bidirectional)), self.num_classes)
        
    def forward(self, x):
        # Input shape: (batch_size, seq_length)
        batch_size, seq_length, emb_size = x.size()
        
        gru_out, hidden = self.gru(x)
        
        # Use the final state
        # hidden -> (num_direction, batch, hidden_size)
        if self.bidirectional:
            hidden = hidden.view(self.n_layers, 2, batch_size, self.hidden_dim)
            final_hidden = torch.cat((hidden[:, -1, :, :].squeeze(0), hidden[:, 0, :, :].squeeze(0)), 1)
        else:
            final_hidden = hidden.squeeze(0)
        
        # final_hidden -> (batch_size, num_classes)
        logits = self.final_layer(final_hidden)
        
        return logits
    
class MyGRU(nn.Module):
    def __init__(self, input_size, hidden_dim, n_layers, dropout, bidirectional, output_dim):
        super(MyGRU, self).__init__()
        self.input_size = input_size
        self.hidden_dim = hidden_dim
        self.n_layers = n_layers
        self.dropout = dropout
        self.bidirectional = bidirectional
        
        # Layers
        self.gru = nn.GRU(self.input_size, self.hidden_dim, self.n_layers, 
                          batch_first=True, dropout=self.dropout, bidirectional=self.bidirectional)
        self.final_layer = nn.Linear(self.hidden_dim*(1 + int(self.bidirectional)), output_dim)

    def forward(self, x):
        batch_size, seq_length, emb_size = x.size()
        
        gru_out, hidden = self.gru(x)
        
        # Use the final state
        # hidden -> (num_direction, batch, hidden_size)
        if self.bidirectional:
            hidden = hidden.view(self.n_layers, 2, batch_size, self.hidden_dim)
            final_hidden = torch.cat((hidden[:, -1, :, :].squeeze(0), hidden[:, 0, :, :].squeeze(0)), 1)
        else:
            final_hidden = hidden.squeeze(0)
        
        # final_hidden -> (batch_size, num_classes)
        logits = self.final_layer(final_hidden)
        
        return logits

class MyCNN(nn.Module):
    def __init__(self, 
            input_dim: int, 
            output_dim: int = 0,
            hidden_sizes: Sequence[int] = (),
            norm_layer: Optional[Union[ModuleType, Sequence[ModuleType]]] = None,
            activation: ModuleType = nn.ReLU,
            device: Optional[Union[str, int, torch.device]] = None,
            linear_layer: Type[nn.Linear] = nn.Linear,
            flatten_input: bool = True,) -> None:
        super().__init__()
        self.model = []
        input_dim_temp = input_dim
        for h in hidden_sizes:
            self.model.append(nn.Conv1d(in_channels=input_dim_temp, out_channels=h, kernel_size=3, padding=1))
            self.model.append(activation())
            self.model.append(nn.MaxPool1d(kernel_size=2))
            input_dim_temp = h
        self.model = nn.Sequential(*self.model)
        self.fc = nn.Linear(in_features=input_dim_temp, out_features=output_dim)
        
    def forward(self, x):
        x = self.model(x.transpose(1, 2))
        x.transpose_(1, 2)
        x = self.fc(x)
        return x

class Net_GRU_Bert_tianshou(Net):
    def __init__(
        self,
        state_shape: Union[int, Sequence[int]],
        action_shape: Union[int, Sequence[int]] = 0,
        hidden_sizes: Sequence[int] = (),
        norm_layer: Optional[ModuleType] = None,
        activation: Optional[ModuleType] = nn.ReLU,
        device: Union[str, int, torch.device] = "cpu",
        softmax: bool = False,
        concat: bool = False,
        num_atoms: int = 1,
        dueling_param: Optional[Tuple[Dict[str, Any], Dict[str, Any]]] = None,
        linear_layer: Type[nn.Linear] = nn.Linear,
        hidden_dim: int = 128,
        bidirectional: bool = True,
        dropout: float = 0.,
        n_layers: int = 1,
        max_length: int = 512,
        trans_model_name: str = 'bert-base-uncased',
    ) -> None:
        nn.Module.__init__(self)
        self.device = device
        self.softmax = softmax
        self.num_atoms = num_atoms
        self.hidden_dim = hidden_dim
        self.bidirectional = bidirectional
        self.dropout = dropout
        self.n_layers = n_layers
        self.trans_model_name = trans_model_name
        self.max_length = max_length

        input_dim = int(np.prod(state_shape))
        action_dim = int(np.prod(action_shape)) * num_atoms
        if concat:
            input_dim += action_dim
        self.use_dueling = dueling_param is not None
        output_dim = action_dim if not self.use_dueling and not concat else 0
        self.output_dim = output_dim or hidden_dim
        self.model = MyGRU(768, self.hidden_dim, self.n_layers, 
                          self.dropout, self.bidirectional, self.output_dim)
        if self.use_dueling:  # dueling DQN
            q_kwargs, v_kwargs = dueling_param  # type: ignore
            q_output_dim, v_output_dim = 0, 0
            if not concat:
                q_output_dim, v_output_dim = action_dim, num_atoms
            q_kwargs: Dict[str, Any] = {
                **q_kwargs, "input_dim": self.output_dim,
                "output_dim": q_output_dim,
                "device": self.device
            }
            v_kwargs: Dict[str, Any] = {
                **v_kwargs, "input_dim": self.output_dim,
                "output_dim": v_output_dim,
                "device": self.device
            }
            self.Q, self.V = MLP(**q_kwargs), MLP(**v_kwargs)
            self.output_dim = self.Q.output_dim
        self.bert_model = AutoModel.from_pretrained(self.trans_model_name).to(self.device)
        self.tokenizer = AutoTokenizer.from_pretrained(trans_model_name)
        from transformers import logging
        logging.set_verbosity_error()

    def bert_embedding(self, x, max_length=512):
        text = x
        if isinstance(text, np.ndarray):
            text = list(text)
        tokens = self.tokenizer(text, max_length=max_length, padding='max_length', truncation=True, return_tensors='pt')
        input_ids = tokens['input_ids'].to(self.device)
        attention_mask = tokens['attention_mask'].to(self.device)
        with torch.no_grad():
            outputs = self.bert_model(input_ids, attention_mask=attention_mask)
            embeddings = outputs.last_hidden_state
        return embeddings

    def forward(
        self,
        obs: Union[np.ndarray, torch.Tensor],
        state: Any = None,
        info: Dict[str, Any] = {},
    ) -> Tuple[torch.Tensor, Any]:
        """Mapping: obs -> flatten (inside MLP)-> logits."""
        embedding = self.bert_embedding(obs, max_length=self.max_length)
        logits = self.model(embedding)
        bsz = logits.shape[0]
        if self.use_dueling:  # Dueling DQN
            q, v = self.Q(logits), self.V(logits)
            if self.num_atoms > 1:
                q = q.view(bsz, -1, self.num_atoms)
                v = v.view(bsz, -1, self.num_atoms)
            logits = q - q.mean(dim=1, keepdim=True) + v
        elif self.num_atoms > 1:
            logits = logits.view(bsz, -1, self.num_atoms)
        if self.softmax:
            logits = torch.softmax(logits, dim=-1)
        return logits, state
    
class Net_Bert_CLS_tianshou(Net):
    def __init__(
        self,
        state_shape: Union[int, Sequence[int]],
        action_shape: Union[int, Sequence[int]] = 0,
        hidden_sizes: Sequence[int] = (),
        norm_layer: Optional[ModuleType] = None,
        activation: Optional[ModuleType] = nn.ReLU,
        device: Union[str, int, torch.device] = "cpu",
        softmax: bool = False,
        concat: bool = False,
        num_atoms: int = 1,
        dueling_param: Optional[Tuple[Dict[str, Any], Dict[str, Any]]] = None,
        linear_layer: Type[nn.Linear] = nn.Linear,
        hidden_dim: int = 128,
        bidirectional: bool = True,
        dropout: float = 0.,
        n_layers: int = 1,
        max_length: int = 512,
        trans_model_name: str = 'bert-base-uncased',
    ) -> None:
        nn.Module.__init__(self)
        self.device = device
        self.softmax = softmax
        self.num_atoms = num_atoms
        self.hidden_dim = hidden_dim
        self.bidirectional = bidirectional
        self.dropout = dropout
        self.n_layers = n_layers
        self.trans_model_name = trans_model_name
        self.max_length = max_length

        input_dim = int(np.prod(state_shape))
        action_dim = int(np.prod(action_shape)) * num_atoms
        if concat:
            input_dim += action_dim
        self.use_dueling = dueling_param is not None
        output_dim = action_dim if not self.use_dueling and not concat else 0
        self.output_dim = output_dim or hidden_dim
        self.model = MLP(768, output_dim, hidden_sizes, norm_layer, activation, device, linear_layer)
        if self.use_dueling:  # dueling DQN
            q_kwargs, v_kwargs = dueling_param  # type: ignore
            q_output_dim, v_output_dim = 0, 0
            if not concat:
                q_output_dim, v_output_dim = action_dim, num_atoms
            q_kwargs: Dict[str, Any] = {
                **q_kwargs, "input_dim": self.output_dim,
                "output_dim": q_output_dim,
                "device": self.device
            }
            v_kwargs: Dict[str, Any] = {
                **v_kwargs, "input_dim": self.output_dim,
                "output_dim": v_output_dim,
                "device": self.device
            }
            self.Q, self.V = MLP(**q_kwargs), MLP(**v_kwargs)
            self.output_dim = self.Q.output_dim
        self.bert_model = AutoModel.from_pretrained(self.trans_model_name).to(self.device)
        self.tokenizer = AutoTokenizer.from_pretrained(trans_model_name)
        from transformers import logging
        logging.set_verbosity_error()

    def bert_CLS_embedding(self, x, max_length=512):
        text = x
        if isinstance(text, np.ndarray):
            text = list(text)
        tokens = self.tokenizer(text, max_length=max_length, padding='max_length', truncation=True, return_tensors='pt')
        input_ids = tokens['input_ids'].to(self.device)
        attention_mask = tokens['attention_mask'].to(self.device)
        with torch.no_grad():
            outputs = self.bert_model(input_ids, attention_mask=attention_mask)
            embeddings = outputs[0][:, 0, :]
        return embeddings

    def forward(
        self,
        obs: Union[np.ndarray, torch.Tensor],
        state: Any = None,
        info: Dict[str, Any] = {},
    ) -> Tuple[torch.Tensor, Any]:
        """Mapping: obs -> flatten (inside MLP)-> logits."""
        embedding = self.bert_CLS_embedding(obs, max_length=self.max_length)
        logits = self.model(embedding)
        bsz = logits.shape[0]
        if self.use_dueling:  # Dueling DQN
            q, v = self.Q(logits), self.V(logits)
            if self.num_atoms > 1:
                q = q.view(bsz, -1, self.num_atoms)
                v = v.view(bsz, -1, self.num_atoms)
            logits = q - q.mean(dim=1, keepdim=True) + v
        elif self.num_atoms > 1:
            logits = logits.view(bsz, -1, self.num_atoms)
        if self.softmax:
            logits = torch.softmax(logits, dim=-1)
        return logits, state
    

class Net_Bert_CNN_tianshou(Net_GRU_Bert_tianshou):
    def __init__(
        self,
        state_shape: Union[int, Sequence[int]],
        action_shape: Union[int, Sequence[int]] = 0,
        hidden_sizes: Sequence[int] = (),
        norm_layer: Optional[ModuleType] = None,
        activation: Optional[ModuleType] = nn.ReLU,
        device: Union[str, int, torch.device] = "cpu",
        softmax: bool = False,
        concat: bool = False,
        num_atoms: int = 1,
        dueling_param: Optional[Tuple[Dict[str, Any], Dict[str, Any]]] = None,
        linear_layer: Type[nn.Linear] = nn.Linear,
        hidden_dim: int = 128,
        bidirectional: bool = True,
        dropout: float = 0.,
        n_layers: int = 1,
        max_length: int = 512,
        trans_model_name: str = 'bert-base-uncased',
    ) -> None:
        nn.Module.__init__(self)
        self.device = device
        self.softmax = softmax
        self.num_atoms = num_atoms
        self.hidden_dim = hidden_dim
        self.bidirectional = bidirectional
        self.dropout = dropout
        self.n_layers = n_layers
        self.trans_model_name = trans_model_name
        self.max_length = max_length

        input_dim = int(np.prod(state_shape))
        action_dim = int(np.prod(action_shape)) * num_atoms
        if concat:
            input_dim += action_dim
        self.use_dueling = dueling_param is not None
        output_dim = action_dim if not self.use_dueling and not concat else 0
        self.output_dim = output_dim or hidden_dim
        self.model = MyCNN(768, output_dim, hidden_sizes, norm_layer, activation, device, linear_layer, flatten_input=False)
        if self.use_dueling:  # dueling DQN
            q_kwargs, v_kwargs = dueling_param  # type: ignore
            q_output_dim, v_output_dim = 0, 0
            if not concat:
                q_output_dim, v_output_dim = action_dim, num_atoms
            q_kwargs: Dict[str, Any] = {
                **q_kwargs, "input_dim": self.output_dim,
                "output_dim": q_output_dim,
                "device": self.device
            }
            v_kwargs: Dict[str, Any] = {
                **v_kwargs, "input_dim": self.output_dim,
                "output_dim": v_output_dim,
                "device": self.device
            }
            self.Q, self.V = MLP(**q_kwargs), MLP(**v_kwargs)
            self.output_dim = self.Q.output_dim
        self.bert_model = AutoModel.from_pretrained(self.trans_model_name).to(self.device)
        self.tokenizer = AutoTokenizer.from_pretrained(trans_model_name)
        from transformers import logging
        logging.set_verbosity_error()

class DQN_GRU(nn.Module):
    """Reference: Human-level control through deep reinforcement learning.
    """

    def __init__(
        self,
        state_shape: Union[int, Sequence[int]],
        action_shape: Sequence[int],
        device: Union[str, int, torch.device] = "cpu",
        features_only: bool = False,
        output_dim: Optional[int] = None,
        hidden_dim: int = 128,
        n_layers: int = 1,
        dropout: float = 0.,
        bidirectional: bool = True,
        trans_model_name: str = 'bert-base-uncased',
        max_length: int = 512,
    ) -> None:
        super().__init__()
        self.device = device
        self.max_length = max_length
        action_dim = int(np.prod(action_shape))
        self.net = MyGRU(768, hidden_dim, n_layers, dropout, bidirectional, 
                hidden_dim)
        if not features_only:
            self.net = MyGRU(768, hidden_dim, n_layers, dropout, bidirectional, 
                action_dim)
            self.output_dim = action_dim
        elif output_dim is not None:
            self.net = MyGRU(768, hidden_dim, n_layers, dropout, bidirectional, 
                output_dim)
            self.output_dim = output_dim
        else:
            self.net = MyGRU(768, hidden_dim, n_layers, dropout, bidirectional,
                hidden_dim)
            self.output_dim = hidden_dim
        self.trans_model_name = trans_model_name
        self.bert_model = AutoModel.from_pretrained(self.trans_model_name).to(self.device)
        self.tokenizer = AutoTokenizer.from_pretrained(trans_model_name)
        from transformers import logging
        logging.set_verbosity_error()

    def bert_embedding(self, x, max_length=512):
        text = x
        if isinstance(text, np.ndarray):
            text = list(text)
        tokens = self.tokenizer(text, max_length=max_length, padding='max_length', truncation=True, return_tensors='pt')
        input_ids = tokens['input_ids'].to(self.device)
        attention_mask = tokens['attention_mask'].to(self.device)
        with torch.no_grad():
            outputs = self.bert_model(input_ids, attention_mask=attention_mask)
            embeddings = outputs.last_hidden_state
        return embeddings

    def forward(
        self,
        obs: Union[np.ndarray, torch.Tensor],
        state: Optional[Any] = None,
        info: Dict[str, Any] = {},
    ) -> Tuple[torch.Tensor, Any]:
        r"""Mapping: s -> Q(s, \*)."""
        embedding = self.bert_embedding(obs, max_length=self.max_length)
        return self.net(embedding), state
    
class Rainbow_GRU(DQN_GRU):
    """Reference: Rainbow: Combining Improvements in Deep Reinforcement Learning.
    """

    def __init__(
        self,
        state_shape: Union[int, Sequence[int]],
        action_shape: Sequence[int],
        num_atoms: int = 51,
        noisy_std: float = 0.5,
        device: Union[str, int, torch.device] = "cpu",
        is_dueling: bool = True,
        is_noisy: bool = True,
        output_dim: Optional[int] = None,
        hidden_dim: int = 128,
        n_layers: int = 1,
        dropout: float = 0.,
        bidirectional: bool = True,
        trans_model_name: str = 'bert-base-uncased',
        max_length: int = 512,
    ) -> None:
        super().__init__(state_shape, action_shape, device, features_only=True,
                         output_dim=output_dim, hidden_dim=hidden_dim, n_layers=n_layers, 
                         dropout=dropout, bidirectional=bidirectional, trans_model_name=trans_model_name) 
        self.action_num = np.prod(action_shape)
        self.num_atoms = num_atoms

        def linear(x, y):
            if is_noisy:
                return NoisyLinear(x, y, noisy_std)
            else:
                return nn.Linear(x, y)

        self.Q = nn.Sequential(
            linear(self.output_dim, 512), nn.ReLU(inplace=True),
            linear(512, self.action_num * self.num_atoms)
        )
        self._is_dueling = is_dueling
        if self._is_dueling:
            self.V = nn.Sequential(
                linear(self.output_dim, 512), nn.ReLU(inplace=True),
                linear(512, self.num_atoms)
            )
        self.output_dim = self.action_num * self.num_atoms

    def forward(
        self,
        obs: Union[np.ndarray, torch.Tensor],
        state: Optional[Any] = None,
        info: Dict[str, Any] = {},
    ) -> Tuple[torch.Tensor, Any]:
        r"""Mapping: x -> Z(x, \*)."""
        obs, state = super().forward(obs)
        q = self.Q(obs)
        q = q.view(-1, self.action_num, self.num_atoms)
        if self._is_dueling:
            v = self.V(obs)
            v = v.view(-1, 1, self.num_atoms)
            logits = q - q.mean(dim=1, keepdim=True) + v
        else:
            logits = q
        probs = logits.softmax(dim=2)
        return probs, state
    
class Net_GRU_nn_emb_tianshou(Net):
    
    def __init__(
        self,
        action_shape: Union[int, Sequence[int]] = 0,
        hidden_sizes: Sequence[int] = (),
        norm_layer: Optional[ModuleType] = None,
        activation: Optional[ModuleType] = nn.ReLU,
        device: Union[str, int, torch.device] = "cpu",
        softmax: bool = False,
        concat: bool = False,
        num_atoms: int = 1,
        dueling_param: Optional[Tuple[Dict[str, Any], Dict[str, Any]]] = None,
        linear_layer: Type[nn.Linear] = nn.Linear,
        hidden_dim: int = 128,
        bidirectional: bool = True,
        dropout: float = 0.,
        n_layers: int = 1,
        max_length: int = 512,
        trans_model_name: str = 'bert-base-uncased',
        word_emb_dim: int = 128,
    ) -> None:
        nn.Module.__init__(self)
        self.device = device
        self.softmax = softmax
        self.num_atoms = num_atoms
        self.hidden_dim = hidden_dim
        self.bidirectional = bidirectional
        self.dropout = dropout
        self.n_layers = n_layers
        self.trans_model_name = trans_model_name
        self.max_length = max_length

        action_dim = int(np.prod(action_shape)) * num_atoms
        self.use_dueling = dueling_param is not None
        output_dim = action_dim if not self.use_dueling and not concat else 0
        self.output_dim = output_dim or hidden_dim

        self.tokenizer = AutoTokenizer.from_pretrained(trans_model_name)
        from transformers import logging
        logging.set_verbosity_error()
        self.vocab_size = self.tokenizer.vocab_size
        self.embedding = nn.Embedding(self.vocab_size, word_emb_dim)
        self.model = MyGRU(word_emb_dim, self.hidden_dim, self.n_layers, 
                          self.dropout, self.bidirectional, self.output_dim)
        if self.use_dueling:  # dueling DQN
            q_kwargs, v_kwargs = dueling_param  # type: ignore
            q_output_dim, v_output_dim = 0, 0
            if not concat:
                q_output_dim, v_output_dim = action_dim, num_atoms
            q_kwargs: Dict[str, Any] = {
                **q_kwargs, "input_dim": self.output_dim,
                "output_dim": q_output_dim,
                "device": self.device
            }
            v_kwargs: Dict[str, Any] = {
                **v_kwargs, "input_dim": self.output_dim,
                "output_dim": v_output_dim,
                "device": self.device
            }
            self.Q, self.V = MLP(**q_kwargs), MLP(**v_kwargs)
            self.output_dim = self.Q.output_dim        


    def forward(
        self,
        obs: Union[np.ndarray, torch.Tensor],
        state: Any = None,
        info: Dict[str, Any] = {},
    ) -> Tuple[torch.Tensor, Any]:
        """Mapping: obs -> flatten (inside MLP)-> logits."""
        if isinstance(obs, np.ndarray):
            text = list(obs)
        else:
            text = obs
        tokens = self.tokenizer(text, max_length=self.max_length, padding='max_length', truncation=True, return_tensors='pt')
        input_ids = tokens['input_ids'].to(self.device)
        attention_mask = tokens['attention_mask'].to(self.device)
        embedding = self.embedding(input_ids)
        mask = attention_mask.unsqueeze(-1).expand(embedding.size()).float()
        embedding = embedding * mask
        logits = self.model(embedding)
        bsz = logits.shape[0]
        if self.use_dueling:  # Dueling DQN
            q, v = self.Q(logits), self.V(logits)
            if self.num_atoms > 1:
                q = q.view(bsz, -1, self.num_atoms)
                v = v.view(bsz, -1, self.num_atoms)
            logits = q - q.mean(dim=1, keepdim=True) + v
        elif self.num_atoms > 1:
            logits = logits.view(bsz, -1, self.num_atoms)
        if self.softmax:
            logits = torch.softmax(logits, dim=-1)
        return logits, state
        
        