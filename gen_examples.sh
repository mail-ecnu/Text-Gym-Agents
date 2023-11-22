# # (Wenhao Li, 2023-09-06, 09:20)
# # Important !!!
# # For environment that truncate at 200 steps automatically, you could set the max_episode_len to greater than 200.
# # Otherwise, you need to set the max_episode_len to 200 manually (for fair comparison).

# # L2
# ## Cartpole env
# python gen_few_shots_examples.py --env_name CartPole-v0 --init_summarizer cart_init_translator --curr_summarizer cart_basic_translator --decider random_actor --max_episode_len 1000 --n_episodes 5

# ## Acrobot-v1 env
# # Note that we want to use the Acrobot-v0 but it is deprecated in gym 0.26.2.
# # So we use Acrobot-v1 instead and set the max_episode_len to 200.
# python gen_few_shots_examples.py --env_name Acrobot-v1 --init_summarizer acrobot_init_translator --curr_summarizer acrobot_basic_translator --decider random_actor --max_episode_len 200 --n_episodes 5

# ## MountainCar-v0 env
# python gen_few_shots_examples.py --env_name MountainCar-v0 --init_summarizer mountaincar_init_translator --curr_summarizer mountaincar_basic_translator --decider random_actor --max_episode_len 1000 --n_episodes 5

# ## LunarLander-v2 env
# python gen_few_shots_examples.py --env_name LunarLander-v2 --init_summarizer lunarLander_init_translator --curr_summarizer lunarLander_basic_translator --decider random_actor --max_episode_len 1000 --n_episodes 5

# # Blacjack-v1 env
# # (Wenhao Li, 2023-09-06, 10:00)
# # random_actor is too weak, so we need to set the n_episodes to a larger number (100).
# # the n_episodes should be set to a smaller number for other more powerful deciders.

# # (Wenhao Li, 2023-09-07, 20:25)
# # reset n_episodes to 2 (default value) for fair comparison.
# python gen_few_shots_examples.py --env_name Blackjack-v1 --init_summarizer blackjack_init_translator --curr_summarizer blackjack_basic_translator --decider random_actor --max_episode_len 200 --n_episodes 5

# # Taxi-v3 env
# python gen_few_shots_examples.py --env_name Taxi-v3 --init_summarizer taxi_init_translator --curr_summarizer taxi_basic_translator --decider random_actor --max_episode_len 1000 --n_episodes 5

# # CliffWalking-v0 env
# python gen_few_shots_examples.py --env_name CliffWalking-v0 --init_summarizer cliffwalking_init_translator --curr_summarizer cliffwalking_basic_translator --decider random_actor --max_episode_len 200 --n_episodes 5

# # FrozenLake-v1 env
# python gen_few_shots_examples.py --env_name FrozenLake-v1 --init_summarizer frozenlake_init_translator --curr_summarizer frozenlake_basic_translator --decider random_actor --max_episode_len 1000 --n_episodes 5

# L4
## Cartpole env
python gen_few_shots_examples.py --env_name CartPole-v0 --init_summarizer cart_init_translator --curr_summarizer cart_basic_translator --decider expert --policy_path RL_based/checkpoints/CartPole-v0/expert/policy.pth --max_episode_len 200 --n_episodes 5

python gen_few_shots_examples.py --env_name LunarLander-v2 --init_summarizer lunarLander_init_translator --curr_summarizer lunarLander_basic_translator --decider expert --policy_path RL_based/checkpoints/LunarLander-v2/expert/policy.pth --max_episode_len 200 --n_episodes 5

python gen_few_shots_examples.py --env_name Acrobot-v1 --init_summarizer acrobot_init_translator --curr_summarizer acrobot_basic_translator --decider expert --policy_path RL_based/checkpoints/Acrobot-v1/expert/policy.pth --max_episode_len 200 --n_episodes 5

python gen_few_shots_examples.py --env_name MountainCar-v0 --init_summarizer mountaincar_init_translator --curr_summarizer mountaincar_basic_translator --decider expert --policy_path RL_based/checkpoints/MountainCar-v0/expert/policy.pth --max_episode_len 200 --n_episodes 5

python gen_few_shots_examples.py --env_name Blackjack-v1 --init_summarizer blackjack_init_translator --curr_summarizer blackjack_basic_translator --decider expert --policy_path RL_based/checkpoints/Blackjack-v1/expert/policy.pth --max_episode_len 200 --n_episodes 5

python gen_few_shots_examples.py --env_name Taxi-v3 --init_summarizer taxi_init_translator --curr_summarizer taxi_basic_translator --decider expert --policy_path RL_based/checkpoints/Taxi-v3/expert/policy.pth --max_episode_len 200 --n_episodes 5

python gen_few_shots_examples.py --env_name CliffWalking-v0 --init_summarizer cliffwalking_init_translator --curr_summarizer cliffwalking_basic_translator --decider expert --policy_path RL_based/checkpoints/CliffWalking-v0/expert/policy.pth --max_episode_len 200 --n_episodes 5

python gen_few_shots_examples.py --env_name FrozenLake-v1 --init_summarizer frozenlake_init_translator --curr_summarizer frozenlake_basic_translator --decider expert --policy_path RL_based/checkpoints/FrozenLake-v1/expert/policy.pth --max_episode_len 200 --n_episodes 5
