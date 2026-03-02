import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
from sklearn.linear_model import Ridge
from sklearn.model_selection import LeaveOneOut
from sklearn.metrics import mean_squared_error, r2_score
from scipy.stats import spearmanr

# Path Setup
FILE_PATH = os.path.join("..", "..", "output", "master_table.csv")
df = pd.read_csv(FILE_PATH)

# Define Features (X) and Target (y)
features = ['TotalTime', 'PathEfficiency', 'IdleRatio', 'Smoothness', 'RevisitRate']
X = df[features].values
y = df['BlockDesignScore'].values

# Initialize Ridge and LOSO
# alpha=1.0 is the standard starting point for regularization
l = LeaveOneOut()
model = Ridge(alpha=1.0)

y_true = []
y_pred = []

# LOSO Cross-Validation Loop
for train_index, test_index in l.split(X):
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]

    # Scale data
    from sklearn.preprocessing import StandardScaler

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    model.fit(X_train_scaled, y_train)
    y_pred.append(model.predict(X_test_scaled)[0])
    y_true.append(y_test[0])

# Performance Metrics
rmse = np.sqrt(mean_squared_error(y_true, y_pred))
rho, p_val = spearmanr(y_true, y_pred)
r2 = r2_score(y_true, y_pred)

# Adjusted R2
n = len(y_true)
k = len(features)
adj_r2 = 1 - ((1 - r2) * (n - 1) / (n - k - 1))

# Output Results
print("RIDGE REGRESSION PERFORMANCE (LOSO)")
print(f"RMSE: {rmse:.2f}")
print(f"Spearman rho: {rho:.2f} (p = {p_val:.3f})")
print(f"Adjusted R2: {adj_r2:.2f}")

# Scatter Plot
plt.figure(figsize=(7, 7))
plt.scatter(y_true, y_pred, color='pink', edgecolors='hotpink', s=100, label='LOSO Predictions')
# Add the 45-degree "Perfect Prediction" line
plt.plot([min(y_true), max(y_true)], [min(y_true), max(y_true)],
         color='purple', linestyle='--', label='Perfect Fit')

plt.xlabel("Actual Block Design Score")
plt.ylabel("Predicted Block Design Score")
plt.title("Ridge Model: Predicted vs. Actual Scores")
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig("../../output/plots/ridge_performance_scatter.png")
plt.show()