import pickle
import json
import random


# Load trained model
model = pickle.load(open("app/ml/model.pkl", "rb"))

# Load vectorizer
vectorizer = pickle.load(open("app/ml/vectorizer.pkl", "rb"))

# Load dataset
with open("app/ml/dataset/intents.json") as file:
    data = json.load(file)


def predict_response(user_input: str):

    # Convert user text to vector
    X = vectorizer.transform([user_input])

    # Predict intent
    prediction = model.predict(X)[0]

    # Confidence score
    probability = max(model.predict_proba(X)[0])

    # If confidence too low
    if probability < 0.65:
        return "I'm not sure I understood that. Could you please rephrase?"

    # Find response
    for intent in data["intents"]:
        if intent["tag"] == prediction:
            return random.choice(intent["responses"])

    return "Sorry, something went wrong."