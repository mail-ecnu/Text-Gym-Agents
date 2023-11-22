# # ppo for cartpole-v0
# CUDA_VISIBLE_DEVICES=1 python RL_based/train_PPO.py --env_name CartPole-v0 --init_summarizer cart_init_translator --curr_summarizer cart_basic_translator\
#  --trans_model_name distilbert-base-uncased --model_name nn_embedding --eval --policy-path RL_based/checkpoints/CartPole-v0/expert/policy.pth --collect_one_episode

# # ppo for lunarlander: treasured-music-91 score: 164.66
# TRANSFORMERS_OFFLINE=1 \
# CUDA_VISIBLE_DEVICES=2 python RL_based/train_PPO.py --env_name LunarLander-v2 --init_summarizer lunarLander_init_translator --curr_summarizer lunarLander_basic_translator \
#  --trans_model_name /home/ubuntu/LLM-Decider-Bench/RL_based/transformer_offline_distilbert --model_name nn_embedding --max_length 128 --eval --collect_one_episode --policy-path /home/ubuntu/LLM-Decider-Bench/RL_based/checkpoints/LunarLander-v2/expert/policy.pth

# ppo for Acrobot-v1: charmed-salad-93 score: -85.8
# TRANSFORMERS_OFFLINE=1 \
# CUDA_VISIBLE_DEVICES=0 python RL_based/train_PPO.py --env_name Acrobot-v1 --init_summarizer acrobot_init_translator --curr_summarizer acrobot_basic_translator --decider naive_actor --prompt_level 1\
#  --trans_model_name /home/ubuntu/LLM-Decider-Bench/RL_based/transformer_offline_distilbert --model_name nn_embedding --max_length 128 --eval --collect_one_episode --policy-path /home/ubuntu/LLM-Decider-Bench/RL_based/checkpoints/Acrobot-v1/expert/policy.pth

# # # # ppo for MountainCar-v0: 
# TRANSFORMERS_OFFLINE=1 \
# CUDA_VISIBLE_DEVICES=1 python RL_based/train_PPO.py --env_name MountainCar-v0 --init_summarizer mountaincar_init_translator --curr_summarizer mountaincar_basic_translator --decider naive_actor --prompt_level 1\
#  --trans_model_name /home/ubuntu/LLM-Decider-Bench/RL_based/transformer_offline_distilbert --model_name nn_embedding --max_length 128 --eval --collect_one_episode --policy-path /home/ubuntu/LLM-Decider-Bench/RL_based/checkpoints/MountainCar-v0/expert/policy.pth
 
# # ppo for Blackjack-v1
# TRANSFORMERS_OFFLINE=1 \
# CUDA_VISIBLE_DEVICES=2 python RL_based/train_PPO.py --env_name Blackjack-v1 --init_summarizer blackjack_init_translator --curr_summarizer blackjack_basic_translator --decider naive_actor --prompt_level 1\
#  --trans_model_name /home/ubuntu/LLM-Decider-Bench/RL_based/transformer_offline_distilbert --model_name nn_embedding --max_length 128 --eval --collect_one_episode --policy-path /home/ubuntu/LLM-Decider-Bench/RL_based/checkpoints/Blackjack-v1/expert/policy.pth
 
# # # ppo for Taxi-v3
TRANSFORMERS_OFFLINE=1 \
CUDA_VISIBLE_DEVICES=6 python RL_based/train_PPO.py --env_name Taxi-v3 --init_summarizer taxi_init_translator --curr_summarizer taxi_basic_translator --decider naive_actor --prompt_level 1\
 --trans_model_name /home/ubuntu/LLM-Decider-Bench/RL_based/transformer_offline_distilbert --model_name nn_embedding --max_length 128 --eval --collect_one_episode --policy-path /home/ubuntu/LLM-Decider-Bench/RL_based/checkpoints/Taxi-v3/expert/policy.pth
 
# # # ppo for CliffWalking-v0
# TRANSFORMERS_OFFLINE=1 \
# CUDA_VISIBLE_DEVICES=4 python RL_based/train_PPO.py --env_name CliffWalking-v0 --init_summarizer cliffwalking_init_translator --curr_summarizer cliffwalking_basic_translator --decider naive_actor --prompt_level 1\
#  --trans_model_name /home/ubuntu/LLM-Decider-Bench/RL_based/transformer_offline_distilbert --model_name nn_embedding --max_length 128 --eval --collect_one_episode --policy-path /home/ubuntu/LLM-Decider-Bench/RL_based/checkpoints/CliffWalking-v0/expert/policy.pth
 
# # # ppo for FrozenLake-v1
# TRANSFORMERS_OFFLINE=1 \
# CUDA_VISIBLE_DEVICES=5 python RL_based/train_PPO.py --env_name FrozenLake-v1 --init_summarizer frozenlake_init_translator --curr_summarizer frozenlake_basic_translator --decider naive_actor --prompt_level 1\
#  --trans_model_name /home/ubuntu/LLM-Decider-Bench/RL_based/transformer_offline_distilbert --model_name nn_embedding --max_length 128 --eval --collect_one_episode --policy-path /home/ubuntu/LLM-Decider-Bench/RL_based/checkpoints/FrozenLake-v1/expert/policy.pth
 