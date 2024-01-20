
from .act import NaiveAct, RandomAct
# from .selfask import SelfAskAct
# from .cot import ChainOfThought
# from .self_consistency import SelfConsistency
# from .spp import SPP
# from .reflexion import Reflexion
# from .exe import EXE

REGISTRY = {}
REGISTRY['random_actor'] = RandomAct
REGISTRY['naive_actor'] = NaiveAct
# REGISTRY['selfask_actor'] = SelfAskAct
# REGISTRY['cot_actor'] = ChainOfThought
# REGISTRY['self_consistency_actor'] = SelfConsistency
# REGISTRY['spp_actor'] = SPP
# REGISTRY['reflexion_actor'] = Reflexion
# REGISTRY['exe_actor'] = EXE
