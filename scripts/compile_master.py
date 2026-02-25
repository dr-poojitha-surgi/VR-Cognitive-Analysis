import pandas as pd
import numpy as np
import os

DATA_FOLDER = '../data/'
OUTPUT_FOLDER = '../output/'


def extract_features():
    print("Starting data compilation...")

    # Load the scores
    try:
        assessments = pd.read_excel(os.path.join(DATA_FOLDER, 'Assessments.xlsx'))
        assessments = assessments[["TOPF\nSubject ID", "Block Design Score"]]
        assessments.columns = ['SubjectID', 'Score']
    except FileNotFoundError:
        print("Error: Could not find Assessments.xlsx in the data folder!")
        return
    except KeyError:
        print("Error: Could not find columns 'Subject ID' or 'Block Design Score'. Check your Excel headers!")
        return

    master_rows = []

    # 2. The Loop: Visit every person in the list
    for index, row in assessments.iterrows():
        id = row['SubjectID']
        score = row['Score']

        # Define the file names for this specific person
        steps_file = os.path.join(DATA_FOLDER, f"{id}_SimpleStew_CompletedStepsData.csv")
        move_file = os.path.join(DATA_FOLDER, f"{id}_SimpleStew_MovementData.csv")

        # Create a dictionary to hold this person's results
        person_stats = {'SubjectID': id, 'BlockDesignScore': score}

        # Check if the person has basic VR data
        if os.path.exists(steps_file):
            df_steps = pd.read_csv(steps_file)
            person_stats['TotalTime'] = df_steps['Session Time'].max()
        else:
            print(f"Skipping {id}: No basic VR data found.")
            continue

        # Check if they have the big Movement data for our "Best Four" features
        if os.path.exists(move_file):
                df_move = pd.read_csv(move_file)

                # Get coordinates and time
                x = df_move['MotionControllerRight_LOCATION_X'].values
                y = df_move['MotionControllerRight_LOCATION_Y'].values
                z = df_move['MotionControllerRight_LOCATION_Z'].values
                t = df_move['Times'].values

                # Distance and Velocity calculation
                dist_steps = np.sqrt(np.diff(x) ** 2 + np.diff(y) ** 2 + np.diff(z) ** 2)
                dt = np.diff(t)
                vel = np.divide(dist_steps, dt, out=np.zeros_like(dist_steps), where=dt != 0)

                # FEATURE 1: Path Efficiency
                total_dist = np.sum(dist_steps)
                start_to_end = np.sqrt((x[-1] - x[0]) ** 2 + (y[-1] - y[0]) ** 2 + (z[-1] - z[0]) ** 2)
                person_stats['PathEfficiency'] = start_to_end / total_dist if total_dist > 0 else 0

                # FEATURE 2: Idle Ratio (Hesitation)
                idle_mask = vel < 0.05
                person_stats['IdleRatio'] = np.sum(dt[idle_mask]) / (t[-1] - t[0]) if (t[-1] - t[0]) > 0 else 0

                # FEATURE 3: Smoothness (Velocity Variance)
                person_stats['Smoothness'] = np.std(vel)

                # FEATURE 4: Revisit Rate (Memory)
                grid_size = 50
                zones = list(zip(x // grid_size, y // grid_size))
                person_stats['RevisitRate'] = len(set(zones)) / len(zones) if len(zones) > 0 else 0

                master_rows.append(person_stats)
                print(f"Successfully processed {id}")

        # Save the results
        final_df = pd.DataFrame(master_rows)

        # Ensure output folder exists
        if not os.path.exists(OUTPUT_FOLDER):
            os.makedirs(OUTPUT_FOLDER)

        final_df.to_csv(os.path.join(OUTPUT_FOLDER, 'master_table.csv'), index=False)
        print("\nSUCCESS! Master dataset saved in the 'output' folder.")
        print(final_df.head())

if __name__ == "__main__":
    extract_features()