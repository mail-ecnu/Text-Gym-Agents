
from .act import NaiveAct, RandomAct
from .selfask import SelfAskAct
from .pal import PAL
from .cot import ChainOfThought
from .self_consistency import SelfConsistency
from .spp import SPP
from .reflexion import Reflexion
from .jarvis import Jarvis
from .jarvis_without_insights import JarvisWithoutInsight
from .jarvis_without_suggestions import JarvisWithoutSuggestions
from .jarvis_without_shortmem import JarvisWithoutShortMem

REGISTRY = {}
REGISTRY['random_actor'] = RandomAct
REGISTRY['naive_actor'] = NaiveAct
REGISTRY['selfask_actor'] = SelfAskAct
REGISTRY['pal_actor'] = PAL
REGISTRY['cot_actor'] = ChainOfThought
REGISTRY['self_consistency_actor'] = SelfConsistency
REGISTRY['spp_actor'] = SPP
REGISTRY['reflexion_actor'] = Reflexion
REGISTRY['jarvis_actor'] = Jarvis
REGISTRY['jarvis_actor_woi'] = JarvisWithoutInsight
REGISTRY['jarvis_actor_wosug'] = JarvisWithoutSuggestions
REGISTRY['jarvis_actor_wosh'] = JarvisWithoutShortMem
