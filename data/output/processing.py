import pandas as pd
import glob
import os

# Create output folder
os.makedirs("output", exist_ok=True)

# Load CSVs
files = glob.glob("data/*.csv")
dfs = [pd.read_csv(f) for f in files]
df = pd.concat(dfs, ignore_index=True)

# Filter Pink Morsels
df = df[df['product'] == 'pink morsel']

# Calculate sales
df['sales'] = df['quantity'] * df['price']

# Keep only required columns
final_df = df[['sales', 'date', 'region']]

# Save output file
final_df.to_csv("output/combined_sales.csv", index=False)

print("File saved successfully!")