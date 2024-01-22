# CoT 
## Atari
python main_reflexion.py --env_name RepresentedPong-v0 --init_summarizer RepresentedPong_init_translator --curr_summarizer RepresentedPong_basic_translator --decider naive_actor --prompt_level 1 --num_trails 1 --seed 0

python main_reflexion.py --env_name RepresentedMsPacman-v0 --init_summarizer RepresentedMsPacman_init_translator --curr_summarizer RepresentedMsPacman_basic_translator --decider naive_actor --prompt_level 1 --num_trails 1 --seed 0 

python main_reflexion.py --env_name RepresentedMontezumaRevenge-v0 --init_summarizer RepresentedMontezumaRevenge_init_translator --curr_summarizer RepresentedMontezumaRevenge_basic_translator --decider naive_actor --prompt_level 1 --num_trails 1 --seed 0

