import os
import pandas as pd

# Path to folder where your CompletedStepsData files are stored
DATA_FOLDER = '../data/'

results = []

for file in os.listdir(DATA_FOLDER):
    if "CompletedStepsData.csv" in file:
        file_path = os.path.join(DATA_FOLDER, file)

        df = pd.read_csv(file_path)

        # Subject ID from filename (e.g., C008_SimpleStew_CompletedStepsData.csv)
        subject = file.split("_")[0]

        # The final Session Time value is the total completion time
        total_time = df["Session Time"].max()

        results.append([subject, total_time])

# Create clean table
total_time_df = pd.DataFrame(results, columns=["Subject", "Total_Completion_Time"])
total_time_df = total_time_df.sort_values("Subject")

print("\nTotal Recipe Completion Time for Each Participant:")
print(total_time_df.to_string(index=False))