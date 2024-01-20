# Hopper-v4

# COT
python main_reflexion.py --env_name Hopper-v4 --init_summarizer hopper_init_translator --curr_summarizer hopper_basic_translator --decider cot_actor --prompt_level 1 --num_trails 1

python main_reflexion.py --env_name Hopper-v4 --init_summarizer hopper_init_translator --curr_summarizer hopper_basic_translator --decider cot_actor --prompt_level 3 --num_trails 5 --distiller traj_distiller 

# SPP
python main_reflexion.py --env_name Hopper-v4 --init_summarizer hopper_init_translator --curr_summarizer hopper_basic_translator --decider spp_actor --prompt_level 1 --num_trails 1

python main_reflexion.py --env_name Hopper-v4 --init_summarizer hopper_init_translator --curr_summarizer hopper_basic_translator --decider spp_actor --prompt_level 3 --num_trails 5 --distiller traj_distiller 



# REFLEXION
python main_reflexion.py --env_name Hopper-v4 --init_summarizer hopper_init_translator --curr_summarizer hopper_basic_translator --decider reflexion_actor --prompt_level 1 --num_trails 1 --distiller reflect_distiller 

python main_reflexion.py --env_name Hopper-v4 --init_summarizer hopper_init_translator --curr_summarizer hopper_basic_translator --decider reflexion_actor --prompt_level 3 --num_trails 5 --distiller reflect_distiller 

python main_reflexion.py --env_name Hopper-v4 --init_summarizer hopper_init_translator --curr_summarizer hopper_basic_translator --decider reflexion_actor --prompt_level 5 --num_trails 1 --distiller reflect_distiller 


# exe
python main_reflexion.py --env_name Hopper-v4 --init_summarizer hopper_init_translator --curr_summarizer hopper_basic_translator --decider exe_actor --prompt_level 1 --num_trails 1 --distiller guide_generator --api_type openai

python main_reflexion.py --env_name Hopper-v4 --init_summarizer hopper_init_translator --curr_summarizer hopper_basic_translator --decider exe_actor --prompt_level 3 --num_trails 5 --distiller guide_generator

python main_reflexion.py --env_name Hopper-v4 --init_summarizer hopper_init_translator --curr_summarizer hopper_basic_translator --decider exe_actor --prompt_level 5 --num_trails 1 --distiller guide_generator