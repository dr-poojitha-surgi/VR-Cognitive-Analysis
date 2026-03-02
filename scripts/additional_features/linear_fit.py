import pandas as pd
import numpy as np

# Load the dataset
df = pd.read_csv("../../output/master_table.csv")

# List the four additional features
features = [
    "PathEfficiency",
    "IdleRatio",
    "Smoothness",
    "RevisitRate"
]

# Loop through each feature
for feature in features:

    print("===================================")
    print("Linear fit for:", feature)

    # Remove missing values
    clean = df[[feature, "BlockDesignScore"]].dropna()

    x = clean[feature]
    y = clean["BlockDesignScore"]

    # Compute linear fit
    slope, intercept = np.polyfit(x, y, 1)

    # Print results
    print("Slope:", round(slope, 4))
    print("Intercept:", round(intercept, 4))

    print("Equation:")
    print("BlockDesignScore =", round(slope,4), "*", feature, "+", round(intercept,4))
    print("\n")