# InvertedDoublePendulum-v4

# REFLEXION
python main_reflexion.py --env_name InvertedDoublePendulum-v4 --init_summarizer invertedDoublePendulum_init_translator --curr_summarizer invertedDoublePendulum_basic_translator --decider reflexion_actor --prompt_level 1 --num_trails 1 --distiller reflect_distiller 

python main_reflexion.py --env_name InvertedDoublePendulum-v4 --init_summarizer invertedDoublePendulum_init_translator --curr_summarizer invertedDoublePendulum_basic_translator --decider reflexion_actor --prompt_level 3 --num_trails 5 --distiller reflect_distiller 

python main_reflexion.py --env_name InvertedDoublePendulum-v4 --init_summarizer invertedDoublePendulum_init_translator --curr_summarizer invertedDoublePendulum_basic_translator --decider reflexion_actor --prompt_level 5 --num_trails 1 --distiller reflect_distiller 


# exe
python main_reflexion.py --env_name InvertedDoublePendulum-v4 --init_summarizer invertedDoublePendulum_init_translator --curr_summarizer invertedDoublePendulum_basic_translator --decider exe_actor --prompt_level 1 --num_trails 1 --distiller guide_generator --api_type openai

python main_reflexion.py --env_name InvertedDoublePendulum-v4 --init_summarizer invertedDoublePendulum_init_translator --curr_summarizer invertedDoublePendulum_basic_translator --decider exe_actor --prompt_level 3 --num_trails 5 --distiller guide_generator

python main_reflexion.py --env_name InvertedDoublePendulum-v4 --init_summarizer invertedDoublePendulum_init_translator --curr_summarizer invertedDoublePendulum_basic_translator --decider exe_actor --prompt_level 5 --num_trails 1 --distiller guide_generator