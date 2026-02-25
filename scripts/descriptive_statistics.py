import pandas as pd
import os

# Set file path
INPUT_FILE = '../output/master_table.csv'


def calculate_stats():
    # Load the table
    if not os.path.exists(INPUT_FILE):
        print("Error: Run compile_master.py first to create the table!")
        return

    df = pd.read_csv(INPUT_FILE)

    # Calculate stats for Block Design Score
    mean_score = df['BlockDesignScore'].mean()
    sd_score = df['BlockDesignScore'].std()
    min_score = df['BlockDesignScore'].min()
    max_score = df['BlockDesignScore'].max()
    n_participants = len(df)

    print("DESCRIPTIVE STATISTICS")
    print(f"Number of Participants (N): {n_participants}")
    print(f"Mean Score (M): {mean_score:.2f}")
    print(f"Standard Deviation (SD): {sd_score:.2f}")
    print(f"Range: {min_score} - {max_score}")

    print("")
    print(f"A total of {n_participants} participants completed the study. "
          f"The assessment scores for the Block Design task ranged from {min_score} to {max_score}, "
          f"with a mean score of {mean_score:.2f} (SD = {sd_score:.2f}).")


if __name__ == "__main__":
    calculate_stats()