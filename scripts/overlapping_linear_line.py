import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load your master table
df = pd.read_csv("../output/master_table.csv")

# Define columns
TIME_COL = "TotalTime"
BLOCK_COL = "BlockDesignScore"

# Remove missing values
clean = df[[TIME_COL, BLOCK_COL]].dropna()

x = clean[TIME_COL]
y = clean[BLOCK_COL]

# Compute linear fit
slope, intercept = np.polyfit(x, y, 1)

# Create predicted line values
line = slope * x + intercept

# Plot
plt.figure()

# Scatter plot
plt.scatter(x, y, color='pink', s=100, edgecolors='hotpink')

# Linear fit line
plt.plot(x, line, color='purple', linewidth=2)

plt.xlabel("Total Completion Time (seconds)")
plt.ylabel("Block Design Score")
plt.title("Total Completion Time vs Block Design Score")

plt.show()