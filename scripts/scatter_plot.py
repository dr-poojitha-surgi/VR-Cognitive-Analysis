import pandas as pd
import matplotlib.pyplot as plt

# Load master table
df = pd.read_csv("../output/master_table.csv")

# Column names from your file
x_col = "TotalTime"
y_col = "BlockDesignScore"

# Convert to numeric
df[x_col] = pd.to_numeric(df[x_col], errors="coerce")
df[y_col] = pd.to_numeric(df[y_col], errors="coerce")

# Remove missing values
clean = df[[x_col, y_col]].dropna()

# Create scatter plot
plt.figure()
plt.scatter(clean[x_col], clean[y_col])

plt.xlabel("Total Completion Time (seconds)")
plt.ylabel("Block Design Score")
plt.title("Total Completion Time vs Block Design Score")

plt.show()