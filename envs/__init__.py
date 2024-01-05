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
register_environments()

from .mujoco import ant_translator, ant_policies

REGISTRY = {}
REGISTRY["sampling_wrapper"] = SettableStateEnv
REGISTRY["base_env"] = BaseEnv
REGISTRY["cart_init_translator"] = cartpole_translator.GameDescriber
REGISTRY["cart_basic_translator"] = cartpole_translator.BasicStateSequenceTranslator
REGISTRY["acrobot_init_translator"] = acrobot_translator.GameDescriber
REGISTRY["acrobot_basic_translator"] = acrobot_translator.BasicStateSequenceTranslator
REGISTRY["mountaincar_init_translator"] = mountaincar_translator.GameDescriber
REGISTRY["mountaincar_basic_translator"] = mountaincar_translator.BasicStateSequenceTranslator

REGISTRY["cart_policies"] = [cartpole_policies.dedicated_1_policy, cartpole_policies.dedicated_2_policy, cartpole_policies.pseudo_random_policy, cartpole_policies.real_random_policy]
REGISTRY["acrobot_policies"] = [acrobot_policies.dedicated_1_policy, acrobot_policies.dedicated_2_policy, acrobot_policies.dedicated_3_policy, acrobot_policies.pseudo_random_policy, acrobot_policies.real_random_policy]
REGISTRY["mountaincar_policies"] = [mountaincar_policies.dedicated_1_policy, mountaincar_policies.dedicated_2_policy, mountaincar_policies.dedicated_3_policy, mountaincar_policies.pseudo_random_policy, mountaincar_policies.real_random_policy]

REGISTRY["lunarLander_init_translator"] = LunarLander_translator.GameDescriber
REGISTRY["lunarLander_basic_translator"] = LunarLander_translator.BasicStateSequenceTranslator
REGISTRY["lunarLander_policies"] = [LunarLander_policies.dedicated_1_policy, LunarLander_policies.dedicated_2_policy, LunarLander_policies.dedicated_3_policy,LunarLander_policies.dedicated_4_policy, LunarLander_policies.pseudo_random_policy, LunarLander_policies.real_random_policy]

REGISTRY["blackjack_init_translator"] = blackjack_translator.GameDescriber
REGISTRY["blackjack_basic_translator"] = blackjack_translator.BasicStateSequenceTranslator
REGISTRY["blackjack_policies"] = [blackjack_policies.dedicated_1_policy, blackjack_policies.dedicated_2_policy, blackjack_policies.pseudo_random_policy, blackjack_policies.real_random_policy]

REGISTRY["taxi_init_translator"] = taxi_translator.GameDescriber
REGISTRY["taxi_basic_translator"] = taxi_translator.BasicStateSequenceTranslator
REGISTRY["taxi_policies"] = [taxi_policies.dedicated_1_policy, taxi_policies.dedicated_2_policy, taxi_policies.dedicated_3_policy, taxi_policies.dedicated_4_policy, taxi_policies.dedicated_5_policy, taxi_policies.dedicated_6_policy, taxi_policies.pseudo_random_policy, taxi_policies.real_random_policy]

REGISTRY["cliffwalking_init_translator"] = cliffwalking_translator.GameDescriber
REGISTRY["cliffwalking_basic_translator"] = cliffwalking_translator.BasicStateSequenceTranslator
REGISTRY["cliffwalking_policies"] = [cliffwalking_policies.dedicated_1_policy, cliffwalking_policies.dedicated_2_policy, cliffwalking_policies.dedicated_3_policy, cliffwalking_policies.dedicated_4_policy, cliffwalking_policies.pseudo_random_policy, cliffwalking_policies.real_random_policy]

REGISTRY["frozenlake_init_translator"] = frozenlake_translator.GameDescriber
REGISTRY["frozenlake_basic_translator"] = frozenlake_translator.BasicStateSequenceTranslator
REGISTRY["frozenlake_policies"] = [frozenlake_policies.dedicated_1_policy, frozenlake_policies.dedicated_2_policy, frozenlake_policies.dedicated_3_policy, frozenlake_policies.dedicated_4_policy, frozenlake_policies.pseudo_random_policy, frozenlake_policies.real_random_policy]


REGISTRY["mountaincarContinuous_init_translator"] = mountaincarContinuous_translator.GameDescriber
REGISTRY["mountaincarContinuous_basic_translator"] = mountaincarContinuous_translator.BasicStateSequenceTranslator
REGISTRY["mountaincarContinuous_policies"] = [mountaincarContinuous_policies.pseudo_random_policy, mountaincarContinuous_policies.real_random_policy]


REGISTRY["RepresentedBoxing_init_translator"] = Boxing_translator.GameDescriber
REGISTRY["RepresentedBoxing_basic_translator"] = Boxing_translator.BasicStateSequenceTranslator
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
REGISTRY["RepresentedPong_basic_translator"] = Pong_translator.BasicStateSequenceTranslator
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

REGISTRY["ant_init_translator"] = ant_translator.GameDescriber
REGISTRY["ant_basic_translator"] = ant_translator.BasicStateSequenceTranslator
REGISTRY["ant_policies"] = [ant_policies.pseudo_random_policy, ant_policies.real_random_policy]