import pandas as pd
from scipy.stats import spearmanr

# Load your master table
df = pd.read_csv("../output/master_table.csv")

# Confirm the columns
print("Columns in master_table.csv:")
print(list(df.columns))

# Set the exact column names in master table
BLOCK_COL = "BlockDesignScore"
TIME_COL = "TotalTime"

# Safety checks
if BLOCK_COL not in df.columns:
    raise ValueError(f"Missing column: {BLOCK_COL}. Check spelling in your CSV columns list.")
if TIME_COL not in df.columns:
    raise ValueError(f"Missing column: {TIME_COL}. Check spelling in your CSV columns list.")

# Convert both columns to numbers
df[BLOCK_COL] = pd.to_numeric(df[BLOCK_COL], errors="coerce")
df[TIME_COL] = pd.to_numeric(df[TIME_COL], errors="coerce")

# Keep only rows with both values present
clean = df[[BLOCK_COL, TIME_COL]].dropna()

# Run Spearman correlation
rho, p_value = spearmanr(clean[BLOCK_COL], clean[TIME_COL])

# Print results
print("\nSPEARMAN CORRELATION RESULTS")
print("N =", len(clean))
print("rho =", round(rho, 3))
print("p-value =", p_value)

# APA-friendly formatting (rho to 2 decimals, p formatted properly)
rho_apa = f"{rho:.2f}"
if p_value < 0.001:
    p_apa = "< .001"
else:
    p_apa = f"= {p_value:.3f}".replace("0.", ".")

direction = "negative" if rho < 0 else "positive"

# Format rho and p for APA
rho_apa = f"{rho:.2f}"

# Decide significance
if p_value < 0.05:
    significance_sentence = "The correlation was statistically significant."
else:
    significance_sentence = "The correlation was not statistically significant."

# Create APA paragraph
apa_paragraph = (
    "A Spearman rank-order correlation was conducted to examine the association between "
    "Block Design scores and total recipe completion time. "
    f"The correlation was rho = {rho_apa}, p {p_apa}. "
    f"{significance_sentence}"
)

print("\nAPA paragraph:")
print(apa_paragraph)