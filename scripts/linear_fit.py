import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("../output/master_table.csv")

x_col = "TotalTime"
y_col = "BlockDesignScore"

# Convert to numeric
df[x_col] = pd.to_numeric(df[x_col], errors="coerce")
df[y_col] = pd.to_numeric(df[y_col], errors="coerce")

# Remove missing values
clean = df[[x_col, y_col]].dropna()

x = clean[x_col]
y = clean[y_col]

# Compute Linear Fit
slope, intercept = np.polyfit(x, y, 1)

print("Linear Fit Equation:")
print(f"BlockDesignScore = {slope:.4f} * TotalTime + {intercept:.4f}")