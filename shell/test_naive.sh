# Blackjack-v1
# Naive Actor
python main_reflexion.py --env_name Blackjack-v1 --init_summarizer blackjack_init_translator --curr_summarizer blackjack_basic_translator --decider naive_actor --prompt_level 1 --num_trails 50
python main_reflexion.py --env_name Blackjack-v1 --init_summarizer blackjack_init_translator --curr_summarizer blackjack_basic_translator --decider naive_actor --prompt_level 2 --num_trails 50 --distiller traj_distiller --prompt_path "envs/toy_text/few_shot_examples/blackjack"
python main_reflexion.py --env_name Blackjack-v1 --init_summarizer blackjack_init_translator --curr_summarizer blackjack_basic_translator --decider naive_actor --prompt_level 3 --num_trails 50 --use_short_mem 0 --distiller traj_distiller
python main_reflexion.py --env_name Blackjack-v1 --init_summarizer blackjack_init_translator --curr_summarizer blackjack_basic_translator --decider naive_actor --prompt_level 4 --num_trails 50 --distiller traj_distiller --prompt_path "envs/toy_text/few_shot_examples/blackjack"
python main_reflexion.py --env_name Blackjack-v1 --init_summarizer blackjack_init_translator --curr_summarizer blackjack_basic_translator --decider naive_actor --prompt_level 5 --num_trails 50

# LunarLander-v2
# Naive Actor
python main_reflexion.py --env_name LunarLander-v2 --init_summarizer lunarLander_init_translator --curr_summarizer lunarLander_basic_translator --decider naive_actor --prompt_level 1 --num_trails 1 --seed 0
python main_reflexion.py --env_name LunarLander-v2 --init_summarizer lunarLander_init_translator --curr_summarizer lunarLander_basic_translator --decider naive_actor --prompt_level 2 --num_trails 1 --distiller traj_distiller --prompt_path "envs/box2d/few_shot_examples/lunarlander" --seed 0
python main_reflexion.py --env_name LunarLander-v2 --init_summarizer lunarLander_init_translator --curr_summarizer lunarLander_basic_translator --decider naive_actor --prompt_level 3 --num_trails 5 --distiller traj_distiller --use_short_mem 0 --seed 0
python main_reflexion.py --env_name LunarLander-v2 --init_summarizer lunarLander_init_translator --curr_summarizer lunarLander_basic_translator --decider naive_actor --prompt_level 4 --num_trails 1 --distiller traj_distiller --prompt_path "envs/box2d/few_shot_examples/lunarlander" --seed 0
python main_reflexion.py --env_name LunarLander-v2 --init_summarizer lunarLander_init_translator --curr_summarizer lunarLander_basic_translator --decider naive_actor --prompt_level 5 --num_trails 1 --seed 0

# Acrobot-v1
# Naive Actor
python main_reflexion.py --env_name Acrobot-v1 --init_summarizer acrobot_init_translator --curr_summarizer acrobot_basic_translator --decider naive_actor --prompt_level 1 --num_trails 1
python main_reflexion.py --env_name Acrobot-v1 --init_summarizer acrobot_init_translator --curr_summarizer acrobot_basic_translator --decider naive_actor --prompt_level 2 --num_trails 1 --distiller traj_distiller --prompt_path "envs/classic_control/few_shot_examples/acrobot"
python main_reflexion.py --env_name Acrobot-v1 --init_summarizer acrobot_init_translator --curr_summarizer acrobot_basic_translator --decider naive_actor --prompt_level 3 --num_trails 5 --distiller traj_distiller --use_short_mem 0
python main_reflexion.py --env_name Acrobot-v1 --init_summarizer acrobot_init_translator --curr_summarizer acrobot_basic_translator --decider naive_actor --prompt_level 4 --num_trails 1 --distiller traj_distiller --prompt_path "envs/classic_control/few_shot_examples/acrobot"
python main_reflexion.py --env_name Acrobot-v1 --init_summarizer acrobot_init_translator --curr_summarizer acrobot_basic_translator --decider naive_actor --prompt_level 5 --num_trails 1

# CartPole-v0
# Naive Actor
python main_reflexion.py --env_name CartPole-v0 --init_summarizer cart_init_translator --curr_summarizer cart_basic_translator --decider naive_actor --prompt_level 1 --num_trails 1 --seed 0
python main_reflexion.py --env_name CartPole-v0 --init_summarizer cart_init_translator --curr_summarizer cart_basic_translator --decider naive_actor --prompt_level 2 --num_trails 1 --distiller traj_distiller --prompt_path "envs/classic_control/few_shot_examples/cartpole" --seed 0
python main_reflexion.py --env_name CartPole-v0 --init_summarizer cart_init_translator --curr_summarizer cart_basic_translator --decider naive_actor --prompt_level 3 --num_trails 5 --distiller traj_distiller --use_short_mem 0 --seed 0
python main_reflexion.py --env_name CartPole-v0 --init_summarizer cart_init_translator --curr_summarizer cart_basic_translator --decider naive_actor --prompt_level 4 --num_trails 1 --distiller traj_distiller --prompt_path "envs/classic_control/few_shot_examples/cartpole" --seed 0
python main_reflexion.py --env_name CartPole-v0 --init_summarizer cart_init_translator --curr_summarizer cart_basic_translator --decider naive_actor --prompt_level 5 --num_trails 1 --seed 0

# CliffWalking-v0
# Naive Actor
python main_reflexion.py --env_name CliffWalking-v0 --init_summarizer cliffwalking_init_translator --curr_summarizer cliffwalking_basic_translator --decider naive_actor --prompt_level 1 --num_trails 1
python main_reflexion.py --env_name CliffWalking-v0 --init_summarizer cliffwalking_init_translator --curr_summarizer cliffwalking_basic_translator --decider naive_actor --prompt_level 2 --num_trails 1 --distiller traj_distiller --prompt_path "envs/toy_text/few_shot_examples/cliffwalking"
python main_reflexion.py --env_name CliffWalking-v0 --init_summarizer cliffwalking_init_translator --curr_summarizer cliffwalking_basic_translator --decider naive_actor --prompt_level 3 --num_trails 5 --distiller traj_distiller --use_short_mem 0
python main_reflexion.py --env_name CliffWalking-v0 --init_summarizer cliffwalking_init_translator --curr_summarizer cliffwalking_basic_translator --decider naive_actor --prompt_level 4 --num_trails 1 --distiller traj_distiller --prompt_path "envs/toy_text/few_shot_examples/cliffwalking"
python main_reflexion.py --env_name CliffWalking-v0 --init_summarizer cliffwalking_init_translator --curr_summarizer cliffwalking_basic_translator --decider naive_actor --prompt_level 5 --num_trails 1

# FrozenLake-v1
# Naive Actor
python main_reflexion.py --env_name FrozenLake-v1 --init_summarizer frozenlake_init_translator --curr_summarizer frozenlake_basic_translator --decider naive_actor --prompt_level 1 --num_trails 1
python main_reflexion.py --env_name FrozenLake-v1 --init_summarizer frozenlake_init_translator --curr_summarizer frozenlake_basic_translator --decider naive_actor --prompt_level 2 --num_trails 1 --distiller traj_distiller --prompt_path "envs/toy_text/few_shot_examples/frozenlake"
python main_reflexion.py --env_name FrozenLake-v1 --init_summarizer frozenlake_init_translator --curr_summarizer frozenlake_basic_translator --decider naive_actor --prompt_level 3 --num_trails 5 --distiller traj_distiller --use_short_mem 0
python main_reflexion.py --env_name FrozenLake-v1 --init_summarizer frozenlake_init_translator --curr_summarizer frozenlake_basic_translator --decider naive_actor --prompt_level 4 --num_trails 1 --distiller traj_distiller --prompt_path "envs/toy_text/few_shot_examples/frozenlake"
python main_reflexion.py --env_name FrozenLake-v1 --init_summarizer frozenlake_init_translator --curr_summarizer frozenlake_basic_translator --decider naive_actor --prompt_level 5 --num_trails 1

# MountainCar-v0
# Naive Actor
python main_reflexion.py --env_name MountainCar-v0 --init_summarizer mountaincar_init_translator --curr_summarizer mountaincar_basic_translator --decider naive_actor --prompt_level 1 --num_trails 1
python main_reflexion.py --env_name MountainCar-v0 --init_summarizer mountaincar_init_translator --curr_summarizer mountaincar_basic_translator --decider naive_actor --prompt_level 2 --num_trails 1 --distiller traj_distiller --prompt_path "envs/classic_control/few_shot_examples/mountaincar"
python main_reflexion.py --env_name MountainCar-v0 --init_summarizer mountaincar_init_translator --curr_summarizer mountaincar_basic_translator --decider naive_actor --prompt_level 3 --num_trails 5 --distiller traj_distiller --use_short_mem 0
python main_reflexion.py --env_name MountainCar-v0 --init_summarizer mountaincar_init_translator --curr_summarizer mountaincar_basic_translator --decider naive_actor --prompt_level 4 --num_trails 1 --distiller traj_distiller --prompt_path "envs/classic_control/few_shot_examples/mountaincar"
python main_reflexion.py --env_name MountainCar-v0 --init_summarizer mountaincar_init_translator --curr_summarizer mountaincar_basic_translator --decider naive_actor --prompt_level 5 --num_trails 1

# Taxi-v3
# Naive Actor
python main_reflexion.py --env_name Taxi-v3 --init_summarizer taxi_init_translator --curr_summarizer taxi_basic_translator --decider naive_actor --prompt_level 1 --num_trails 1
python main_reflexion.py --env_name Taxi-v3 --init_summarizer taxi_init_translator --curr_summarizer taxi_basic_translator --decider naive_actor --prompt_level 2 --num_trails 1 --distiller traj_distiller --prompt_path "envs/toy_text/few_shot_examples/taxi"
python main_reflexion.py --env_name Taxi-v3 --init_summarizer taxi_init_translator --curr_summarizer taxi_basic_translator --decider naive_actor --prompt_level 3 --num_trails 5 --distiller traj_distiller --use_short_mem 0
python main_reflexion.py --env_name Taxi-v3 --init_summarizer taxi_init_translator --curr_summarizer taxi_basic_translator --decider naive_actor --prompt_level 4 --num_trails 1 --distiller traj_distiller --prompt_path "envs/toy_text/few_shot_examples/taxi"
python main_reflexion.py --env_name Taxi-v3 --init_summarizer taxi_init_translator --curr_summarizer taxi_basic_translator --decider naive_actor --prompt_level 5 --num_trails 1
