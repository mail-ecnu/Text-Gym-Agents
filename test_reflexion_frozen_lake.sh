# Blackjack-v1
# L1
python main_reflexion.py --env_name Blackjack-v1 --init_summarizer blackjack_init_translator --curr_summarizer blackjack_basic_translator --decider jarvis_actor --prompt_level 3 --distiller guide_generator --num_trails 5 --seed 1 
python main_reflexion.py --env_name Blackjack-v1 --init_summarizer blackjack_init_translator --curr_summarizer blackjack_basic_translator --decider reflexion_actor --prompt_level 3 --distiller reflect_distiller --num_trails 5 --seed 1
# Naive Actor
python main_reflexion.py --env_name Blackjack-v1 --init_summarizer blackjack_init_translator --curr_summarizer blackjack_basic_translator --decider naive_actor --prompt_level 3 --num_trails 5 --seed 1 
# PAL
python main_reflexion.py --env_name Blackjack-v1 --init_summarizer blackjack_init_translator --curr_summarizer blackjack_basic_translator --decider pal_actor  --prompt_level 3 --num_trails 5 --seed 1 
# COT
python main_reflexion.py --env_name Blackjack-v1 --init_summarizer blackjack_init_translator --curr_summarizer blackjack_basic_translator --decider cot_actor --prompt_level 3 --num_trails 5 --seed 1 
# self consistency
python main_reflexion.py --env_name Blackjack-v1 --init_summarizer blackjack_init_translator --curr_summarizer blackjack_basic_translator --decider self_consistency_actor --prompt_level 3 --num_trails 5 --seed 1 
# self-ask
python main_reflexion.py --env_name Blackjack-v1 --init_summarizer blackjack_init_translator --curr_summarizer blackjack_basic_translator --decider selfask_actor --prompt_level 3 --num_trails 5 --seed 1 
# SPP
python main_reflexion.py --env_name Blackjack-v1 --init_summarizer blackjack_init_translator --curr_summarizer blackjack_basic_translator --decider spp_actor --prompt_level 3 --num_trails 5 --seed 1 

# L1
python main_reflexion.py --env_name Blackjack-v1 --init_summarizer blackjack_init_translator --curr_summarizer blackjack_basic_translator --decider jarvis_actor --prompt_level 3 --distiller guide_generator --num_trails 5 --seed 1 
python main_reflexion.py --env_name Blackjack-v1 --init_summarizer blackjack_init_translator --curr_summarizer blackjack_basic_translator --decider reflexion_actor --prompt_level 3 --distiller reflect_distiller --num_trails 5 --seed 2
# Naive Actor
python main_reflexion.py --env_name Blackjack-v1 --init_summarizer blackjack_init_translator --curr_summarizer blackjack_basic_translator --decider naive_actor --prompt_level 3 --num_trails 5 --seed 1
# PAL
python main_reflexion.py --env_name Blackjack-v1 --init_summarizer blackjack_init_translator --curr_summarizer blackjack_basic_translator --decider pal_actor  --prompt_level 3 --num_trails 5 --seed 1 
# COT
python main_reflexion.py --env_name Blackjack-v1 --init_summarizer blackjack_init_translator --curr_summarizer blackjack_basic_translator --decider cot_actor --prompt_level 3 --num_trails 5 --seed 1
# self consistency
python main_reflexion.py --env_name Blackjack-v1 --init_summarizer blackjack_init_translator --curr_summarizer blackjack_basic_translator --decider self_consistency_actor --prompt_level 3 --num_trails 5 --seed 1
# self-ask
python main_reflexion.py --env_name Blackjack-v1 --init_summarizer blackjack_init_translator --curr_summarizer blackjack_basic_translator --decider selfask_actor --prompt_level 3 --num_trails 5 --seed 1
# SPP
python main_reflexion.py --env_name Blackjack-v1 --init_summarizer blackjack_init_translator --curr_summarizer blackjack_basic_translator --decider spp_actor --prompt_level 3 --num_trails 5 --seed 1

# L1
python main_reflexion.py --env_name Blackjack-v1 --init_summarizer blackjack_init_translator --curr_summarizer blackjack_basic_translator --decider jarvis_actor --prompt_level 3 --distiller guide_generator --num_trails 5 --seed 2 
python main_reflexion.py --env_name Blackjack-v1 --init_summarizer blackjack_init_translator --curr_summarizer blackjack_basic_translator --decider reflexion_actor --prompt_level 3 --distiller reflect_distiller --num_trails 5 --seed 2
# Naive Actor
python main_reflexion.py --env_name Blackjack-v1 --init_summarizer blackjack_init_translator --curr_summarizer blackjack_basic_translator --decider naive_actor --prompt_level 3 --num_trails 5 --seed 2 
# PAL
python main_reflexion.py --env_name Blackjack-v1 --init_summarizer blackjack_init_translator --curr_summarizer blackjack_basic_translator --decider pal_actor  --prompt_level 3 --num_trails 5 --seed 2 
# COT
python main_reflexion.py --env_name Blackjack-v1 --init_summarizer blackjack_init_translator --curr_summarizer blackjack_basic_translator --decider cot_actor --prompt_level 3 --num_trails 5 --seed 2 
# self consistency
python main_reflexion.py --env_name Blackjack-v1 --init_summarizer blackjack_init_translator --curr_summarizer blackjack_basic_translator --decider self_consistency_actor --prompt_level 3 --num_trails 5 --seed 2
# self-ask
python main_reflexion.py --env_name Blackjack-v1 --init_summarizer blackjack_init_translator --curr_summarizer blackjack_basic_translator --decider selfask_actor --prompt_level 3 --num_trails 5 --seed 2 
# SPP
python main_reflexion.py --env_name Blackjack-v1 --init_summarizer blackjack_init_translator --curr_summarizer blackjack_basic_translator --decider spp_actor --prompt_level 3 --num_trails 5 --seed 2
# Taxi-v3
# L1
# Naive Actor
# python main_reflexion.py --env_name Taxi-v3 --init_summarizer taxi_init_translator --curr_summarizer taxi_basic_translator --decider naive_actor
# # PAL
# python main_reflexion.py --env_name Taxi-v3 --init_summarizer taxi_init_translator --curr_summarizer taxi_basic_translator --decider pal_actor
# # COT
# python main_reflexion.py --env_name Taxi-v3 --init_summarizer taxi_init_translator --curr_summarizer taxi_basic_translator --decider cot_actor
# # self consistency
# python main_reflexion.py --env_name Taxi-v3 --init_summarizer taxi_init_translator --curr_summarizer taxi_basic_translator --decider self_consistency_actor
# # self-ask
# python main_reflexion.py --env_name Taxi-v3 --init_summarizer taxi_init_translator --curr_summarizer taxi_basic_translator --decider selfask_actor
# # SPP
# python main_reflexion.py --env_name Taxi-v3 --init_summarizer taxi_init_translator --curr_summarizer taxi_basic_translator --decider spp_actor

# CliffWalking-v0
# L1
# Naive Actor
# python main_reflexion.py --env_name CliffWalking-v0 --init_summarizer cliffwalking_init_translator --curr_summarizer cliffwalking_basic_translator --decider naive_actor
# # PAL
# python main_reflexion.py --env_name CliffWalking-v0 --init_summarizer cliffwalking_init_translator --curr_summarizer cliffwalking_basic_translator --decider pal_actor
# # COT
# python main_reflexion.py --env_name CliffWalking-v0 --init_summarizer cliffwalking_init_translator --curr_summarizer cliffwalking_basic_translator --decider cot_actor
# # self consistency
# python main_reflexion.py --env_name CliffWalking-v0 --init_summarizer cliffwalking_init_translator --curr_summarizer cliffwalking_basic_translator --decider self_consistency_actor
# # self-ask
# python main_reflexion.py --env_name CliffWalking-v0 --init_summarizer cliffwalking_init_translator --curr_summarizer cliffwalking_basic_translator --decider selfask_actor
# # SPP
# python main_reflexion.py --env_name CliffWalking-v0 --init_summarizer cliffwalking_init_translator --curr_summarizer cliffwalking_basic_translator --decider spp_actor

# FrozenLake-v1
# L1
python main_reflexion.py --env_name FrozenLake-v1 --init_summarizer frozenlake_init_translator --curr_summarizer frozenlake_basic_translator --decider jarvis_actor --prompt_level 3 --distiller guide_generator --num_trails 5 --seed 0 
# python main_reflexion.py --env_name FrozenLake-v1 --init_summarizer frozenlake_init_translator --curr_summarizer frozenlake_basic_translator --decider reflexion_actor --prompt_level 3 --distiller reflect_distiller --num_trails 5 --seed 0
# Naive Actor
python main_reflexion.py --env_name FrozenLake-v1 --init_summarizer frozenlake_init_translator --curr_summarizer frozenlake_basic_translator --decider naive_actor --prompt_level 3 --num_trails 5 --seed 0 
# PAL
python main_reflexion.py --env_name FrozenLake-v1 --init_summarizer frozenlake_init_translator --curr_summarizer frozenlake_basic_translator --decider pal_actor --prompt_level 3 --num_trails 5 --seed 0 
# COT
python main_reflexion.py --env_name FrozenLake-v1 --init_summarizer frozenlake_init_translator --curr_summarizer frozenlake_basic_translator --decider cot_actor --prompt_level 3 --num_trails 5 --seed 0 
# self consistency
python main_reflexion.py --env_name FrozenLake-v1 --init_summarizer frozenlake_init_translator --curr_summarizer frozenlake_basic_translator --decider self_consistency_actor --prompt_level 3 --num_trails 5 --seed 0 
# self-ask
python main_reflexion.py --env_name FrozenLake-v1 --init_summarizer frozenlake_init_translator --curr_summarizer frozenlake_basic_translator --decider selfask_actor --prompt_level 3 --num_trails 5 --seed 0 
# SPP
python main_reflexion.py --env_name FrozenLake-v1 --init_summarizer frozenlake_init_translator --curr_summarizer frozenlake_basic_translator --decider spp_actor --prompt_level 3 --num_trails 5 --seed 0 

# CartPole-v0
# L3 

