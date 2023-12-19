from .task_relevant.classic_control import cartpole
from .task_relevant.classic_control import acrobot
from .task_relevant.classic_control import mountaincar
from .task_relevant.classic_control import mountaincarContinuous
from .task_relevant.box2d import LunarLander
from .task_relevant.toy_text import blackjack
from .task_relevant.toy_text import taxi
from .task_relevant.toy_text import cliffwalking
from .task_relevant.toy_text import frozenlake
from .task_irrelevant import prompts

REGISTRY = {}
# task irrelevant prompts
REGISTRY[("naive_actor")] = prompts.ACT
REGISTRY[("cot_actor")] = prompts.COT
REGISTRY[("pal_actor")] = prompts.PAL
REGISTRY[('self_consistency_actor')] = prompts.CONSISTENCY
REGISTRY[('selfask_actor')] = prompts.SELFASK
REGISTRY[('spp_actor')] = prompts.SPP
REGISTRY[('reflexion_actor')] = prompts.REFLEXION
REGISTRY[('exe_actor')] = prompts.EXE

# CartPole-v0
REGISTRY[("CartPole-v0","naive_actor")] = cartpole.ACT
REGISTRY[("CartPole-v0","cot_actor")] = cartpole.COT
REGISTRY[("CartPole-v0","pal_actor")] = cartpole.PAL
REGISTRY[("CartPole-v0",'self_consistency_actor')] = cartpole.CONSISTENCY
REGISTRY[("CartPole-v0",'selfask_actor')] = cartpole.SELFASK
REGISTRY[("CartPole-v0",'spp_actor')] = cartpole.SPP
REGISTRY[("CartPole-v0",'reflexion_actor')] = cartpole.REFLEXION
REGISTRY[("CartPole-v0",'exe_actor')] = cartpole.EXE

# LunarLander-v2
REGISTRY[("LunarLander-v2","naive_actor")] = LunarLander.ACT
REGISTRY[("LunarLander-v2","cot_actor")] = LunarLander.COT
REGISTRY[("LunarLander-v2","pal_actor")] = LunarLander.PAL
REGISTRY[("LunarLander-v2",'self_consistency_actor')] = LunarLander.CONSISTENCY
REGISTRY[("LunarLander-v2",'selfask_actor')] = LunarLander.SELFASK
REGISTRY[("LunarLander-v2",'spp_actor')] = LunarLander.SPP
REGISTRY[("LunarLander-v2",'reflexion_actor')] = LunarLander.REFLEXION
REGISTRY[("LunarLander-v2",'exe_actor')] = LunarLander.EXE


# Acrobot-v1
REGISTRY[("Acrobot-v1","naive_actor")] = acrobot.ACT
REGISTRY[("Acrobot-v1","cot_actor")] = acrobot.COT
REGISTRY[("Acrobot-v1","pal_actor")] = acrobot.PAL
REGISTRY[("Acrobot-v1",'self_consistency_actor')] = acrobot.CONSISTENCY
REGISTRY[("Acrobot-v1",'selfask_actor')] = acrobot.SELFASK
REGISTRY[("Acrobot-v1",'spp_actor')] = acrobot.SPP
REGISTRY[("Acrobot-v1",'reflexion_actor')] = acrobot.REFLEXION
REGISTRY[("Acrobot-v1",'exe_actor')] = acrobot.EXE

# MountainCar-v0
REGISTRY[("MountainCar-v0","naive_actor")] = mountaincar.ACT
REGISTRY[("MountainCar-v0","cot_actor")] = mountaincar.COT
REGISTRY[("MountainCar-v0","pal_actor")] = mountaincar.PAL
REGISTRY[("MountainCar-v0",'self_consistency_actor')] = mountaincar.CONSISTENCY
REGISTRY[("MountainCar-v0",'selfask_actor')] = mountaincar.SELFASK
REGISTRY[("MountainCar-v0",'spp_actor')] = mountaincar.SPP
REGISTRY[("MountainCar-v0",'reflexion_actor')] = mountaincar.REFLEXION
REGISTRY[("MountainCar-v0",'exe_actor')] = mountaincar.EXE

# Blackjack-v1
REGISTRY[("Blackjack-v1","naive_actor")] = blackjack.ACT
REGISTRY[("Blackjack-v1","cot_actor")] = blackjack.COT
REGISTRY[("Blackjack-v1","pal_actor")] = blackjack.PAL
REGISTRY[("Blackjack-v1",'self_consistency_actor')] = blackjack.CONSISTENCY
REGISTRY[("Blackjack-v1",'selfask_actor')] = blackjack.SELFASK
REGISTRY[("Blackjack-v1",'spp_actor')] = blackjack.SPP
REGISTRY[("Blackjack-v1",'reflexion_actor')] = blackjack.REFLEXION
REGISTRY[("Blackjack-v1",'exe_actor')] = blackjack.EXE

# Taxi-v3
REGISTRY[("Taxi-v3","naive_actor")] = taxi.ACT
REGISTRY[("Taxi-v3","cot_actor")] = taxi.COT
REGISTRY[("Taxi-v3","pal_actor")] = taxi.PAL
REGISTRY[("Taxi-v3",'self_consistency_actor')] = taxi.CONSISTENCY
REGISTRY[("Taxi-v3",'selfask_actor')] = taxi.SELFASK
REGISTRY[("Taxi-v3",'spp_actor')] = taxi.SPP
REGISTRY[("Taxi-v3",'reflexion_actor')] = taxi.REFLEXION
REGISTRY[("Taxi-v3",'exe_actor')] = taxi.EXE
# CliffWalking-v0
REGISTRY[("CliffWalking-v0","naive_actor")] = cliffwalking.ACT
REGISTRY[("CliffWalking-v0","cot_actor")] = cliffwalking.COT
REGISTRY[("CliffWalking-v0","pal_actor")] = cliffwalking.PAL
REGISTRY[("CliffWalking-v0",'self_consistency_actor')] = cliffwalking.CONSISTENCY
REGISTRY[("CliffWalking-v0",'selfask_actor')] = cliffwalking.SELFASK
REGISTRY[("CliffWalking-v0",'spp_actor')] = cliffwalking.SPP
REGISTRY[("CliffWalking-v0",'reflexion_actor')] = cliffwalking.REFLEXION
REGISTRY[("CliffWalking-v0",'exe_actor')] = cliffwalking.EXE

# FrozenLake-v1
REGISTRY[("FrozenLake-v1","naive_actor")] = frozenlake.ACT
REGISTRY[("FrozenLake-v1","cot_actor")] = frozenlake.COT
REGISTRY[("FrozenLake-v1","pal_actor")] = frozenlake.PAL
REGISTRY[("FrozenLake-v1",'self_consistency_actor')] = frozenlake.CONSISTENCY
REGISTRY[("FrozenLake-v1",'selfask_actor')] = frozenlake.SELFASK
REGISTRY[("FrozenLake-v1",'spp_actor')] = frozenlake.SPP
REGISTRY[("FrozenLake-v1",'reflexion_actor')] = frozenlake.REFLEXION
REGISTRY[("FrozenLake-v1",'exe_actor')] = frozenlake.EXE

# MountainCarContinuous-v0
REGISTRY[("MountainCarContinuous-v0","naive_actor")] = mountaincarContinuous.ACT
REGISTRY[("MountainCarContinuous-v0","cot_actor")] = mountaincarContinuous.COT
REGISTRY[("MountainCarContinuous-v0","pal_actor")] = mountaincarContinuous.PAL
REGISTRY[("MountainCarContinuous-v0",'self_consistency_actor')] = mountaincarContinuous.CONSISTENCY
REGISTRY[("MountainCarContinuous-v0",'selfask_actor')] = mountaincarContinuous.SELFASK
REGISTRY[("MountainCarContinuous-v0",'spp_actor')] = mountaincarContinuous.SPP
REGISTRY[("MountainCarContinuous-v0",'reflexion_actor')] = mountaincarContinuous.REFLEXION
REGISTRY[("MountainCarContinuous-v0",'exe_actor')] = mountaincarContinuous.EXE
