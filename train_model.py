import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
import pickle

print("Loading dataset...")
try:
    df = pd.read_csv("instagram_reach_data.csv", encoding='latin1')
    print(f"Loaded {len(df)} rows.")
except:
    print("ERROR: File not found.")
    exit()

# Features
features = ['Followers', 'Likes', 'Comments', 'Post_Hour', 'Day_Of_Week']
target = 'Reach'

df = df.dropna(subset=features + [target])

X = df[features]
y = df[target]

# training
print(f"Training model on {len(df)} rows...")
xtrain, xtest, ytrain, ytest = train_test_split(X, y, test_size=0.2, random_state=42)

# Gradient Boosting 
model = GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, random_state=42)
model.fit(xtrain, ytrain)

score = model.score(xtest, ytest)
print(f"Model Accuracy (R²): {score:.2f}")

pickle.dump(model, open('model.pkl', 'wb'))
print("Saved 'model.pkl'")