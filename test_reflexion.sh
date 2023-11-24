
# CartPole-v0
# Naive Actor
python main_reflexion.py --env_name CartPole-v0 --init_summarizer cart_init_translator --curr_summarizer cart_basic_translator --decider naive_actor --prompt_level 1 --num_trails 1 
python main_reflexion.py --env_name CartPole-v0 --init_summarizer cart_init_translator --curr_summarizer cart_basic_translator --decider naive_actor --prompt_level 3 -num_trails 2 --distiller traj_distiller  
python main_reflexion.py --env_name CartPole-v0 --init_summarizer cart_init_translator --curr_summarizer cart_basic_translator --decider naive_actor --prompt_level 4 --num_trails 1 --distiller traj_distiller --prompt_path "envs/classic_control/few_shot_examples/cartpole" 
python main_reflexion.py --env_name CartPole-v0 --init_summarizer cart_init_translator --curr_summarizer cart_basic_translator --decider naive_actor --prompt_level 5 --num_trails 1 

# COT
python main_reflexion.py --env_name CartPole-v0 --init_summarizer cart_init_translator --curr_summarizer cart_basic_translator --decider cot_actor --prompt_level 1 --num_trails 1 
python main_reflexion.py --env_name CartPole-v0 --init_summarizer cart_init_translator --curr_summarizer cart_basic_translator --decider cot_actor --prompt_level 3 -num_trails 2 --distiller traj_distiller  
python main_reflexion.py --env_name CartPole-v0 --init_summarizer cart_init_translator --curr_summarizer cart_basic_translator --decider cot_actor --prompt_level 4 --num_trails 1 --distiller traj_distiller --prompt_path "envs/classic_control/few_shot_examples/cartpole"
python main_reflexion.py --env_name CartPole-v0 --init_summarizer cart_init_translator --curr_summarizer cart_basic_translator --decider cot_actor --prompt_level 5 --num_trails 1 

# self consistency
python main_reflexion.py --env_name CartPole-v0 --init_summarizer cart_init_translator --curr_summarizer cart_basic_translator --decider self_consistency_actor --prompt_level 1 --num_trails 1 
python main_reflexion.py --env_name CartPole-v0 --init_summarizer cart_init_translator --curr_summarizer cart_basic_translator --decider self_consistency_actor --prompt_level 3 -num_trails 2 --distiller traj_distiller  
python main_reflexion.py --env_name CartPole-v0 --init_summarizer cart_init_translator --curr_summarizer cart_basic_translator --decider self_consistency_actor --prompt_level 4 --num_trails 1 --distiller traj_distiller --prompt_path "envs/classic_control/few_shot_examples/cartpole" 
python main_reflexion.py --env_name CartPole-v0 --init_summarizer cart_init_translator --curr_summarizer cart_basic_translator --decider self_consistency_actor --prompt_level 5 --num_trails 1 

# self-ask
python main_reflexion.py --env_name CartPole-v0 --init_summarizer cart_init_translator --curr_summarizer cart_basic_translator --decider selfask_actor --prompt_level 1 --num_trails 1 
python main_reflexion.py --env_name CartPole-v0 --init_summarizer cart_init_translator --curr_summarizer cart_basic_translator --decider selfask_actor --prompt_level 3 -num_trails 2 --distiller traj_distiller  
python main_reflexion.py --env_name CartPole-v0 --init_summarizer cart_init_translator --curr_summarizer cart_basic_translator --decider selfask_actor --prompt_level 4 --num_trails 1 --distiller traj_distiller --prompt_path "envs/classic_control/few_shot_examples/cartpole" 
python main_reflexion.py --env_name CartPole-v0 --init_summarizer cart_init_translator --curr_summarizer cart_basic_translator --decider selfask_actor --prompt_level 5 --num_trails 1 

# SPP
python main_reflexion.py --env_name CartPole-v0 --init_summarizer cart_init_translator --curr_summarizer cart_basic_translator --decider spp_actor --prompt_level 1 --num_trails 1 
python main_reflexion.py --env_name CartPole-v0 --init_summarizer cart_init_translator --curr_summarizer cart_basic_translator --decider spp_actor --prompt_level 3 -num_trails 2 --distiller traj_distiller  
python main_reflexion.py --env_name CartPole-v0 --init_summarizer cart_init_translator --curr_summarizer cart_basic_translator --decider spp_actor --prompt_level 4 --num_trails 1 --distiller traj_distiller --prompt_path "envs/classic_control/few_shot_examples/cartpole" 
python main_reflexion.py --env_name CartPole-v0 --init_summarizer cart_init_translator --curr_summarizer cart_basic_translator --decider spp_actor --prompt_level 5 --num_trails 1 

# REFLEXION
python main_reflexion.py --env_name CartPole-v0 --init_summarizer cart_init_translator --curr_summarizer cart_basic_translator --decider reflexion_actor --prompt_level 1 --num_trails 1 --distiller reflect_distiller 
python main_reflexion.py --env_name CartPole-v0 --init_summarizer cart_init_translator --curr_summarizer cart_basic_translator --decider reflexion_actor --prompt_level 3 -num_trails 2 --distiller reflect_distiller 
python main_reflexion.py --env_name CartPole-v0 --init_summarizer cart_init_translator --curr_summarizer cart_basic_translator --decider reflexion_actor --prompt_level 4 --num_trails 1 --distiller reflect_distiller --prompt_path "envs/classic_control/few_shot_examples/cartpole" 
python main_reflexion.py --env_name CartPole-v0 --init_summarizer cart_init_translator --curr_summarizer cart_basic_translator --decider reflexion_actor --prompt_level 5 --num_trails 1 --distiller reflect_distiller 

# exe
python main_reflexion.py --env_name CartPole-v0 --init_summarizer cart_init_translator --curr_summarizer cart_basic_translator --decider exe_actor --prompt_level 1 --num_trails 1 --distiller guide_generator 
python main_reflexion.py --env_name CartPole-v0 --init_summarizer cart_init_translator --curr_summarizer cart_basic_translator --decider exe_actor --prompt_level 3 -num_trails 2 --distiller guide_generator 
python main_reflexion.py --env_name CartPole-v0 --init_summarizer cart_init_translator --curr_summarizer cart_basic_translator --decider exe_actor --prompt_level 4 --num_trails 1 --distiller guide_generator --prompt_path "envs/classic_control/few_shot_examples/cartpole" 
python main_reflexion.py --env_name CartPole-v0 --init_summarizer cart_init_translator --curr_summarizer cart_basic_translator --decider exe_actor --prompt_level 5 --num_trails 1 --distiller guide_generator 