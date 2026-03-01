import pandas as pd

# Load ABRicate output
file_path = "../data/all_results.txt"

# Read tab-separated file
df = pd.read_csv(file_path, sep="\t")

# Extract isolate name from #FILE column
df["Isolate"] = df["#FILE"].apply(lambda x: x.split("/")[0])

# Define carbapenemase genes
carb_genes = ["blaNDM", "blaOXA-181", "blaOXA-232", "blaOXA-48", "blaKPC"]

# Filter carbapenemase genes
carb_df = df[df["GENE"].str.contains("|".join(carb_genes), na=False)]

# Save filtered results
carb_df.to_csv("../results/carbapenemase_filtered.csv", index=False)

# Calculate prevalence
total_isolates = df["Isolate"].nunique()
ndm_count = carb_df[carb_df["GENE"].str.contains("blaNDM")]["Isolate"].nunique()
oxa_count = carb_df[carb_df["GENE"].str.contains("blaOXA")]["Isolate"].nunique()
kpc_count = carb_df[carb_df["GENE"].str.contains("blaKPC")]["Isolate"].nunique()

print("Total isolates:", total_isolates)
print("blaNDM isolates:", ndm_count)
print("OXA-48-like isolates:", oxa_count)
print("blaKPC isolates:", kpc_count)
