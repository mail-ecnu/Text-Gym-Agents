# Acrobot-v1
python main_reflexion.py --env_name Acrobot-v1 --init_summarizer acrobot_init_translator --curr_summarizer acrobot_basic_translator --decider jarvis_actor_wosh --prompt_level 1 --num_trails 1 --distiller guide_generator
python main_reflexion.py --env_name Acrobot-v1 --init_summarizer acrobot_init_translator --curr_summarizer acrobot_basic_translator --decider jarvis_actor_wosh --prompt_level 2 --num_trails 1 --distiller guide_generator --prompt_path "envs/classic_control/few_shot_examples/acrobot"
python main_reflexion.py --env_name Acrobot-v1 --init_summarizer acrobot_init_translator --curr_summarizer acrobot_basic_translator --decider jarvis_actor_wosh --prompt_level 3 --num_trails 3 --distiller guide_generator
python main_reflexion.py --env_name Acrobot-v1 --init_summarizer acrobot_init_translator --curr_summarizer acrobot_basic_translator --decider jarvis_actor_wosh --prompt_level 4 --num_trails 1 --distiller guide_generator --prompt_path "envs/classic_control/few_shot_examples/acrobot"
python main_reflexion.py --env_name Acrobot-v1 --init_summarizer acrobot_init_translator --curr_summarizer acrobot_basic_translator --decider jarvis_actor_wosh --prompt_level 5 --num_trails 1 --distiller guide_generator

# Blackjack-v1
python main_reflexion.py --env_name Blackjack-v1 --init_summarizer blackjack_init_translator --curr_summarizer blackjack_basic_translator --decider jarvis_actor_wosh --prompt_level 1 --num_trails 50 --distiller guide_generator
python main_reflexion.py --env_name Blackjack-v1 --init_summarizer blackjack_init_translator --curr_summarizer blackjack_basic_translator --decider jarvis_actor_wosh --prompt_level 2 --num_trails 50 --distiller guide_generator --prompt_path "envs/toy_text/few_shot_examples/blackjack"
python main_reflexion.py --env_name Blackjack-v1 --init_summarizer blackjack_init_translator --curr_summarizer blackjack_basic_translator --decider jarvis_actor_wosh --prompt_level 3 --num_trails 50 --distiller guide_generator
python main_reflexion.py --env_name Blackjack-v1 --init_summarizer blackjack_init_translator --curr_summarizer blackjack_basic_translator --decider jarvis_actor_wosh --prompt_level 4 --num_trails 50 --distiller guide_generator --prompt_path "envs/toy_text/few_shot_examples/blackjack"
python main_reflexion.py --env_name Blackjack-v1 --init_summarizer blackjack_init_translator --curr_summarizer blackjack_basic_translator --decider jarvis_actor_wosh --prompt_level 5 --num_trails 50 --distiller guide_generator

# CartPole-v0
python main_reflexion.py --env_name CartPole-v0 --init_summarizer cart_init_translator --curr_summarizer cart_basic_translator --decider jarvis_actor_wosh --prompt_level 1 --num_trails 1 --distiller guide_generator --seed 0
python main_reflexion.py --env_name CartPole-v0 --init_summarizer cart_init_translator --curr_summarizer cart_basic_translator --decider jarvis_actor_wosh --prompt_level 2 --num_trails 1 --distiller guide_generator --prompt_path "envs/classic_control/few_shot_examples/cartpole" --seed 0
python main_reflexion.py --env_name CartPole-v0 --init_summarizer cart_init_translator --curr_summarizer cart_basic_translator --decider jarvis_actor_wosh --prompt_level 3 --num_trails 3 --distiller guide_generator --seed 0
python main_reflexion.py --env_name CartPole-v0 --init_summarizer cart_init_translator --curr_summarizer cart_basic_translator --decider jarvis_actor_wosh --prompt_level 4 --num_trails 1 --distiller guide_generator --prompt_path "envs/classic_control/few_shot_examples/cartpole" --seed 0
python main_reflexion.py --env_name CartPole-v0 --init_summarizer cart_init_translator --curr_summarizer cart_basic_translator --decider jarvis_actor_wosh --prompt_level 5 --num_trails 1 --distiller guide_generator --seed 0

# CliffWalking-v0
python main_reflexion.py --env_name CliffWalking-v0 --init_summarizer cliffwalking_init_translator --curr_summarizer cliffwalking_basic_translator --decider jarvis_actor_wosh --prompt_level 1 --num_trails 1 --distiller guide_generator
python main_reflexion.py --env_name CliffWalking-v0 --init_summarizer cliffwalking_init_translator --curr_summarizer cliffwalking_basic_translator --decider jarvis_actor_wosh --prompt_level 2 --num_trails 1 --distiller guide_generator --prompt_path "envs/toy_text/few_shot_examples/cliffwalking"
python main_reflexion.py --env_name CliffWalking-v0 --init_summarizer cliffwalking_init_translator --curr_summarizer cliffwalking_basic_translator --decider jarvis_actor_wosh --prompt_level 3 --num_trails 3 --distiller guide_generator
python main_reflexion.py --env_name CliffWalking-v0 --init_summarizer cliffwalking_init_translator --curr_summarizer cliffwalking_basic_translator --decider jarvis_actor_wosh --prompt_level 4 --num_trails 1 --distiller guide_generator --prompt_path "envs/toy_text/few_shot_examples/cliffwalking"
python main_reflexion.py --env_name CliffWalking-v0 --init_summarizer cliffwalking_init_translator --curr_summarizer cliffwalking_basic_translator --decider jarvis_actor_wosh --prompt_level 5 --num_trails 1 --distiller guide_generator

# LunarLander-v2
python main_reflexion.py --env_name LunarLander-v2 --init_summarizer lunarLander_init_translator --curr_summarizer lunarLander_basic_translator --seed 0  --decider jarvis_actor_wosh --prompt_level 1 --num_trails 1 --distiller guide_generator --seed 0
python main_reflexion.py --env_name LunarLander-v2 --init_summarizer lunarLander_init_translator --curr_summarizer lunarLander_basic_translator --seed 0  --decider jarvis_actor_wosh --prompt_level 2 --num_trails 1 --distiller guide_generator --prompt_path "envs/box2d/few_shot_examples/lunarlander" --seed 0
python main_reflexion.py --env_name LunarLander-v2 --init_summarizer lunarLander_init_translator --curr_summarizer lunarLander_basic_translator --seed 0  --decider jarvis_actor_wosh --prompt_level 3 --num_trails 3 --distiller guide_generator --seed 0
python main_reflexion.py --env_name LunarLander-v2 --init_summarizer lunarLander_init_translator --curr_summarizer lunarLander_basic_translator --seed 0  --decider jarvis_actor_wosh --prompt_level 4 --num_trails 1 --distiller guide_generator --prompt_path "envs/box2d/few_shot_examples/lunarlander" --seed 0
python main_reflexion.py --env_name LunarLander-v2 --init_summarizer lunarLander_init_translator --curr_summarizer lunarLander_basic_translator --seed 0  --decider jarvis_actor_wosh --prompt_level 5 --num_trails 1 --distiller guide_generator --seed 0

# MountainCar-v0
python main_reflexion.py --env_name MountainCar-v0 --init_summarizer mountaincar_init_translator --curr_summarizer mountaincar_basic_translator --decider jarvis_actor_wosh --prompt_level 1 --num_trails 1 --distiller guide_generator
python main_reflexion.py --env_name MountainCar-v0 --init_summarizer mountaincar_init_translator --curr_summarizer mountaincar_basic_translator --decider jarvis_actor_wosh --prompt_level 2 --num_trails 1 --distiller guide_generator --prompt_path "envs/classic_control/few_shot_examples/mountaincar"
python main_reflexion.py --env_name MountainCar-v0 --init_summarizer mountaincar_init_translator --curr_summarizer mountaincar_basic_translator --decider jarvis_actor_wosh --prompt_level 3 --num_trails 3 --distiller guide_generator
python main_reflexion.py --env_name MountainCar-v0 --init_summarizer mountaincar_init_translator --curr_summarizer mountaincar_basic_translator --decider jarvis_actor_wosh --prompt_level 4 --num_trails 1 --distiller guide_generator --prompt_path "envs/classic_control/few_shot_examples/mountaincar"
python main_reflexion.py --env_name MountainCar-v0 --init_summarizer mountaincar_init_translator --curr_summarizer mountaincar_basic_translator --decider jarvis_actor_wosh --prompt_level 5 --num_trails 1 --distiller guide_generator

# MountainCarContinuous-v0
python main_reflexion.py --env_name MountainCarContinuous-v0 --init_summarizer mountaincarContinuous_init_translator --curr_summarizer mountaincarContinuous_basic_translator --decider jarvis_actor_wosh --prompt_level 1 --num_trails 1 --distiller guide_generator
python main_reflexion.py --env_name MountainCarContinuous-v0 --init_summarizer mountaincarContinuous_init_translator --curr_summarizer mountaincarContinuous_basic_translator --decider jarvis_actor_wosh --prompt_level 2 --num_trails 1 --distiller guide_generator --prompt_path "envs/classic_control/few_shot_examples/mountaincarContinuous"
python main_reflexion.py --env_name MountainCarContinuous-v0 --init_summarizer mountaincarContinuous_init_translator --curr_summarizer mountaincarContinuous_basic_translator --decider jarvis_actor_wosh --prompt_level 3 --num_trails 3 --distiller guide_generator
python main_reflexion.py --env_name MountainCarContinuous-v0 --init_summarizer mountaincarContinuous_init_translator --curr_summarizer mountaincarContinuous_basic_translator --decider jarvis_actor_wosh --prompt_level 4 --num_trails 1 --distiller guide_generator --prompt_path "envs/classic_control/few_shot_examples/mountaincarContinuous"
python main_reflexion.py --env_name MountainCarContinuous-v0 --init_summarizer mountaincarContinuous_init_translator --curr_summarizer mountaincarContinuous_basic_translator --decider jarvis_actor_wosh --prompt_level 5 --num_trails 1 --distiller guide_generator

# Taxi-v3
python main_reflexion.py --env_name Taxi-v3 --init_summarizer taxi_init_translator --curr_summarizer taxi_basic_translator --decider jarvis_actor_wosh --prompt_level 1 --num_trails 1 --distiller guide_generator
python main_reflexion.py --env_name Taxi-v3 --init_summarizer taxi_init_translator --curr_summarizer taxi_basic_translator --decider jarvis_actor_wosh --prompt_level 2 --num_trails 1 --distiller guide_generator --prompt_path "envs/toy_text/few_shot_examples/taxi"
python main_reflexion.py --env_name Taxi-v3 --init_summarizer taxi_init_translator --curr_summarizer taxi_basic_translator --decider jarvis_actor_wosh --prompt_level 3 --num_trails 3 --distiller guide_generator
python main_reflexion.py --env_name Taxi-v3 --init_summarizer taxi_init_translator --curr_summarizer taxi_basic_translator --decider jarvis_actor_wosh --prompt_level 4 --num_trails 1 --distiller guide_generator --prompt_path "envs/toy_text/few_shot_examples/taxi"
python main_reflexion.py --env_name Taxi-v3 --init_summarizer taxi_init_translator --curr_summarizer taxi_basic_translator --decider jarvis_actor_wosh --prompt_level 5 --num_trails 1 --distiller guide_generator