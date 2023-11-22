import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV data
data = pd.read_csv("performance_data.csv")

# Group games by type
game_types = {
    "Classic Control": ["Acrobot-v1", "CartPole-v0", "MountainCar-v0"],
    "Box 2D": ["LunarLander-v2"],
    "Toy Text": ["Taxi-v3", "CliffWalking-v0", "Blackjack-v1"]
}

for game_type, games in game_types.items():
    fig, axs = plt.subplots(1, len(games), figsize=(12 * len(games), 6))
    fig.suptitle(f"Performance Plot: {game_type}", fontsize=28, fontname="Times New Roman")

    if len(games) == 1:
        axs = [axs]

    handles, labels = [], []

    for idx, game in enumerate(games):
        # Filter data to get information for the current game (in the loop)
        game_data = data[data["game"] == game]

        axs[idx].set_title(game, fontsize=20, fontname="Times New Roman")
        axs[idx].set_xlabel("Levels", fontsize=16, fontname="Times New Roman")
        if idx == 0:
            axs[idx].set_ylabel("Scores", fontsize=16, fontname="Times New Roman")

        for index, row in game_data.iterrows():
            decider_name = row["decider_name"]
            levels = ["l1", "l2", "l3", "l4", "l5"]
            scores = row[levels].values.tolist()
            lines = axs[idx].plot(levels, scores, "-o", label=decider_name)
            # Grab the handle and label for creating a global legend
            handles.append(lines[0])
            labels.append(decider_name)

    # Eliminate duplicate labels and handles
    unique_labels = []
    unique_handles = []
    for handle, label in zip(handles, labels):
        if label not in unique_labels:
            unique_labels.append(label)
            unique_handles.append(handle)

    # Add a legend at the bottom middle of the figure
    fig.legend(
        unique_handles,
        unique_labels,
        loc="lower center",
        ncol=4, prop={'size': 18}
    )

    # Adjust layout to accommodate the legend and prevent cropping

    plt.savefig("./vis/" + game_type + ".png", dpi=300)
