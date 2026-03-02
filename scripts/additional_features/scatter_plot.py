import pandas as pd
import matplotlib.pyplot as plt
import os

# Setup the paths
FILE_PATH = os.path.join("..", "..", "output", "master_table.csv")
OUTPUT_FOLDER = "../../output/plots/"

if not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)

# Define the 4 features you are proposing
features = ['PathEfficiency', 'IdleRatio', 'Smoothness', 'RevisitRate']


def create_proposed_scatters():
    if not os.path.exists(FILE_PATH):
        print(f"Error: Could not find master_table.csv at {FILE_PATH}")
        return

    df = pd.read_csv(FILE_PATH)
    y_axis = df['BlockDesignScore']

    for feat in features:
        if feat not in df.columns:
            print(f"Skipping {feat}: Check your column names in master_table.csv")
            continue

        x_axis = df[feat]

        # Create the Plot
        plt.figure(figsize=(8, 5))


        plt.scatter(x_axis, y_axis,
                    color='pink',
                    edgecolors='hotpink',
                    s=120,
                    alpha=0.8)

        # Formatting
        plt.title(f'Proposed Feature: {feat} vs. Cognitive Score')
        plt.xlabel(f'{feat} (VR Metric)')
        plt.ylabel('Block Design Score')
        plt.grid(True, linestyle='--', alpha=0.3)

        # Save the plot
        file_name = f"{feat}_scatter.png"
        plt.savefig(os.path.join(OUTPUT_FOLDER, file_name))
        print(f"Successfully created: {file_name}")

        plt.close()


if __name__ == "__main__":
    create_proposed_scatters()