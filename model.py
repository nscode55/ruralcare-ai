import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import pickle

# Load data
df = pd.read_csv("dataset.csv")

X = df.drop("disease", axis=1)
y = df["disease"]

# Train model
model = DecisionTreeClassifier()
model.fit(X, y)

# Save model
pickle.dump(model, open("model.pkl", "wb"))