import pandas as pd
from scipy.stats import spearmanr

# Load the master table
df = pd.read_csv("../../output/master_table.csv")

print("Columns in dataset:")
print(df.columns)
print("\n")

# Define the four additional features
additional_features = [
    "PathEfficiency",
    "IdleRatio",
    "Smoothness",
    "RevisitRate"
]

print("Four additional features we will analyze:")
for feature in additional_features:
    print("-", feature)

print("\n")

# Run Spearman correlation for each feature

outcome_variable = "BlockDesignScore"

for feature in additional_features:

    print("--------------------------------------------------")
    print("Analyzing:", feature)

    # Convert columns to numeric
    df[feature] = pd.to_numeric(df[feature], errors="coerce")
    df[outcome_variable] = pd.to_numeric(df[outcome_variable], errors="coerce")

    # Remove missing values
    clean_data = df[[feature, outcome_variable]].dropna()

    # Compute Spearman correlation
    rho, p_value = spearmanr(clean_data[feature], clean_data[outcome_variable])

    print("N =", len(clean_data))
    print("rho =", round(rho, 2))
    print("p-value =", round(p_value, 3))

    # ------------------------------------------------
    # APA Formatting
    # ------------------------------------------------

    # Format p-value correctly
    if p_value < 0.001:
        p_text = "p < .001"
    else:
        p_text = "p = " + f"{p_value:.3f}".replace("0.", ".")

    # Determine direction
    if rho > 0:
        direction = "positive"
    elif rho < 0:
        direction = "negative"
    else:
        direction = "no"

    # Determine significance
    if p_value < 0.05:
        significance = "The correlation was statistically significant."
    else:
        significance = "The correlation was not statistically significant."

    # APA paragraph
    apa_paragraph = (
        f"A Spearman rank-order correlation was conducted to examine the association between "
        f"{feature} and Block Design scores. The correlation was {direction}, "
        f"ρ = {rho:.2f}, {p_text}, based on N = {len(clean_data)} participants. "
        f"{significance}"
    )

    print("\nAPA paragraph:")
    print(apa_paragraph)
    print("\n")