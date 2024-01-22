# CoT 
## Atari
python main_reflexion.py --env_name RepresentedPong-v0 --init_summarizer RepresentedPong_init_translator --curr_summarizer RepresentedPong_basic_translator --decider naive_actor --prompt_level 1 --num_trails 1 --seed 0 --gpt_version gpt-3.5-turbo-1106

python main_reflexion.py --env_name RepresentedMsPacman-v0 --init_summarizer RepresentedMsPacman_init_translator --curr_summarizer RepresentedMsPacman_basic_translator --decider naive_actor --prompt_level 1 --num_trails 1 --seed 0 --gpt_version gpt-3.5-turbo-1106

python main_reflexion.py --env_name RepresentedMontezumaRevenge-v0 --init_summarizer RepresentedMontezumaRevenge_init_translator --curr_summarizer RepresentedMontezumaRevenge_basic_translator --decider naive_actor --prompt_level 1 --num_trails 1 --seed 0 --gpt_version gpt-3.5-turbo-1106

## Mujoco
python main_reflexion.py --env_name Hopper-v4 --init_summarizer hopper_init_translator --curr_summarizer hopper_basic_translator --decider cot_actor --prompt_level 1 --num_trails 1 --seed 0 --gpt_version gpt-3.5-turbo-1106

python main_reflexion.py --env_name Walker2d-v4 --init_summarizer walker2d_init_translator --curr_summarizer walker2d_basic_translator --decider cot_actor  --seed 0  --prompt_level 1 --num_trails 1 --gpt_version gpt-3.5-turbo-1106

python main_reflexion.py --env_name Ant-v4 --init_summarizer ant_init_translator --curr_summarizer ant_basic_translator --decider cot_actor --prompt_level 1 --num_trails 1 --seed 0 --gpt_version gpt-3.5-turbo-1106