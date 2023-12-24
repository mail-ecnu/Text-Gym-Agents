import gym
import ale_py
import numpy as np
from atariari.benchmark.wrapper import AtariARIWrapper
from typing import Optional, Union



class RepresentedAtariEnv(gym.Wrapper):
    def __init__(self, env_name, render_mode=None):
        super().__init__(AtariARIWrapper(gym.make(env_name, render_mode=render_mode)))
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
    def __init__(self, render_mode: Optional[str]=None):
        env_name = "MsPacmanNoFrameskip-v4"
        super().__init__(env_name=env_name, render_mode=render_mode)


class RepresentedBowling(RepresentedAtariEnv):
    def __init__(self, render_mode: Optional[str]=None):
        env_name = "BowlingNoFrameskip-v4"
        super().__init__(env_name=env_name, render_mode=render_mode)


class RepresentedBoxing(RepresentedAtariEnv):
    def __init__(self, render_mode: Optional[str]=None):
        env_name = "BoxingNoFrameskip-v4"
        super().__init__(env_name=env_name, render_mode=render_mode)


class RepresentedBreakout(RepresentedAtariEnv):
    def __init__(self, render_mode: Optional[str]=None):
        env_name = "BreakoutNoFrameskip-v4"
        super().__init__(env_name=env_name, render_mode=render_mode)


class RepresentedDemonAttack(RepresentedAtariEnv):
    def __init__(self, render_mode: Optional[str]=None):
        env_name = "DemonAttackNoFrameskip-v4"
        super().__init__(env_name=env_name, render_mode=render_mode)


class RepresentedFreeway(RepresentedAtariEnv):
    def __init__(self, render_mode: Optional[str]=None):
        env_name = "FreewayNoFrameskip-v4"
        super().__init__(env_name=env_name, render_mode=render_mode)


class RepresentedFrostbite(RepresentedAtariEnv):
    def __init__(self, render_mode: Optional[str]=None):
        env_name = "FrostbiteNoFrameskip-v4"
        super().__init__(env_name=env_name, render_mode=render_mode)


class RepresentedHero(RepresentedAtariEnv):
    def __init__(self, render_mode: Optional[str]=None):
        env_name = "HeroNoFrameskip-v4"
        super().__init__(env_name=env_name, render_mode=render_mode)


class RepresentedMontezumaRevenge(RepresentedAtariEnv):
    def __init__(self, render_mode: Optional[str]=None):
        env_name = "MontezumaRevengeNoFrameskip-v4"
        super().__init__(env_name=env_name, render_mode=render_mode)


class RepresentedPitfall(RepresentedAtariEnv):
    def __init__(self, render_mode: Optional[str]=None):
        env_name = "PitfallNoFrameskip-v4"
        super().__init__(env_name=env_name, render_mode=render_mode)


class RepresentedPong(RepresentedAtariEnv):
    def __init__(self, render_mode: Optional[str]=None):
        env_name = "PongNoFrameskip-v4"
        super().__init__(env_name=env_name, render_mode=render_mode)


class RepresentedPrivateEye(RepresentedAtariEnv):
    def __init__(self, render_mode: Optional[str]=None):
        env_name = "PrivateEyeNoFrameskip-v4"
        super().__init__(env_name=env_name, render_mode=render_mode)


class RepresentedQbert(RepresentedAtariEnv):
    def __init__(self, render_mode: Optional[str]=None):
        env_name = "QbertNoFrameskip-v4"
        super().__init__(env_name=env_name, render_mode=render_mode)


class RepresentedRiverraid(RepresentedAtariEnv):
    def __init__(self, render_mode: Optional[str]=None):
        env_name = "RiverraidNoFrameskip-v4"
        super().__init__(env_name=env_name, render_mode=render_mode)


class RepresentedSeaquest(RepresentedAtariEnv):
    def __init__(self, render_mode: Optional[str]=None):
        env_name = "SeaquestNoFrameskip-v4"
        super().__init__(env_name=env_name, render_mode=render_mode)


class RepresentedSpaceInvaders(RepresentedAtariEnv):
    def __init__(self, render_mode: Optional[str]=None):
        env_name = "SpaceInvadersNoFrameskip-v4"
        super().__init__(env_name=env_name, render_mode=render_mode)


class RepresentedTennis(RepresentedAtariEnv):
    def __init__(self, render_mode: Optional[str]=None):
        env_name = "TennisNoFrameskip-v4"
        super().__init__(env_name=env_name, render_mode=render_mode)


class RepresentedVenture(RepresentedAtariEnv):
    def __init__(self, render_mode: Optional[str]=None):
        env_name = "VentureNoFrameskip-v4"
        super().__init__(env_name=env_name, render_mode=render_mode)


class RepresentedVideoPinball(RepresentedAtariEnv):
    def __init__(self, render_mode: Optional[str]=None):
        env_name = "VideoPinballNoFrameskip-v4"
        super().__init__(env_name=env_name, render_mode=render_mode)


def env_factory(env_class):
    def _create_instance(render_mode=None):
        return env_class(render_mode=render_mode)
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