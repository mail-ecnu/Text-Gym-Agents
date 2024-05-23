import gym
import numpy as np
import imageio

def save_frames_as_gif(frames, filename='pong_gameplay.gif'):
    """Function to save a list of frames as a gif."""
    with imageio.get_writer(filename, mode='I', duration=0.02) as writer:
        for frame in frames:
            writer.append_data(frame)

def main():
    # Create the Pong-v4 environment
    env = gym.make('Pong-v4', render_mode='rgb_array')
    env.reset()
    frames = []

    for _ in range(1000):  # run for more or fewer frames if you like
        # Render to rgb_array and store frames
        frame = env.render()
        frames.append(frame)
        
        # Take a random action
        action = env.action_space.sample()
        _, _, done,_,  _ = env.step(action)

        if done:
            break

    env.close()

    # Save the frames as a gif
    save_frames_as_gif(frames)

if __name__ == '__main__':
    main()