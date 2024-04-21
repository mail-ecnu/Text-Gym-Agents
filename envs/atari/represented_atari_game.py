import gym
import ale_py
import numpy as np
from atariari.benchmark.wrapper import AtariARIWrapper
from typing import Optional, Union



class RepresentedAtariEnv(gym.Wrapper):
    def __init__(self, env_name, render_mode=None, frameskip=4):
        super().__init__(AtariARIWrapper(gym.make(env_name, render_mode=render_mode, frameskip=frameskip)))
        self.metadata = self.env.metadata
        self.env_name = env_name
        self.observation = None
        self.info = {}
        self.action_space = self.env.action_space
        _ = self.env.reset()
        obs = self.env.labels()
        obs_dim = len(obs)
        self.obs_label = obs.keys()
        self.observation_space = gym.spaces.Box(low=-np.inf, high=np.inf, shape=(obs_dim,), dtype=np.float32)

    def step(self, action):
        original_next_obs, reward, env_done, env_truncated, info = self.env.step(action)
        next_obs = self.env.labels()
        self.obs_label = next_obs.keys()
        self.observation = next_obs
        return np.array(list(next_obs.values())), reward, env_done, env_truncated, info

    def reset(self, seed=0):
        obs_original, info = self.env.reset(seed=seed)
        obs = self.env.labels()
        self.obs_label = obs.keys()
        self.observation = obs
        return np.array(list(obs.values())), info

    def get_info(self):
        return self.observation

    def render(self, render_mode=None):
        return self.env.render()

class RepresentedMsPacman(RepresentedAtariEnv):
    def __init__(self, render_mode: Optional[str]=None, frameskip: int=4):
        env_name = "MsPacmanDeterministic-v4"
        super().__init__(env_name=env_name, render_mode=render_mode, frameskip=frameskip)

class RepresentedBowling(RepresentedAtariEnv):
    def __init__(self, render_mode: Optional[str]=None, frameskip: int=4):
        env_name = "BowlingDeterministic-v4"
        super().__init__(env_name=env_name, render_mode=render_mode, frameskip=frameskip)

class RepresentedBoxing(RepresentedAtariEnv):
    def __init__(self, render_mode: Optional[str]=None, frameskip: int=4):
        env_name = "BoxingDeterministic-v4"
        super().__init__(env_name=env_name, render_mode=render_mode, frameskip=frameskip)

class RepresentedBreakout(RepresentedAtariEnv):
    def __init__(self, render_mode: Optional[str]=None, frameskip: int=4):
        env_name = "BreakoutDeterministic-v4"
        super().__init__(env_name=env_name, render_mode=render_mode, frameskip=frameskip)

class RepresentedDemonAttack(RepresentedAtariEnv):
    def __init__(self, render_mode: Optional[str]=None, frameskip: int=4):
        env_name = "DemonAttackDeterministic-v4"
        super().__init__(env_name=env_name, render_mode=render_mode, frameskip=frameskip)

class RepresentedFreeway(RepresentedAtariEnv):
    def __init__(self, render_mode: Optional[str]=None, frameskip: int=4):
        env_name = "FreewayDeterministic-v4"
        super().__init__(env_name=env_name, render_mode=render_mode, frameskip=frameskip)

class RepresentedFrostbite(RepresentedAtariEnv):
    def __init__(self, render_mode: Optional[str]=None, frameskip: int=4):
        env_name = "FrostbiteDeterministic-v4"
        super().__init__(env_name=env_name, render_mode=render_mode, frameskip=frameskip)

class RepresentedHero(RepresentedAtariEnv):
    def __init__(self, render_mode: Optional[str]=None, frameskip: int=4):
        env_name = "HeroDeterministic-v4"
        super().__init__(env_name=env_name, render_mode=render_mode, frameskip=frameskip)

class RepresentedMontezumaRevenge(RepresentedAtariEnv):
    def __init__(self, render_mode: Optional[str]=None, frameskip: int=4):
        env_name = "MontezumaRevengeDeterministic-v4"
        super().__init__(env_name=env_name, render_mode=render_mode, frameskip=frameskip)

class RepresentedPitfall(RepresentedAtariEnv):
    def __init__(self, render_mode: Optional[str]=None, frameskip: int=4):
        env_name = "PitfallDeterministic-v4"
        super().__init__(env_name=env_name, render_mode=render_mode, frameskip=frameskip)

class RepresentedPong(RepresentedAtariEnv):
    def __init__(self, render_mode: Optional[str]=None, frameskip: int=4):
        env_name = "PongDeterministic-v4"
        super().__init__(env_name=env_name, render_mode=render_mode, frameskip=frameskip)

class RepresentedPrivateEye(RepresentedAtariEnv):
    def __init__(self, render_mode: Optional[str]=None, frameskip: int=4):
        env_name = "PrivateEyeDeterministic-v4"
        super().__init__(env_name=env_name, render_mode=render_mode, frameskip=frameskip)

class RepresentedQbert(RepresentedAtariEnv):
    def __init__(self, render_mode: Optional[str]=None, frameskip: int=4):
        env_name = "QbertDeterministic-v4"
        super().__init__(env_name=env_name, render_mode=render_mode, frameskip=frameskip)

class RepresentedRiverraid(RepresentedAtariEnv):
    def __init__(self, render_mode: Optional[str]=None, frameskip: int=4):
        env_name = "RiverraidDeterministic-v4"
        super().__init__(env_name=env_name, render_mode=render_mode, frameskip=frameskip)

class RepresentedSeaquest(RepresentedAtariEnv):
    def __init__(self, render_mode: Optional[str]=None, frameskip: int=4):
        env_name = "SeaquestDeterministic-v4"
        super().__init__(env_name=env_name, render_mode=render_mode, frameskip=frameskip)

class RepresentedSpaceInvaders(RepresentedAtariEnv):
    def __init__(self, render_mode: Optional[str]=None, frameskip: int=4):
        env_name = "SpaceInvadersDeterministic-v4"
        super().__init__(env_name=env_name, render_mode=render_mode, frameskip=frameskip)

class RepresentedTennis(RepresentedAtariEnv):
    def __init__(self, render_mode: Optional[str]=None, frameskip: int=4):
        env_name = "TennisDeterministic-v4"
        super().__init__(env_name=env_name, render_mode=render_mode, frameskip=frameskip)

class RepresentedVenture(RepresentedAtariEnv):
    def __init__(self, render_mode: Optional[str]=None, frameskip: int=4):
        env_name = "VentureDeterministic-v4"
        super().__init__(env_name=env_name, render_mode=render_mode, frameskip=frameskip)

class RepresentedVideoPinball(RepresentedAtariEnv):
    def __init__(self, render_mode: Optional[str]=None, frameskip: int=4):
        env_name = "VideoPinballDeterministic-v4"
        super().__init__(env_name=env_name, render_mode=render_mode, frameskip=frameskip)


def env_factory(env_class):
    def _create_instance(render_mode=None, frameskip=4):
        return env_class(render_mode=render_mode, frameskip=frameskip)
    return _create_instance


def register_environments():
    env_classes = {
        'RepresentedMsPacman-v0': RepresentedMsPacman,
        'RepresentedBowling-v0': RepresentedBowling,
        'RepresentedBoxing-v0': RepresentedBoxing,
        'RepresentedBreakout-v0': RepresentedBreakout,
        'RepresentedDemonAttack-v0': RepresentedDemonAttack,
        'RepresentedFreeway-v0': RepresentedFreeway,
        'RepresentedFrostbite-v0': RepresentedFrostbite,
        'RepresentedHero-v0': RepresentedHero,
        'RepresentedMontezumaRevenge-v0': RepresentedMontezumaRevenge,
        'RepresentedPitfall-v0': RepresentedPitfall,
        'RepresentedPong-v0': RepresentedPong,
        'RepresentedPrivateEye-v0': RepresentedPrivateEye,
        'RepresentedQbert-v0': RepresentedQbert,
        'RepresentedRiverraid-v0': RepresentedRiverraid,
        'RepresentedSeaquest-v0': RepresentedSeaquest,
        'RepresentedSpaceInvaders-v0': RepresentedSpaceInvaders,
        'RepresentedTennis-v0': RepresentedTennis,
        'RepresentedVenture-v0': RepresentedVenture,
        'RepresentedVideoPinball-v0': RepresentedVideoPinball
    }

    for env_name, env_class in env_classes.items():
        gym.register(
            id=env_name,
            entry_point=env_factory(env_class),
        )


# register_environments()
# env_classes = {
#     'RepresentedMsPacman-v0': RepresentedMsPacman,
#     'RepresentedBowling-v0': RepresentedBowling,
#     'RepresentedBoxing-v0': RepresentedBoxing,
#     'RepresentedBreakout-v0': RepresentedBreakout,
#     'RepresentedDemonAttack-v0': RepresentedDemonAttack,
#     'RepresentedFreeway-v0': RepresentedFreeway,
#     'RepresentedFrostbite-v0': RepresentedFrostbite,
#     'RepresentedHero-v0': RepresentedHero,
#     'RepresentedMontezumaRevenge-v0': RepresentedMontezumaRevenge,
#     'RepresentedPitfall-v0': RepresentedPitfall,
#     'RepresentedPong-v0': RepresentedPong,
#     'RepresentedPrivateEye-v0': RepresentedPrivateEye,
#     'RepresentedQbert-v0': RepresentedQbert,
#     'RepresentedRiverraid-v0': RepresentedRiverraid,
#     'RepresentedSeaquest-v0': RepresentedSeaquest,
#     'RepresentedSpaceInvaders-v0': RepresentedSpaceInvaders,
#     'RepresentedTennis-v0': RepresentedTennis,
#     'RepresentedVenture-v0': RepresentedVenture,
#     'RepresentedVideoPinball-v0': RepresentedVideoPinball
# }
#
# for env, env_class in env_classes.items():
#     env_1 = env_class()
#     env_name = env_1.env_name
#     env_2 = gym.make(env_name)
#     print(env_name, env_1.action_space == env_2.action_space, env_1.action_space)