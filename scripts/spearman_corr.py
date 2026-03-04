import pandas as pd
import scipy.stats as stats

# Load the dataset
df = pd.read_csv('../output/master_table.csv')

# Spearman correlation between BlockDesignScore and TotalTime
rho, p_value = stats.spearmanr(df['BlockDesignScore'], df['TotalTime'])

print("Spearman's correlation:")
print("N =", len(df))
print("rho =", round(rho, 2))
print("p-value =", round(p_value, 3))

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
    f"Total Time and Block Design scores. The correlation was {direction}, "
    f"ρ = {rho:.2f}, {p_text}, based on N = {len(df)} participants. "
    f"{significance}"
)

print("\nAPA paragraph:")
print(apa_paragraph)
print("\n")