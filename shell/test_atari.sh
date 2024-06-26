# python main_reflexion.py --env_name RepresentedBoxing-v0 --init_summarizer RepresentedBoxing_init_translator --curr_summarizer RepresentedBoxing_basic_translator --decider cot_actor --prompt_level 1 --num_trails 1 --seed 0 --api_type vllm --gpt_version Meta-Llama-3-8B-Instruct --max_episode_len 4500 
# python main_reflexion.py --env_name RepresentedPong-v0 --init_summarizer RepresentedPong_init_translator --curr_summarizer RepresentedPong_basic_translator --decider cot_actor --prompt_level 1 --num_trails 1 --seed 0 --api_type vllm --gpt_version Meta-Llama-3-8B-Instruct --max_episode_len 4500

# python main_reflexion.py --env_name RepresentedMsPacman-v0 --init_summarizer RepresentedMsPacman_init_translator --curr_summarizer RepresentedMsPacman_basic_translator --decider cot_actor --prompt_level 1 --num_trails 1 --seed 0 --api_type vllm --gpt_version Meta-Llama-3-8B-Instruct --max_episode_len 4500

# python main_reflexion.py --env_name RepresentedMontezumaRevenge-v0 --init_summarizer RepresentedMontezumaRevenge_init_translator --curr_summarizer RepresentedMontezumaRevenge_basic_translator --decider cot_actor --prompt_level 1 --num_trails 1 --seed 0 --api_type vllm --gpt_version Meta-Llama-3-8B-Instruct --max_episode_len 4500

# Boxing
python main_reflexion.py --env_name RepresentedBoxing-v0 --init_summarizer RepresentedBoxing_init_translator --curr_summarizer RepresentedBoxing_basic_translator --decider cot_actor  --prompt_level 3 --num_trails 5  --distiller traj_distiller --seed 0 --api_type vllm --gpt_version Meta-Llama-3-8B-Instruct --max_episode_len 4500 

python main_reflexion.py --env_name RepresentedBoxing-v0 --init_summarizer RepresentedBoxing_init_translator --curr_summarizer RepresentedBoxing_basic_translator --decider reflexion_actor  --prompt_level 3 --num_trails 5  --distiller reflect_distiller --seed 0 --api_type vllm --gpt_version Meta-Llama-3-8B-Instruct --max_episode_len 4500 

# Pong
python main_reflexion.py --env_name RepresentedPong-v0 --init_summarizer RepresentedPong_init_translator --curr_summarizer RepresentedPong_basic_translator  --decider cot_actor --prompt_level 3 --num_trails 5  --distiller traj_distiller --seed 0 --api_type vllm --gpt_version Meta-Llama-3-8B-Instruct --max_episode_len 4500

python main_reflexion.py --env_name RepresentedPong-v0 --init_summarizer RepresentedPong_init_translator --curr_summarizer RepresentedPong_basic_translator  --decider reflexion_actor --prompt_level 3 --num_trails 5  --distiller reflect_distiller --seed 0 --api_type vllm --gpt_version Meta-Llama-3-8B-Instruct --max_episode_len 4500

# PacMan

python main_reflexion.py --env_name RepresentedMsPacman-v0 --init_summarizer RepresentedMsPacman_init_translator --curr_summarizer RepresentedMsPacman_basic_translator  --decider cot_actor --prompt_level 3 --num_trails 5  --distiller traj_distiller --seed 0 --api_type vllm --gpt_version Meta-Llama-3-8B-Instruct --max_episode_len 4500
python main_reflexion.py --env_name RepresentedMsPacman-v0 --init_summarizer RepresentedMsPacman_init_translator --curr_summarizer RepresentedMsPacman_basic_translator  --decider reflexion_actor --prompt_level 3 --num_trails 5  --distiller reflect_distiller --seed 0 --api_type vllm --gpt_version Meta-Llama-3-8B-Instruct --max_episode_len 4500

# python main_reflexion.py --env_name RepresentedMontezumaRevenge-v0 --init_summarizer RepresentedMontezumaRevenge_init_translator --curr_summarizer RepresentedMontezumaRevenge_basic_translator --decider cot_actor --decider cot_actor --prompt_level 3 --num_trails 5  --distiller traj_distiller --seed 0 --api_type vllm --gpt_version Meta-Llama-3-8B-Instruct --max_episode_len 4500
