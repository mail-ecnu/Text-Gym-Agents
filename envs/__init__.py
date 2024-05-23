from .base_env import BaseEnv, SettableStateEnv

from .classic_control import cartpole_translator, cartpole_policies
from .classic_control import acrobot_translator, acrobot_policies
from .classic_control import mountaincar_translator, mountaincar_policies
from .classic_control import mountaincarContinuous_translator,mountaincarContinuous_policies

from .box2d import LunarLander_translator, LunarLander_policies

from .toy_text import blackjack_translator, blackjack_policies
from .toy_text import taxi_translator, taxi_policies
from .toy_text import cliffwalking_translator, cliffwalking_policies
from .toy_text import frozenlake_translator, frozenlake_policies

from .atari import register_environments
from .atari import Boxing_policies, Boxing_translator, Pong_policies, Pong_translator
from .atari import mspacman_policies, mspacman_translator
from .atari import montezumarevenge_policies, montezumarevenge_translator
from .atari import Asteroids_translator, BattleZone_translator, Berzerk_translator, Bowling_translator, Breakout_translator, Skiing_translator
register_environments()


REGISTRY = {}
REGISTRY["sampling_wrapper"] = SettableStateEnv
REGISTRY["base_env"] = BaseEnv
REGISTRY["cart_init_translator"] = cartpole_translator.GameDescriber
REGISTRY["cart_basic_translator"] = cartpole_translator.TransitionTranslator
REGISTRY["acrobot_init_translator"] = acrobot_translator.GameDescriber
REGISTRY["acrobot_basic_translator"] = acrobot_translator.TransitionTranslator
REGISTRY["mountaincar_init_translator"] = mountaincar_translator.GameDescriber
REGISTRY["mountaincar_basic_translator"] = mountaincar_translator.TransitionTranslator

REGISTRY["cart_policies"] = [cartpole_policies.dedicated_1_policy, cartpole_policies.dedicated_2_policy, cartpole_policies.pseudo_random_policy, cartpole_policies.real_random_policy]
REGISTRY["acrobot_policies"] = [acrobot_policies.dedicated_1_policy, acrobot_policies.dedicated_2_policy, acrobot_policies.dedicated_3_policy, acrobot_policies.pseudo_random_policy, acrobot_policies.real_random_policy]
REGISTRY["mountaincar_policies"] = [mountaincar_policies.dedicated_1_policy, mountaincar_policies.dedicated_2_policy, mountaincar_policies.dedicated_3_policy, mountaincar_policies.pseudo_random_policy, mountaincar_policies.real_random_policy]

REGISTRY["lunarLander_init_translator"] = LunarLander_translator.GameDescriber
REGISTRY["lunarLander_basic_translator"] = LunarLander_translator.TransitionTranslator
REGISTRY["lunarLander_policies"] = [LunarLander_policies.dedicated_1_policy, LunarLander_policies.dedicated_2_policy, LunarLander_policies.dedicated_3_policy,LunarLander_policies.dedicated_4_policy, LunarLander_policies.pseudo_random_policy, LunarLander_policies.real_random_policy]

REGISTRY["blackjack_init_translator"] = blackjack_translator.GameDescriber
REGISTRY["blackjack_basic_translator"] = blackjack_translator.TransitionTranslator
REGISTRY["blackjack_policies"] = [blackjack_policies.dedicated_1_policy, blackjack_policies.dedicated_2_policy, blackjack_policies.pseudo_random_policy, blackjack_policies.real_random_policy]

REGISTRY["taxi_init_translator"] = taxi_translator.GameDescriber
REGISTRY["taxi_basic_translator"] = taxi_translator.TransitionTranslator
REGISTRY["taxi_policies"] = [taxi_policies.dedicated_1_policy, taxi_policies.dedicated_2_policy, taxi_policies.dedicated_3_policy, taxi_policies.dedicated_4_policy, taxi_policies.dedicated_5_policy, taxi_policies.dedicated_6_policy, taxi_policies.pseudo_random_policy, taxi_policies.real_random_policy]

REGISTRY["cliffwalking_init_translator"] = cliffwalking_translator.GameDescriber
REGISTRY["cliffwalking_basic_translator"] = cliffwalking_translator.TransitionTranslator
REGISTRY["cliffwalking_policies"] = [cliffwalking_policies.dedicated_1_policy, cliffwalking_policies.dedicated_2_policy, cliffwalking_policies.dedicated_3_policy, cliffwalking_policies.dedicated_4_policy, cliffwalking_policies.pseudo_random_policy, cliffwalking_policies.real_random_policy]

REGISTRY["frozenlake_init_translator"] = frozenlake_translator.GameDescriber
REGISTRY["frozenlake_basic_translator"] = frozenlake_translator.TransitionTranslator
REGISTRY["frozenlake_policies"] = [frozenlake_policies.dedicated_1_policy, frozenlake_policies.dedicated_2_policy, frozenlake_policies.dedicated_3_policy, frozenlake_policies.dedicated_4_policy, frozenlake_policies.pseudo_random_policy, frozenlake_policies.real_random_policy]


REGISTRY["mountaincarContinuous_init_translator"] = mountaincarContinuous_translator.GameDescriber
REGISTRY["mountaincarContinuous_basic_translator"] = mountaincarContinuous_translator.TransitionTranslator
REGISTRY["mountaincarContinuous_policies"] = [mountaincarContinuous_policies.pseudo_random_policy, mountaincarContinuous_policies.real_random_policy]



# Atari 
REGISTRY["RepresentedAsteroids_init_translator"] = Asteroids_translator.GameDescriber
REGISTRY["RepresentedAsteroids_basic_translator"] = Asteroids_translator.TransitionTranslator
REGISTRY["RepresentedAsteroids_basic_policies"] = []

REGISTRY["RepresentedBattleZone_init_translator"] = BattleZone_translator.GameDescriber
REGISTRY["RepresentedBattleZone_basic_translator"] = BattleZone_translator.TransitionTranslator
REGISTRY["RepresentedBattleZone_basic_policies"] = []

REGISTRY["RepresentedBerzerk_init_translator"] = Berzerk_translator.GameDescriber
REGISTRY["RepresentedBerzerk_basic_translator"] = Berzerk_translator.TransitionTranslator
REGISTRY["RepresentedBerzerk_basic_policies"] = []

REGISTRY["RepresentedBowling_init_translator"] = Bowling_translator.GameDescriber
REGISTRY["RepresentedBowling_basic_translator"] = Bowling_translator.TransitionTranslator
REGISTRY["RepresentedBowling_basic_policies"] = []

REGISTRY["RepresentedBreakout_init_translator"] = Breakout_translator.GameDescriber
REGISTRY["RepresentedBreakout_basic_translator"] = Breakout_translator.TransitionTranslator
REGISTRY["RepresentedBreakout_basic_policies"] = []

REGISTRY["RepresentedSkiing_init_translator"] = Skiing_translator.GameDescriber
REGISTRY["RepresentedSkiing_basic_translator"] = Skiing_translator.TransitionTranslator
REGISTRY["RepresentedSkiing_basic_policies"] = []


REGISTRY["RepresentedBoxing_init_translator"] = Boxing_translator.GameDescriber
REGISTRY["RepresentedBoxing_basic_translator"] = Boxing_translator.TransitionTranslator
REGISTRY["RepresentedBoxing_basic_policies"] = [
    Boxing_policies.real_random_policy,
    Boxing_policies.pseudo_random_policy,
    Boxing_policies.dedicated_1_policy,
    Boxing_policies.dedicated_2_policy,
    Boxing_policies.dedicated_3_policy,
    Boxing_policies.dedicated_4_policy,
    Boxing_policies.dedicated_5_policy,
    Boxing_policies.dedicated_6_policy,
    Boxing_policies.dedicated_7_policy,
    Boxing_policies.dedicated_8_policy,
    Boxing_policies.dedicated_9_policy,
    Boxing_policies.dedicated_10_policy,
    Boxing_policies.dedicated_11_policy,
    Boxing_policies.dedicated_12_policy,
    Boxing_policies.dedicated_13_policy,
    Boxing_policies.dedicated_14_policy,
    Boxing_policies.dedicated_15_policy,
    Boxing_policies.dedicated_16_policy,
    Boxing_policies.dedicated_17_policy,
    Boxing_policies.dedicated_18_policy
]

REGISTRY["RepresentedPong_init_translator"] = Pong_translator.GameDescriber
REGISTRY["RepresentedPong_basic_translator"] = Pong_translator.TransitionTranslator
REGISTRY["RepresentedPong_basic_policies"] = [
    Pong_policies.real_random_policy,
    Pong_policies.pseudo_random_policy,
    Pong_policies.dedicated_1_policy,
    Pong_policies.dedicated_2_policy,
    Pong_policies.dedicated_3_policy,
    Pong_policies.dedicated_4_policy,
    Pong_policies.dedicated_5_policy,
    Pong_policies.dedicated_6_policy,
]

REGISTRY["RepresentedMsPacman_init_translator"] = mspacman_translator.GameDescriber
REGISTRY["RepresentedMsPacman_basic_translator"] = mspacman_translator.TransitionTranslator
REGISTRY["RepresentedMsPacman_basic_policies"] = [
    mspacman_policies.real_random_policy,
    mspacman_policies.pseudo_random_policy,
    mspacman_policies.dedicated_1_policy,
    mspacman_policies.dedicated_2_policy,
    mspacman_policies.dedicated_3_policy,
    mspacman_policies.dedicated_4_policy,
    mspacman_policies.dedicated_5_policy,
    mspacman_policies.dedicated_6_policy,
    mspacman_policies.dedicated_7_policy,
    mspacman_policies.dedicated_8_policy,
    mspacman_policies.dedicated_9_policy,
]

REGISTRY["RepresentedMontezumaRevenge_init_translator"] = montezumarevenge_translator.GameDescriber
REGISTRY["RepresentedMontezumaRevenge_basic_translator"] = montezumarevenge_translator.TransitionTranslator
REGISTRY["RepresentedMontezumaRevenge_basic_policies"] = [
    montezumarevenge_policies.real_random_policy,
    montezumarevenge_policies.pseudo_random_policy,
    montezumarevenge_policies.dedicated_1_policy,
    montezumarevenge_policies.dedicated_2_policy,
    montezumarevenge_policies.dedicated_3_policy,
    montezumarevenge_policies.dedicated_4_policy,
    montezumarevenge_policies.dedicated_5_policy,
    montezumarevenge_policies.dedicated_6_policy,
    montezumarevenge_policies.dedicated_7_policy,
    montezumarevenge_policies.dedicated_8_policy,
    montezumarevenge_policies.dedicated_9_policy,
    montezumarevenge_policies.dedicated_10_policy,
    montezumarevenge_policies.dedicated_11_policy,
    montezumarevenge_policies.dedicated_12_policy,
    montezumarevenge_policies.dedicated_13_policy,
    montezumarevenge_policies.dedicated_14_policy,
    montezumarevenge_policies.dedicated_15_policy,
    montezumarevenge_policies.dedicated_16_policy,
    montezumarevenge_policies.dedicated_17_policy,
    montezumarevenge_policies.dedicated_18_policy,
]

REGISTRY["RepresentedMsPacman_init_translator"] = mspacman_translator.GameDescriber
REGISTRY["RepresentedMsPacman_basic_translator"] = mspacman_translator.TransitionTranslator
REGISTRY["RepresentedMsPacman_basic_policies"] = [
    mspacman_policies.real_random_policy,
    mspacman_policies.pseudo_random_policy,
    mspacman_policies.dedicated_1_policy,
    mspacman_policies.dedicated_2_policy,
    mspacman_policies.dedicated_3_policy,
    mspacman_policies.dedicated_4_policy,
    mspacman_policies.dedicated_5_policy,
    mspacman_policies.dedicated_6_policy,
    mspacman_policies.dedicated_7_policy,
    mspacman_policies.dedicated_8_policy,
    mspacman_policies.dedicated_9_policy,
]

REGISTRY["RepresentedMontezumaRevenge_init_translator"] = montezumarevenge_translator.GameDescriber
REGISTRY["RepresentedMontezumaRevenge_basic_translator"] = montezumarevenge_translator.TransitionTranslator
REGISTRY["RepresentedMontezumaRevenge_basic_policies"] = [
    montezumarevenge_policies.real_random_policy,
    montezumarevenge_policies.pseudo_random_policy,
    montezumarevenge_policies.dedicated_1_policy,
    montezumarevenge_policies.dedicated_2_policy,
    montezumarevenge_policies.dedicated_3_policy,
    montezumarevenge_policies.dedicated_4_policy,
    montezumarevenge_policies.dedicated_5_policy,
    montezumarevenge_policies.dedicated_6_policy,
    montezumarevenge_policies.dedicated_7_policy,
    montezumarevenge_policies.dedicated_8_policy,
    montezumarevenge_policies.dedicated_9_policy,
    montezumarevenge_policies.dedicated_10_policy,
    montezumarevenge_policies.dedicated_11_policy,
    montezumarevenge_policies.dedicated_12_policy,
    montezumarevenge_policies.dedicated_13_policy,
    montezumarevenge_policies.dedicated_14_policy,
    montezumarevenge_policies.dedicated_15_policy,
    montezumarevenge_policies.dedicated_16_policy,
    montezumarevenge_policies.dedicated_17_policy,
    montezumarevenge_policies.dedicated_18_policy,
]

## For mujoco env


from .mujoco import invertedPendulum_translator, invertedPendulum_policies
from .mujoco import invertedDoublePendulum_translator, invertedDoublePendulum_policies

from .mujoco import swimmer_translator, swimmer_policies

from .mujoco import reacher_translator, reacher_policies

from .mujoco import hopper_translator, hopper_policies
from .mujoco import walker2d_translator, walker2d_policies





REGISTRY["invertedPendulum_init_translator"] = invertedPendulum_translator.GameDescriber
REGISTRY["invertedPendulum_basic_translator"] = invertedPendulum_translator.TransitionTranslator
REGISTRY["invertedPendulum_policies"] = [invertedPendulum_policies.pseudo_random_policy, invertedPendulum_policies.real_random_policy]
REGISTRY["invertedDoublePendulum_init_translator"] = invertedDoublePendulum_translator.GameDescriber
REGISTRY["invertedDoublePendulum_basic_translator"] = invertedDoublePendulum_translator.TransitionTranslator
REGISTRY["invertedDoublePendulum_policies"] = [invertedDoublePendulum_policies.pseudo_random_policy, invertedDoublePendulum_policies.real_random_policy]


REGISTRY["swimmer_init_translator"] = swimmer_translator.GameDescriber
REGISTRY["swimmer_basic_translator"] = swimmer_translator.TransitionTranslator
REGISTRY["swimmer_policies"] = [swimmer_policies.pseudo_random_policy, swimmer_policies.real_random_policy]

REGISTRY["reacher_init_translator"] = reacher_translator.GameDescriber
REGISTRY["reacher_basic_translator"] = reacher_translator.TransitionTranslator
REGISTRY["reacher_policies"] = [reacher_policies.pseudo_random_policy, reacher_policies.real_random_policy]

REGISTRY["hopper_init_translator"] = hopper_translator.GameDescriber
REGISTRY["hopper_basic_translator"] = hopper_translator.TransitionTranslator
REGISTRY["hopper_policies"] = [hopper_policies.pseudo_random_policy, hopper_policies.real_random_policy]
REGISTRY["walker2d_init_translator"] = walker2d_translator.GameDescriber
REGISTRY["walker2d_basic_translator"] = walker2d_translator.TransitionTranslator
REGISTRY["walker2d_policies"] = [walker2d_policies.pseudo_random_policy, walker2d_policies.real_random_policy]


from .mujoco import halfcheetah_translator, halfcheetah_policies
REGISTRY["halfcheetah_init_translator"] = halfcheetah_translator.GameDescriber
REGISTRY["halfcheetah_basic_translator"] = halfcheetah_translator.TransitionTranslator
REGISTRY["halfcheetah_policies"] = [halfcheetah_policies.pseudo_random_policy, halfcheetah_policies.real_random_policy]

from .mujoco import pusher_translator, pusher_policies
REGISTRY["pusher_init_translator"] = pusher_translator.GameDescriber
REGISTRY["pusher_basic_translator"] = pusher_translator.TransitionTranslator
REGISTRY["pusher_policies"] = [pusher_policies.pseudo_random_policy, pusher_policies.real_random_policy]

from .mujoco import ant_translator, ant_policies
REGISTRY["ant_init_translator"] = ant_translator.GameDescriber
REGISTRY["ant_basic_translator"] = ant_translator.TransitionTranslator
REGISTRY["ant_policies"] = [ant_policies.pseudo_random_policy, ant_policies.real_random_policy]
