import os

model_path = os.path.join("artifacts", "model.pkl")
preprocessor_path = os.path.join("artifacts", "preprocessor.pkl")

if not os.path.exists(model_path):
    print(f"Model file not found at {model_path}")
if not os.path.exists(preprocessor_path):
    print(f"Preprocessor file not found at {preprocessor_path}")
