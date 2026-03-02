import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np
from scipy import stats

# Setup the path
FILE_PATH = os.path.join("..", "..", "output", "master_table.csv")
OUTPUT_FOLDER = "../../output/plots/"

if not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)

# Define the 4 proposed features
features = ['PathEfficiency', 'IdleRatio', 'Smoothness', 'RevisitRate']


def create_linear_fit_plots():
    if not os.path.exists(FILE_PATH):
        print(f"Error: Could not find master_table.csv at {FILE_PATH}")
        return

    df = pd.read_csv(FILE_PATH)
    y_axis = df['BlockDesignScore']

    for feat in features:
        if feat not in df.columns:
            print(f"Skipping {feat}: Not found in CSV.")
            continue

        x_axis = df[feat]

        # Compute Linear Fit (Step 5 of the analysis)
        # slope (m), intercept (b)
        slope, intercept, r_val, p_val, std_err = stats.linregress(x_axis, y_axis)

        # Calculate the line coordinates: y = mx + b
        line = slope * x_axis + intercept

        # Create the Combined Plot
        plt.figure(figsize=(8, 5))


        plt.scatter(x_axis, y_axis,
                    color='pink',
                    edgecolors='hotpink',
                    s=120,
                    alpha=0.8,
                    label='Participants')

        # Linear Line
        plt.plot(x_axis, line,
                 color='purple',
                 linewidth=2.5,
                 label=f'Linear Fit (R² = {r_val ** 2:.2f})')

        # Formatting
        plt.title(f'Linear Analysis: {feat} vs. Block Design')
        plt.xlabel(f'{feat} (VR Metric)')
        plt.ylabel('Block Design Score')
        plt.legend(loc='best')
        plt.grid(True, linestyle=':', alpha=0.4)

        # Save the plot
        file_name = f"{feat}_linear_fit.png"
        plt.savefig(os.path.join(OUTPUT_FOLDER, file_name))
        print(f"Generated Plot with Linear Fit: {file_name}")

        plt.close()


if __name__ == "__main__":
    create_linear_fit_plots()