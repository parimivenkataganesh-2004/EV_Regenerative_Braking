import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Load dataset
data = pd.read_csv("dataset.csv")

# Three input parameters
X = data[["Speed", "Battery", "Brake"]]

# Output
y = data["Regeneration"]

# -----------------------------
# STEP 1: Test model accuracy
# -----------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

test_model = DecisionTreeClassifier(random_state=42)

test_model.fit(X_train, y_train)

y_pred = test_model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("AI Model Evaluation")
print("-------------------")
print("Accuracy:", accuracy * 100, "%")

print("\nFeature Importance:")
print("Speed:", test_model.feature_importances_[0])
print("Battery:", test_model.feature_importances_[1])
print("Brake:", test_model.feature_importances_[2])

# --------------------------------
# STEP 2: Train final model
# --------------------------------

final_model = DecisionTreeClassifier(random_state=42)

final_model.fit(X, y)

# Save final model
joblib.dump(final_model, "regen_model.pkl")

print("\nFinal AI Model trained using all 810 examples.")
print("AI Model Saved as regen_model.pkl")