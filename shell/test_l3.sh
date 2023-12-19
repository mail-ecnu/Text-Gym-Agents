#exe
python main_reflexion.py --env_name Taxi-v3 --init_summarizer taxi_init_translator --curr_summarizer taxi_basic_translator --decider exe_actor --prompt_level 3 --num_trails 5 --distiller guide_generator
python main_reflexion.py --env_name MountainCarContinuous-v0 --init_summarizer mountaincarContinuous_init_translator --curr_summarizer mountaincarContinuous_basic_translator --decider exe_actor --prompt_level 3 --num_trails 5 --distiller guide_generator
python main_reflexion.py --env_name MountainCar-v0 --init_summarizer mountaincar_init_translator --curr_summarizer mountaincar_basic_translator --decider exe_actor --prompt_level 3 --num_trails 5 --distiller guide_generator
python main_reflexion.py --env_name LunarLander-v2 --init_summarizer lunarLander_init_translator --curr_summarizer lunarLander_basic_translator --decider exe_actor --prompt_level 3 --num_trails 5 --distiller guide_generator
python main_reflexion.py --env_name CliffWalking-v0 --init_summarizer cliffwalking_init_translator --curr_summarizer cliffwalking_basic_translator --decider exe_actor --prompt_level 3 --num_trails 5 --distiller guide_generator
python main_reflexion.py --env_name CartPole-v0 --init_summarizer cart_init_translator --curr_summarizer cart_basic_translator --decider exe_actor --prompt_level 3 --num_trails 5 --distiller guide_generator
python main_reflexion.py --env_name Acrobot-v1 --init_summarizer acrobot_init_translator --curr_summarizer acrobot_basic_translator --decider exe_actor --prompt_level 3 --num_trails 5 --distiller guide_generator
python main_reflexion.py --env_name Blackjack-v1 --init_summarizer blackjack_init_translator --curr_summarizer blackjack_basic_translator --decider exe_actor --prompt_level 3 --num_trails 5 --distiller guide_generator

# exe trail 5
python main_reflexion.py --env_name Blackjack-v1 --init_summarizer blackjack_init_translator --curr_summarizer blackjack_basic_translator --decider exe_actor --prompt_level 3 --num_trails 5 --distiller guide_generator
python main_reflexion.py --env_name Taxi-v3 --init_summarizer taxi_init_translator --curr_summarizer taxi_basic_translator --decider exe_actor --prompt_level 3 --num_trails 5 --distiller guide_generator
python main_reflexion.py --env_name MountainCarContinuous-v0 --init_summarizer mountaincarContinuous_init_translator --curr_summarizer mountaincarContinuous_basic_translator --decider exe_actor --prompt_level 3 --num_trails 5 --distiller guide_generator
python main_reflexion.py --env_name MountainCar-v0 --init_summarizer mountaincar_init_translator --curr_summarizer mountaincar_basic_translator --decider exe_actor --prompt_level 3 --num_trails 5 --distiller guide_generator
python main_reflexion.py --env_name LunarLander-v2 --init_summarizer lunarLander_init_translator --curr_summarizer lunarLander_basic_translator --decider exe_actor --prompt_level 3 --num_trails 5 --distiller guide_generator
python main_reflexion.py --env_name CliffWalking-v0 --init_summarizer cliffwalking_init_translator --curr_summarizer cliffwalking_basic_translator --decider exe_actor --prompt_level 3 --num_trails 5 --distiller guide_generator
python main_reflexion.py --env_name CartPole-v0 --init_summarizer cart_init_translator --curr_summarizer cart_basic_translator --decider exe_actor --prompt_level 3 --num_trails 5 --distiller guide_generator
python main_reflexion.py --env_name Acrobot-v1 --init_summarizer acrobot_init_translator --curr_summarizer acrobot_basic_translator --decider exe_actor --prompt_level 3 --num_trails 5 --distiller guide_generator

# COT
python main_reflexion.py --env_name Taxi-v3 --init_summarizer taxi_init_translator --curr_summarizer taxi_basic_translator --decider cot_actor --prompt_level 3 --num_trails 5 --distiller traj_distiller 
python main_reflexion.py --env_name MountainCarContinuous-v0 --init_summarizer mountaincarContinuous_init_translator --curr_summarizer mountaincarContinuous_basic_translator --decider cot_actor --prompt_level 3 --num_trails 5 --distiller traj_distiller 
python main_reflexion.py --env_name MountainCar-v0 --init_summarizer mountaincar_init_translator --curr_summarizer mountaincar_basic_translator --decider cot_actor --prompt_level 3 --num_trails 5 --distiller traj_distiller 
python main_reflexion.py --env_name LunarLander-v2 --init_summarizer lunarLander_init_translator --curr_summarizer lunarLander_basic_translator --decider cot_actor --prompt_level 3 --num_trails 5 --distiller traj_distiller 
python main_reflexion.py --env_name CliffWalking-v0 --init_summarizer cliffwalking_init_translator --curr_summarizer cliffwalking_basic_translator --decider cot_actor --prompt_level 3 --num_trails 5 --distiller traj_distiller 
python main_reflexion.py --env_name CartPole-v0 --init_summarizer cart_init_translator --curr_summarizer cart_basic_translator --decider cot_actor --prompt_level 3 --num_trails 5 --distiller traj_distiller 
python main_reflexion.py --env_name Blackjack-v1 --init_summarizer blackjack_init_translator --curr_summarizer blackjack_basic_translator --decider cot_actor --prompt_level 3 --num_trails 5  --distiller traj_distiller
python main_reflexion.py --env_name Acrobot-v1 --init_summarizer acrobot_init_translator --curr_summarizer acrobot_basic_translator --decider cot_actor --prompt_level 3 --num_trails 5 --distiller traj_distiller 

# Reflexion
python main_reflexion.py --env_name Taxi-v3 --init_summarizer taxi_init_translator --curr_summarizer taxi_basic_translator --decider reflexion_actor --prompt_level 3 --num_trails 5 --distiller reflect_distiller
python main_reflexion.py --env_name MountainCarContinuous-v0 --init_summarizer mountaincarContinuous_init_translator --curr_summarizer mountaincarContinuous_basic_translator --decider reflexion_actor --prompt_level 3 --num_trails 5 --distiller reflect_distiller
python main_reflexion.py --env_name MountainCar-v0 --init_summarizer mountaincar_init_translator --curr_summarizer mountaincar_basic_translator --decider reflexion_actor --prompt_level 3 --num_trails 5 --distiller reflect_distiller
python main_reflexion.py --env_name LunarLander-v2 --init_summarizer lunarLander_init_translator --curr_summarizer lunarLander_basic_translator --decider reflexion_actor --prompt_level 3 --num_trails 5 --distiller reflect_distiller
python main_reflexion.py --env_name CliffWalking-v0 --init_summarizer cliffwalking_init_translator --curr_summarizer cliffwalking_basic_translator --decider reflexion_actor --prompt_level 3 --num_trails 5 --distiller reflect_distiller
python main_reflexion.py --env_name CartPole-v0 --init_summarizer cart_init_translator --curr_summarizer cart_basic_translator --decider reflexion_actor --prompt_level 3 --num_trails 5 --distiller reflect_distiller
python main_reflexion.py --env_name Blackjack-v1 --init_summarizer blackjack_init_translator --curr_summarizer blackjack_basic_translator --decider reflexion_actor --prompt_level 3 --num_trails 5 --distiller reflect_distiller
python main_reflexion.py --env_name Acrobot-v1 --init_summarizer acrobot_init_translator --curr_summarizer acrobot_basic_translator --decider reflexion_actor --prompt_level 3 --num_trails 5 --distiller reflect_distiller

# Naive Actor
python main_reflexion.py --env_name Taxi-v3 --init_summarizer taxi_init_translator --curr_summarizer taxi_basic_translator --decider naive_actor --prompt_level 3 --num_trails 5 --distiller traj_distiller 
python main_reflexion.py --env_name MountainCarContinuous-v0 --init_summarizer mountaincarContinuous_init_translator --curr_summarizer mountaincarContinuous_basic_translator --decider naive_actor --prompt_level 3 --num_trails 5 --distiller traj_distiller 
python main_reflexion.py --env_name MountainCar-v0 --init_summarizer mountaincar_init_translator --curr_summarizer mountaincar_basic_translator --decider naive_actor --prompt_level 3 --num_trails 5 --distiller traj_distiller 
python main_reflexion.py --env_name LunarLander-v2 --init_summarizer lunarLander_init_translator --curr_summarizer lunarLander_basic_translator --decider naive_actor --prompt_level 3 --num_trails 5 --distiller traj_distiller 
python main_reflexion.py --env_name CliffWalking-v0 --init_summarizer cliffwalking_init_translator --curr_summarizer cliffwalking_basic_translator --decider naive_actor --prompt_level 3 --num_trails 5 --distiller traj_distiller 
python main_reflexion.py --env_name CartPole-v0 --init_summarizer cart_init_translator --curr_summarizer cart_basic_translator --decider naive_actor --prompt_level 3 --num_trails 5 --distiller traj_distiller 
python main_reflexion.py --env_name Blackjack-v1 --init_summarizer blackjack_init_translator --curr_summarizer blackjack_basic_translator --decider naive_actor --prompt_level 3 --num_trails 5  --distiller traj_distiller
python main_reflexion.py --env_name Acrobot-v1 --init_summarizer acrobot_init_translator --curr_summarizer acrobot_basic_translator --decider naive_actor --prompt_level 3 --num_trails 5 --distiller traj_distiller 

# self consistency
python main_reflexion.py --env_name Acrobot-v1 --init_summarizer acrobot_init_translator --curr_summarizer acrobot_basic_translator --decider self_consistency_actor --prompt_level 3 --num_trails 5 --distiller traj_distiller 
python main_reflexion.py --env_name Blackjack-v1 --init_summarizer blackjack_init_translator --curr_summarizer blackjack_basic_translator --decider self_consistency_actor --prompt_level 3 --num_trails 5  --distiller traj_distiller
python main_reflexion.py --env_name CartPole-v0 --init_summarizer cart_init_translator --curr_summarizer cart_basic_translator --decider self_consistency_actor --prompt_level 3 --num_trails 5 --distiller traj_distiller 
python main_reflexion.py --env_name CliffWalking-v0 --init_summarizer cliffwalking_init_translator --curr_summarizer cliffwalking_basic_translator --decider self_consistency_actor --prompt_level 3 --num_trails 5 --distiller traj_distiller 
python main_reflexion.py --env_name MountainCar-v0 --init_summarizer mountaincar_init_translator --curr_summarizer mountaincar_basic_translator --decider self_consistency_actor --prompt_level 3 --num_trails 5 --distiller traj_distiller 
python main_reflexion.py --env_name MountainCarContinuous-v0 --init_summarizer mountaincarContinuous_init_translator --curr_summarizer mountaincarContinuous_basic_translator --decider self_consistency_actor --prompt_level 3 --num_trails 5 --distiller traj_distiller 
python main_reflexion.py --env_name Taxi-v3 --init_summarizer taxi_init_translator --curr_summarizer taxi_basic_translator --decider self_consistency_actor --prompt_level 3 --num_trails 5 --distiller traj_distiller 
python main_reflexion.py --env_name LunarLander-v2 --init_summarizer lunarLander_init_translator --curr_summarizer lunarLander_basic_translator --decider self_consistency_actor --prompt_level 3 --num_trails 5 --distiller traj_distiller 


# self-ask
python main_reflexion.py --env_name Acrobot-v1 --init_summarizer acrobot_init_translator --curr_summarizer acrobot_basic_translator --decider selfask_actor --prompt_level 3 --num_trails 5 --distiller traj_distiller 
python main_reflexion.py --env_name Blackjack-v1 --init_summarizer blackjack_init_translator --curr_summarizer blackjack_basic_translator --decider selfask_actor --prompt_level 3 --num_trails 5  --distiller traj_distiller
python main_reflexion.py --env_name CartPole-v0 --init_summarizer cart_init_translator --curr_summarizer cart_basic_translator --decider selfask_actor --prompt_level 3 --num_trails 5 --distiller traj_distiller 
python main_reflexion.py --env_name CliffWalking-v0 --init_summarizer cliffwalking_init_translator --curr_summarizer cliffwalking_basic_translator --decider selfask_actor --prompt_level 3 --num_trails 5 --distiller traj_distiller 
python main_reflexion.py --env_name LunarLander-v2 --init_summarizer lunarLander_init_translator --curr_summarizer lunarLander_basic_translator --decider selfask_actor --prompt_level 3 --num_trails 5 --distiller traj_distiller 
python main_reflexion.py --env_name MountainCar-v0 --init_summarizer mountaincar_init_translator --curr_summarizer mountaincar_basic_translator --decider selfask_actor --prompt_level 3 --num_trails 5 --distiller traj_distiller 
python main_reflexion.py --env_name MountainCarContinuous-v0 --init_summarizer mountaincarContinuous_init_translator --curr_summarizer mountaincarContinuous_basic_translator --decider selfask_actor --prompt_level 3 --num_trails 5 --distiller traj_distiller 
python main_reflexion.py --env_name Taxi-v3 --init_summarizer taxi_init_translator --curr_summarizer taxi_basic_translator --decider selfask_actor --prompt_level 3 --num_trails 5 --distiller traj_distiller 

# SPP
python main_reflexion.py --env_name Acrobot-v1 --init_summarizer acrobot_init_translator --curr_summarizer acrobot_basic_translator --decider spp_actor --prompt_level 3 --num_trails 5 --distiller traj_distiller 
python main_reflexion.py --env_name Blackjack-v1 --init_summarizer blackjack_init_translator --curr_summarizer blackjack_basic_translator --decider spp_actor --prompt_level 3 --num_trails 5  --distiller traj_distiller
python main_reflexion.py --env_name CartPole-v0 --init_summarizer cart_init_translator --curr_summarizer cart_basic_translator --decider spp_actor --prompt_level 3 --num_trails 5 --distiller traj_distiller 
python main_reflexion.py --env_name CliffWalking-v0 --init_summarizer cliffwalking_init_translator --curr_summarizer cliffwalking_basic_translator --decider spp_actor --prompt_level 3 --num_trails 5 --distiller traj_distiller 
python main_reflexion.py --env_name LunarLander-v2 --init_summarizer lunarLander_init_translator --curr_summarizer lunarLander_basic_translator --decider spp_actor --prompt_level 3 --num_trails 5 --distiller traj_distiller 
python main_reflexion.py --env_name MountainCar-v0 --init_summarizer mountaincar_init_translator --curr_summarizer mountaincar_basic_translator --decider spp_actor --prompt_level 3 --num_trails 5 --distiller traj_distiller 
python main_reflexion.py --env_name MountainCarContinuous-v0 --init_summarizer mountaincarContinuous_init_translator --curr_summarizer mountaincarContinuous_basic_translator --decider spp_actor --prompt_level 3 --num_trails 5 --distiller traj_distiller 
python main_reflexion.py --env_name Taxi-v3 --init_summarizer taxi_init_translator --curr_summarizer taxi_basic_translator --decider spp_actor --prompt_level 3 --num_trails 5 --distiller traj_distiller 

# PAL
python main_reflexion.py --env_name Acrobot-v1 --init_summarizer acrobot_init_translator --curr_summarizer acrobot_basic_translator --decider pal_actor --prompt_level 3 --num_trails 5 --distiller traj_distiller 
python main_reflexion.py --env_name Blackjack-v1 --init_summarizer blackjack_init_translator --curr_summarizer blackjack_basic_translator --decider pal_actor --prompt_level 3 --num_trails 5  --distiller traj_distiller
python main_reflexion.py --env_name CartPole-v0 --init_summarizer cart_init_translator --curr_summarizer cart_basic_translator --decider pal_actor --prompt_level 3 --num_trails 5 --distiller traj_distiller 
python main_reflexion.py --env_name CliffWalking-v0 --init_summarizer cliffwalking_init_translator --curr_summarizer cliffwalking_basic_translator --decider pal_actor --prompt_level 3 --num_trails 5 --distiller traj_distiller 
python main_reflexion.py --env_name LunarLander-v2 --init_summarizer lunarLander_init_translator --curr_summarizer lunarLander_basic_translator --decider pal_actor --prompt_level 3 --num_trails 5 --distiller traj_distiller 
python main_reflexion.py --env_name MountainCar-v0 --init_summarizer mountaincar_init_translator --curr_summarizer mountaincar_basic_translator --decider pal_actor --prompt_level 3 --num_trails 5 --distiller traj_distiller 
python main_reflexion.py --env_name MountainCarContinuous-v0 --init_summarizer mountaincarContinuous_init_translator --curr_summarizer mountaincarContinuous_basic_translator --decider pal_actor --prompt_level 3 --num_trails 5 --distiller traj_distiller 
python main_reflexion.py --env_name Taxi-v3 --init_summarizer taxi_init_translator --curr_summarizer taxi_basic_translator --decider pal_actor --prompt_level 3 --num_trails 5 --distiller traj_distiller 

# BlackJack
python main_reflexion.py --env_name Blackjack-v1 --init_summarizer blackjack_init_translator --curr_summarizer blackjack_basic_translator --decider exe_actor --prompt_level 3 --num_trails 5 --distiller guide_generator
python main_reflexion.py --env_name Blackjack-v1 --init_summarizer blackjack_init_translator --curr_summarizer blackjack_basic_translator --decider cot_actor --prompt_level 3 --num_trails 5  --distiller traj_distiller
python main_reflexion.py --env_name Blackjack-v1 --init_summarizer blackjack_init_translator --curr_summarizer blackjack_basic_translator --decider reflexion_actor --prompt_level 3 --num_trails 5 --distiller reflect_distiller
python main_reflexion.py --env_name Blackjack-v1 --init_summarizer blackjack_init_translator --curr_summarizer blackjack_basic_translator --decider self_consistency_actor --prompt_level 3 --num_trails 5  --distiller traj_distiller
python main_reflexion.py --env_name Blackjack-v1 --init_summarizer blackjack_init_translator --curr_summarizer blackjack_basic_translator --decider selfask_actor --prompt_level 3 --num_trails 5  --distiller traj_distiller
python main_reflexion.py --env_name Blackjack-v1 --init_summarizer blackjack_init_translator --curr_summarizer blackjack_basic_translator --decider spp_actor --prompt_level 3 --num_trails 5  --distiller traj_distiller
python main_reflexion.py --env_name Blackjack-v1 --init_summarizer blackjack_init_translator --curr_summarizer blackjack_basic_translator --decider naive_actor --prompt_level 3 --num_trails 5  --distiller traj_distiller