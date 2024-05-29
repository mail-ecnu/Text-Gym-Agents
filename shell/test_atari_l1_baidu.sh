#!/bin/bash

# Check if the argument is provided
if [ -z "$1" ]; then
  echo "Usage: $0 <argument>"
  exit 1
fi

# The argument to pass to all tasks
key_name=$1

# Array to hold the PIDs of the background jobs
pids=()

# Function to control the number of background tasks
control_jobs() {
  while [ ${#pids[@]} -ge 4 ]
  do
    # Wait for any of the background jobs to finish
    wait -n
    # Remove finished PIDs from the array
    new_pids=()
    for pid in "${pids[@]}"; do
      if kill -0 "$pid" 2>/dev/null; then
        new_pids+=("$pid")
      fi
    done
    pids=("${new_pids[@]}")
  done
}

# Start the tasks with controlled concurrency
run_task() {
  control_jobs
  echo "Starting task: $1"
  eval "$1 &" # Run the task in the background
  # Add the PID of the last background job to the array
  pids+=($!)
}
# Define your tasks
tasks=(
# Boxing

# "python main_reflexion.py --env_name RepresentedBoxing-v0 --init_summarizer RepresentedBoxing_init_translator --curr_summarizer RepresentedBoxing_basic_translator --decider cot_actor  --prompt_level 1 --num_trails 1  --distiller traj_distiller --seed 0 --api_type aistudio --gpt_version  ERNIE-Speed-8K --key_name $key_name "

# "python main_reflexion.py --env_name RepresentedBoxing-v0 --init_summarizer RepresentedBoxing_init_translator --curr_summarizer RepresentedBoxing_basic_translator --decider cot_actor  --prompt_level 1 --num_trails 1  --distiller traj_distiller --seed 0 --api_type aistudio --gpt_version  ERNIE-Lite-8K --key_name $key_name "

# "python main_reflexion.py --env_name RepresentedBoxing-v0 --init_summarizer RepresentedBoxing_init_translator --curr_summarizer RepresentedBoxing_basic_translator --decider cot_actor  --prompt_level 1 --num_trails 1  --distiller traj_distiller --seed 0 --api_type aistudio --gpt_version  ERNIE-Tiny-8K --key_name $key_name "

# Pong

"python main_reflexion.py --env_name RepresentedPong-v0 --init_summarizer RepresentedPong_init_translator --curr_summarizer RepresentedPong_basic_translator  --decider cot_actor --prompt_level 1 --num_trails 1  --distiller traj_distiller --seed 0 --api_type aistudio --gpt_version  ERNIE-Speed-8K  --key_name $key_name " 

"python main_reflexion.py --env_name RepresentedPong-v0 --init_summarizer RepresentedPong_init_translator --curr_summarizer RepresentedPong_basic_translator  --decider cot_actor --prompt_level 1 --num_trails 1  --distiller traj_distiller --seed 0 --api_type aistudio --gpt_version  ERNIE-Lite-8K  --key_name $key_name "

"python main_reflexion.py --env_name RepresentedPong-v0 --init_summarizer RepresentedPong_init_translator --curr_summarizer RepresentedPong_basic_translator  --decider cot_actor --prompt_level 1 --num_trails 1  --distiller traj_distiller --seed 0 --api_type aistudio --gpt_version  ERNIE-Tiny-8K  --key_name $key_name "


# Asteroids

"python main_reflexion.py --env_name RepresentedAsteroids-v0 --init_summarizer RepresentedAsteroids_init_translator --curr_summarizer RepresentedAsteroids_basic_translator  --decider cot_actor --prompt_level 1 --num_trails 1  --distiller traj_distiller --seed 0 --api_type aistudio --gpt_version ERNIE-Speed-8K --key_name $key_name " 


"python main_reflexion.py --env_name RepresentedAsteroids-v0 --init_summarizer RepresentedAsteroids_init_translator --curr_summarizer RepresentedAsteroids_basic_translator  --decider cot_actor --prompt_level 1 --num_trails 1  --distiller traj_distiller --seed 0 --api_type aistudio --gpt_version ERNIE-Lite-8K --key_name $key_name "

"python main_reflexion.py --env_name RepresentedAsteroids-v0 --init_summarizer RepresentedAsteroids_init_translator --curr_summarizer RepresentedAsteroids_basic_translator  --decider cot_actor --prompt_level 1 --num_trails 1  --distiller traj_distiller --seed 0 --api_type aistudio --gpt_version  ERNIE-Tiny-8K --key_name $key_name "


# BattleZone
"python main_reflexion.py --env_name RepresentedBattleZone-v0 --init_summarizer RepresentedBattleZone_init_translator --curr_summarizer RepresentedBattleZone_basic_translator  --decider cot_actor --prompt_level 1 --num_trails 1  --distiller traj_distiller --seed 0 --api_type aistudio --gpt_version ERNIE-Speed-8K --key_name $key_name " 

"python main_reflexion.py --env_name RepresentedBattleZone-v0 --init_summarizer RepresentedBattleZone_init_translator --curr_summarizer RepresentedBattleZone_basic_translator  --decider cot_actor --prompt_level 1 --num_trails 1  --distiller traj_distiller --seed 0 --api_type aistudio --gpt_version ERNIE-Lite-8K --key_name $key_name "

"python main_reflexion.py --env_name RepresentedBattleZone-v0 --init_summarizer RepresentedBattleZone_init_translator --curr_summarizer RepresentedBattleZone_basic_translator  --decider cot_actor --prompt_level 1 --num_trails 1  --distiller traj_distiller --seed 0 --api_type aistudio --gpt_version ERNIE-Tiny-8K --key_name $key_name " 

# Berzerk
"python main_reflexion.py --env_name RepresentedBerzerk-v0 --init_summarizer RepresentedBerzerk_init_translator --curr_summarizer RepresentedBerzerk_basic_translator  --decider cot_actor --prompt_level 1 --num_trails 1  --distiller traj_distiller --seed 0 --api_type aistudio --gpt_version ERNIE-Speed-8K --key_name $key_name " 

"python main_reflexion.py --env_name RepresentedBerzerk-v0 --init_summarizer RepresentedBerzerk_init_translator --curr_summarizer RepresentedBerzerk_basic_translator  --decider cot_actor --prompt_level 1 --num_trails 1  --distiller traj_distiller --seed 0 --api_type aistudio --gpt_version ERNIE-Speed-128K --key_name $key_name " 

"python main_reflexion.py --env_name RepresentedBerzerk-v0 --init_summarizer RepresentedBerzerk_init_translator --curr_summarizer RepresentedBerzerk_basic_translator  --decider cot_actor --prompt_level 1 --num_trails 1  --distiller traj_distiller --seed 0 --api_type aistudio --gpt_version ERNIE-Tiny-8K --key_name $key_name " 

# Bowling
"python main_reflexion.py --env_name RepresentedBowling-v0 --init_summarizer RepresentedBowling_init_translator --curr_summarizer RepresentedBowling_basic_translator  --decider cot_actor --prompt_level 1 --num_trails 1  --distiller traj_distiller --seed 0 --api_type aistudio --gpt_version ERNIE-Speed-8K --key_name $key_name " 

"python main_reflexion.py --env_name RepresentedBowling-v0 --init_summarizer RepresentedBowling_init_translator --curr_summarizer RepresentedBowling_basic_translator  --decider cot_actor --prompt_level 1 --num_trails 1  --distiller traj_distiller --seed 0 --api_type aistudio --gpt_version ERNIE-Lite-8K --key_name $key_name " 

"python main_reflexion.py --env_name RepresentedBowling-v0 --init_summarizer RepresentedBowling_init_translator --curr_summarizer RepresentedBowling_basic_translator  --decider cot_actor --prompt_level 1 --num_trails 1  --distiller traj_distiller --seed 0 --api_type aistudio --gpt_version ERNIE-Tiny-8K --key_name $key_name " 

# Breakout
"python main_reflexion.py --env_name RepresentedBreakout-v0 --init_summarizer RepresentedBreakout_init_translator --curr_summarizer RepresentedBreakout_basic_translator  --decider cot_actor --prompt_level 1 --num_trails 1  --distiller traj_distiller --seed 0 --api_type aistudio --gpt_version ERNIE-Speed-8K --key_name $key_name " 

"python main_reflexion.py --env_name RepresentedBreakout-v0 --init_summarizer RepresentedBreakout_init_translator --curr_summarizer RepresentedBreakout_basic_translator  --decider cot_actor --prompt_level 1 --num_trails 1  --distiller traj_distiller --seed 0 --api_type aistudio --gpt_version ERNIE-Lite-8K --key_name $key_name " 

"python main_reflexion.py --env_name RepresentedBreakout-v0 --init_summarizer RepresentedBreakout_init_translator --curr_summarizer RepresentedBreakout_basic_translator  --decider cot_actor --prompt_level 1 --num_trails 1  --distiller traj_distiller --seed 0 --api_type aistudio --gpt_version ERNIE-Tiny-8K --key_name $key_name " 

# Skiing
"python main_reflexion.py --env_name RepresentedSkiing-v0 --init_summarizer RepresentedSkiing_init_translator --curr_summarizer RepresentedSkiing_basic_translator  --decider cot_actor --prompt_level 1 --num_trails 1  --distiller traj_distiller --seed 0 --api_type aistudio --gpt_version ERNIE-Speed-8K --key_name $key_name " 

"python main_reflexion.py --env_name RepresentedSkiing-v0 --init_summarizer RepresentedSkiing_init_translator --curr_summarizer RepresentedSkiing_basic_translator  --decider cot_actor --prompt_level 1 --num_trails 1  --distiller traj_distiller --seed 0 --api_type aistudio --gpt_version ERNIE-Lite-8K --key_name $key_name " 

"python main_reflexion.py --env_name RepresentedSkiing-v0 --init_summarizer RepresentedSkiing_init_translator --curr_summarizer RepresentedSkiing_basic_translator  --decider cot_actor --prompt_level 1 --num_trails 1  --distiller traj_distiller --seed 0 --api_type aistudio --gpt_version ERNIE-Tiny-8K --key_name $key_name " 

# DemonAttack
"python main_reflexion.py --env_name RepresentedDemonAttack-v0 --init_summarizer RepresentedDemonAttack_init_translator --curr_summarizer RepresentedDemonAttack_basic_translator  --decider cot_actor --prompt_level 1 --num_trails 1  --distiller traj_distiller --seed 0 --api_type aistudio --gpt_version ERNIE-Speed-8K --key_name $key_name " 
 
"python main_reflexion.py --env_name RepresentedDemonAttack-v0 --init_summarizer RepresentedDemonAttack_init_translator --curr_summarizer RepresentedDemonAttack_basic_translator  --decider cot_actor --prompt_level 1 --num_trails 1  --distiller traj_distiller --seed 0 --api_type aistudio --gpt_version ERNIE-Lite-8K --key_name $key_name " 

"python main_reflexion.py --env_name RepresentedDemonAttack-v0 --init_summarizer RepresentedDemonAttack_init_translator --curr_summarizer RepresentedDemonAttack_basic_translator  --decider cot_actor --prompt_level 1 --num_trails 1  --distiller traj_distiller --seed 0 --api_type aistudio --gpt_version ERNIE-Tiny-8K --key_name $key_name " 

# Freeway
"python main_reflexion.py --env_name RepresentedFreeway-v0 --init_summarizer RepresentedFreeway_init_translator --curr_summarizer RepresentedFreeway_basic_translator  --decider cot_actor --prompt_level 1 --num_trails 1  --distiller traj_distiller --seed 0 --api_type aistudio --gpt_version ERNIE-Speed-8K --key_name $key_name " 

"python main_reflexion.py --env_name RepresentedFreeway-v0 --init_summarizer RepresentedFreeway_init_translator --curr_summarizer RepresentedFreeway_basic_translator  --decider cot_actor --prompt_level 1 --num_trails 1  --distiller traj_distiller --seed 0 --api_type aistudio --gpt_version ERNIE-Lite-8K --key_name $key_name " 

"python main_reflexion.py --env_name RepresentedFreeway-v0 --init_summarizer RepresentedFreeway_init_translator --curr_summarizer RepresentedFreeway_basic_translator  --decider cot_actor --prompt_level 1 --num_trails 1  --distiller traj_distiller --seed 0 --api_type aistudio --gpt_version ERNIE-Tiny-8K --key_name $key_name " 

# Frostbite
"python main_reflexion.py --env_name RepresentedFrostbite-v0 --init_summarizer RepresentedFrostbite_init_translator --curr_summarizer RepresentedFrostbite_basic_translator  --decider cot_actor --prompt_level 1 --num_trails 1  --distiller traj_distiller --seed 0 --api_type aistudio --gpt_version ERNIE-Speed-8K --key_name $key_name " 

"python main_reflexion.py --env_name RepresentedFrostbite-v0 --init_summarizer RepresentedFrostbite_init_translator --curr_summarizer RepresentedFrostbite_basic_translator  --decider cot_actor --prompt_level 1 --num_trails 1  --distiller traj_distiller --seed 0 --api_type aistudio --gpt_version ERNIE-Lite-8K --key_name $key_name " 

"python main_reflexion.py --env_name RepresentedFrostbite-v0 --init_summarizer RepresentedFrostbite_init_translator --curr_summarizer RepresentedFrostbite_basic_translator  --decider cot_actor --prompt_level 1 --num_trails 1  --distiller traj_distiller --seed 0 --api_type aistudio --gpt_version ERNIE-Tiny-8K --key_name $key_name " 


# Qbert
"python main_reflexion.py --env_name RepresentedQbert-v0 --init_summarizer RepresentedQbert_init_translator --curr_summarizer RepresentedQbert_basic_translator  --decider cot_actor --prompt_level 1 --num_trails 1  --distiller traj_distiller --seed 0 --api_type aistudio --gpt_version ERNIE-Speed-8K --key_name $key_name " 

"python main_reflexion.py --env_name RepresentedQbert-v0 --init_summarizer RepresentedQbert_init_translator --curr_summarizer RepresentedQbert_basic_translator  --decider cot_actor --prompt_level 1 --num_trails 1  --distiller traj_distiller --seed 0 --api_type aistudio --gpt_version ERNIE-Lite-8K --key_name $key_name " 

"python main_reflexion.py --env_name RepresentedQbert-v0 --init_summarizer RepresentedQbert_init_translator --curr_summarizer RepresentedQbert_basic_translator  --decider cot_actor --prompt_level 1 --num_trails 1  --distiller traj_distiller --seed 0 --api_type aistudio --gpt_version ERNIE-Tiny-8K --key_name $key_name " 

# Riverraid
"python main_reflexion.py --env_name RepresentedRiverraid-v0 --init_summarizer RepresentedRiverraid_init_translator --curr_summarizer RepresentedRiverraid_basic_translator  --decider cot_actor --prompt_level 1 --num_trails 1  --distiller traj_distiller --seed 0 --api_type aistudio --gpt_version ERNIE-Speed-8K --key_name $key_name " 

"python main_reflexion.py --env_name RepresentedRiverraid-v0 --init_summarizer RepresentedRiverraid_init_translator --curr_summarizer RepresentedRiverraid_basic_translator  --decider cot_actor --prompt_level 1 --num_trails 1  --distiller traj_distiller --seed 0 --api_type aistudio --gpt_version ERNIE-Lite-8K --key_name $key_name " 

"python main_reflexion.py --env_name RepresentedRiverraid-v0 --init_summarizer RepresentedRiverraid_init_translator --curr_summarizer RepresentedRiverraid_basic_translator  --decider cot_actor --prompt_level 1 --num_trails 1  --distiller traj_distiller --seed 0 --api_type aistudio --gpt_version ERNIE-Tiny-8K --key_name $key_name " 

# Seaquest
"python main_reflexion.py --env_name RepresentedSeaquest-v0 --init_summarizer RepresentedSeaquest_init_translator --curr_summarizer RepresentedSeaquest_basic_translator  --decider cot_actor --prompt_level 1 --num_trails 1  --distiller traj_distiller --seed 0 --api_type aistudio --gpt_version ERNIE-Speed-8K --key_name $key_name " 

"python main_reflexion.py --env_name RepresentedSeaquest-v0 --init_summarizer RepresentedSeaquest_init_translator --curr_summarizer RepresentedSeaquest_basic_translator  --decider cot_actor --prompt_level 1 --num_trails 1  --distiller traj_distiller --seed 0 --api_type aistudio --gpt_version ERNIE-Lite-8K --key_name $key_name " 

"python main_reflexion.py --env_name RepresentedSeaquest-v0 --init_summarizer RepresentedSeaquest_init_translator --curr_summarizer RepresentedSeaquest_basic_translator  --decider cot_actor --prompt_level 1 --num_trails 1  --distiller traj_distiller --seed 0 --api_type aistudio --gpt_version ERNIE-Tiny-8K --key_name $key_name " 

# SpaceInvaders
"python main_reflexion.py --env_name RepresentedSpaceInvaders-v0 --init_summarizer RepresentedSpaceInvaders_init_translator --curr_summarizer RepresentedSpaceInvaders_basic_translator  --decider cot_actor --prompt_level 1 --num_trails 1  --distiller traj_distiller --seed 0 --api_type aistudio --gpt_version ERNIE-Speed-8K --key_name $key_name " 

"python main_reflexion.py --env_name RepresentedSpaceInvaders-v0 --init_summarizer RepresentedSpaceInvaders_init_translator --curr_summarizer RepresentedSpaceInvaders_basic_translator  --decider cot_actor --prompt_level 1 --num_trails 1  --distiller traj_distiller --seed 0 --api_type aistudio --gpt_version ERNIE-Lite-8K --key_name $key_name " 

"python main_reflexion.py --env_name RepresentedSpaceInvaders-v0 --init_summarizer RepresentedSpaceInvaders_init_translator --curr_summarizer RepresentedSpaceInvaders_basic_translator  --decider cot_actor --prompt_level 1 --num_trails 1  --distiller traj_distiller --seed 0 --api_type aistudio --gpt_version ERNIE-Tiny-8K --key_name $key_name " 


# PacMan


"python main_reflexion.py --env_name RepresentedMsPacman-v0 --init_summarizer RepresentedMsPacman_init_translator --curr_summarizer RepresentedMsPacman_basic_translator  --decider cot_actor --prompt_level 1 --num_trails 1  --distiller traj_distiller --seed 0 --api_type aistudio --gpt_version  ERNIE-Speed-8K --key_name $key_name " 


"python main_reflexion.py --env_name RAepresentedMsPacman-v0 --init_summarizer RepresentedMsPacman_init_translator --curr_summarizer RepresentedMsPacman_basic_translator  --decider cot_actor --prompt_level 1 --num_trails 1  --distiller traj_distiller --seed 0 --api_type aistudio --gpt_version ERNIE-Lite-8K --key_name $key_name "

"python main_reflexion.py --env_name RepresentedMsPacman-v0 --init_summarizer RepresentedMsPacman_init_translator --curr_summarizer RepresentedMsPacman_basic_translator  --decider cot_actor --prompt_level 1 --num_trails 1  --distiller traj_distiller --seed 0 --api_type aistudio --gpt_version ERNIE-Lite-8K --key_name $key_name "


)

# Run each task
for task in "${tasks[@]}"; do
  run_task "$task"
done

# Wait for all background tasks to complete
wait

echo "All tasks completed"
