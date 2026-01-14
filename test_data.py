import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# CHANGE THIS to the name of the new file you found!
file_name = "new_dataset.csv" 

print(f"🕵️ Inspecting {file_name}...")
try:
    df = pd.read_csv(file_name, encoding='latin1')
except:
    print("❌ File not found.")
    exit()

# 1. Check for the Holy Grail columns
# We need 'Followers' (Context) and 'Reach' (Target)
cols_to_check = ['followers', 'follower_count', 'likes', 'comments', 'reach', 'impressions']
found_cols = [c for c in df.columns if any(x in c.lower() for x in cols_to_check)]

print(f"✅ Found Columns: {found_cols}")

# 2. Check Correlation (The Signal Strength)
# We want to see if Likes/Followers actually predict Reach in this file.
if len(found_cols) > 2:
    # Filter only numeric columns
    numeric_df = df.select_dtypes(include=['float64', 'int64'])
    corr = numeric_df.corr()
    
    # Check if we have a target to compare against
    target = next((c for c in numeric_df.columns if 'reach' in c.lower() or 'impression' in c.lower()), None)
    
    if target:
        print(f"\n📊 Correlation with '{target}':")
        print(corr[target].sort_values(ascending=False))
        
        # VERDICT
        best_score = corr[target].drop(target).max()
        if best_score > 0.6:
            print("\n🎉 VERDICT: GREAT DATASET! (Strong Signal)")
        elif best_score > 0.4:
            print("\n🤔 VERDICT: OKAY DATASET. (Might need Log Transform)")
        else:
            print("\n🗑️ VERDICT: JUNK DATA. (Too noisy, delete it)")
    else:
        print("\n❌ No 'Reach' or 'Impressions' column found to predict!")
else:
    print("\n❌ Missing key columns (Likes/Followers/Reach).")