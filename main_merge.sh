# L1: --prompt_level 1; L2: --prompt_level 2 --distiller traj_distiller; L4: --prompt_level 4 --distiller traj_distiller; L5: --prompt_level 5
# Use History: --use_short_mem 1 or --use_short_mem 0 (default)
# prompt_level default: 1

# CartPole-v0
# L1
# Naive Actor
python main_merge.py --env_name CartPole-v0 --init_summarizer cart_init_translator --curr_summarizer cart_basic_translator --decider naive_actor --seed 0 
# PAL
python main_merge.py --env_name CartPole-v0 --init_summarizer cart_init_translator --curr_summarizer cart_basic_translator --decider pal_actor --seed 0 
# COT
python main_merge.py --env_name CartPole-v0 --init_summarizer cart_init_translator --curr_summarizer cart_basic_translator --decider cot_actor --seed 0 
# self consistency
python main_merge.py --env_name CartPole-v0 --init_summarizer cart_init_translator --curr_summarizer cart_basic_translator --decider self_consistency_actor --seed 0 
# self-ask
python main_merge.py --env_name CartPole-v0 --init_summarizer cart_init_translator --curr_summarizer cart_basic_translator --decider selfask_actor --seed 0 
# SPP
python main_merge.py --env_name CartPole-v0 --init_summarizer cart_init_translator --curr_summarizer cart_basic_translator --decider spp_actor --seed 0 

# LunarLander-v2
# L1
# Naive Actor
python main_merge.py --env_name LunarLander-v2 --init_summarizer lunarLander_init_translator --curr_summarizer lunarLander_basic_translator --decider naive_actor --seed 0 
# PAL
python main_merge.py --env_name LunarLander-v2 --init_summarizer lunarLander_init_translator --curr_summarizer lunarLander_basic_translator --decider pal_actor --seed 0 
# COT
python main_merge.py --env_name LunarLander-v2 --init_summarizer lunarLander_init_translator --curr_summarizer lunarLander_basic_translator --decider cot_actor --seed 0 
# self consistency
python main_merge.py --env_name LunarLander-v2 --init_summarizer lunarLander_init_translator --curr_summarizer lunarLander_basic_translator --decider self_consistency_actor --seed 0 
# self-ask
python main_merge.py --env_name LunarLander-v2 --init_summarizer lunarLander_init_translator --curr_summarizer lunarLander_basic_translator --decider selfask_actor --seed 0 
# SPP
python main_merge.py --env_name LunarLander-v2 --init_summarizer lunarLander_init_translator --curr_summarizer lunarLander_basic_translator --decider spp_actor --prompt_level 1 --seed 0 

# Acrobot-v1
# L1
# Naive Actor
# python main_merge.py --env_name Acrobot-v1 --init_summarizer acrobot_init_translator --curr_summarizer acrobot_basic_translator --decider naive_actor --prompt_level 1 
# # PAL
# python main_merge.py --env_name Acrobot-v1 --init_summarizer acrobot_init_translator --curr_summarizer acrobot_basic_translator --decider pal_actor --prompt_level 1
# # COT
# python main_merge.py --env_name Acrobot-v1 --init_summarizer acrobot_init_translator --curr_summarizer acrobot_basic_translator --decider cot_actor --prompt_level 1
# # self consistency
# python main_merge.py --env_name Acrobot-v1 --init_summarizer acrobot_init_translator --curr_summarizer acrobot_basic_translator --decider self_consistency_actor --prompt_level 1
# # self-ask
# python main_merge.py --env_name Acrobot-v1 --init_summarizer acrobot_init_translator --curr_summarizer acrobot_basic_translator --decider selfask_actor --prompt_level 1
# # SPP
# python main_merge.py --env_name Acrobot-v1 --init_summarizer acrobot_init_translator --curr_summarizer acrobot_basic_translator --decider spp_actor --prompt_level 1

# MountainCar-v0
# L1
# Naive Actor
# python main_merge.py --env_name MountainCar-v0 --init_summarizer mountaincar_init_translator --curr_summarizer mountaincar_basic_translator --decider naive_actor --prompt_level 1 
# # PAL
# python main_merge.py --env_name MountainCar-v0 --init_summarizer mountaincar_init_translator --curr_summarizer mountaincar_basic_translator --decider pal_actor --prompt_level 1
# # COT
# python main_merge.py --env_name MountainCar-v0 --init_summarizer mountaincar_init_translator --curr_summarizer mountaincar_basic_translator --decider cot_actor --prompt_level 1
# # self consistency
# python main_merge.py --env_name MountainCar-v0 --init_summarizer mountaincar_init_translator --curr_summarizer mountaincar_basic_translator --decider self_consistency_actor --prompt_level 1
# # self-ask
# python main_merge.py --env_name MountainCar-v0 --init_summarizer mountaincar_init_translator --curr_summarizer mountaincar_basic_translator --decider selfask_actor --prompt_level 1
# # SPP
# python main_merge.py --env_name MountainCar-v0 --init_summarizer mountaincar_init_translator --curr_summarizer mountaincar_basic_translator --decider spp_actor --prompt_level 1

# Blackjack-v1
# L1
# Naive Actor
python main_merge.py --env_name Blackjack-v1 --init_summarizer blackjack_init_translator --curr_summarizer blackjack_basic_translator --decider naive_actor --prompt_level 1 --seed 0 
# PAL
python main_merge.py --env_name Blackjack-v1 --init_summarizer blackjack_init_translator --curr_summarizer blackjack_basic_translator --decider pal_actor --prompt_level 1 --seed 0 
# COT
python main_merge.py --env_name Blackjack-v1 --init_summarizer blackjack_init_translator --curr_summarizer blackjack_basic_translator --decider cot_actor --prompt_level 1 --seed 0 
# self consistency
python main_merge.py --env_name Blackjack-v1 --init_summarizer blackjack_init_translator --curr_summarizer blackjack_basic_translator --decider self_consistency_actor --prompt_level 1 --seed 0 
# self-ask
python main_merge.py --env_name Blackjack-v1 --init_summarizer blackjack_init_translator --curr_summarizer blackjack_basic_translator --decider selfask_actor --prompt_level 1 --seed 0 
# SPP
python main_merge.py --env_name Blackjack-v1 --init_summarizer blackjack_init_translator --curr_summarizer blackjack_basic_translator --decider spp_actor --prompt_level 1 --seed 0 

# Taxi-v3
# L1
# Naive Actor
# python main_merge.py --env_name Taxi-v3 --init_summarizer taxi_init_translator --curr_summarizer taxi_basic_translator --decider naive_actor --prompt_level 1
# # PAL
# python main_merge.py --env_name Taxi-v3 --init_summarizer taxi_init_translator --curr_summarizer taxi_basic_translator --decider pal_actor --prompt_level 1
# # COT
# python main_merge.py --env_name Taxi-v3 --init_summarizer taxi_init_translator --curr_summarizer taxi_basic_translator --decider cot_actor --prompt_level 1
# # self consistency
# python main_merge.py --env_name Taxi-v3 --init_summarizer taxi_init_translator --curr_summarizer taxi_basic_translator --decider self_consistency_actor --prompt_level 1
# # self-ask
# python main_merge.py --env_name Taxi-v3 --init_summarizer taxi_init_translator --curr_summarizer taxi_basic_translator --decider selfask_actor --prompt_level 1
# # SPP
# python main_merge.py --env_name Taxi-v3 --init_summarizer taxi_init_translator --curr_summarizer taxi_basic_translator --decider spp_actor --prompt_level 1

# CliffWalking-v0
# L1
# Naive Actor
# python main_merge.py --env_name CliffWalking-v0 --init_summarizer cliffwalking_init_translator --curr_summarizer cliffwalking_basic_translator --decider naive_actor --prompt_level 1
# # PAL
# python main_merge.py --env_name CliffWalking-v0 --init_summarizer cliffwalking_init_translator --curr_summarizer cliffwalking_basic_translator --decider pal_actor --prompt_level 1
# # COT
# python main_merge.py --env_name CliffWalking-v0 --init_summarizer cliffwalking_init_translator --curr_summarizer cliffwalking_basic_translator --decider cot_actor --prompt_level 1
# # self consistency
# python main_merge.py --env_name CliffWalking-v0 --init_summarizer cliffwalking_init_translator --curr_summarizer cliffwalking_basic_translator --decider self_consistency_actor --prompt_level 1
# # self-ask
# python main_merge.py --env_name CliffWalking-v0 --init_summarizer cliffwalking_init_translator --curr_summarizer cliffwalking_basic_translator --decider selfask_actor --prompt_level 1
# # SPP
# python main_merge.py --env_name CliffWalking-v0 --init_summarizer cliffwalking_init_translator --curr_summarizer cliffwalking_basic_translator --decider spp_actor --prompt_level 1

# FrozenLake-v1
# L1
# Naive Actor
python main_merge.py --env_name FrozenLake-v1 --init_summarizer frozenlake_init_translator --curr_summarizer frozenlake_basic_translator --decider naive_actor --prompt_level 1 --seed 0 
# PAL
python main_merge.py --env_name FrozenLake-v1 --init_summarizer frozenlake_init_translator --curr_summarizer frozenlake_basic_translator --decider pal_actor --prompt_level 1 --seed 0 
# COT
python main_merge.py --env_name FrozenLake-v1 --init_summarizer frozenlake_init_translator --curr_summarizer frozenlake_basic_translator --decider cot_actor --prompt_level 1 --seed 0 
# self consistency
python main_merge.py --env_name FrozenLake-v1 --init_summarizer frozenlake_init_translator --curr_summarizer frozenlake_basic_translator --decider self_consistency_actor --prompt_level 1 --seed 0 
# self-ask
python main_merge.py --env_name FrozenLake-v1 --init_summarizer frozenlake_init_translator --curr_summarizer frozenlake_basic_translator --decider selfask_actor --prompt_level 1 --seed 0 
# SPP
python main_merge.py --env_name FrozenLake-v1 --init_summarizer frozenlake_init_translator --curr_summarizer frozenlake_basic_translator --decider spp_actor --prompt_level 1 --seed 0 