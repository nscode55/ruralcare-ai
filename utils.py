import pickle

model = pickle.load(open("model.pkl", "rb"))

def predict(symptoms):
    prediction = model.predict([symptoms])
    return prediction[0]

def get_recommendation(disease):
    recommendations = {
        "Flu": "Rest and stay hydrated.",
        "Dengue": "Consult a doctor immediately.",
        "Cold": "Take rest and fluids.",
        "Covid": "Isolate and seek medical advice.",
        "Migraine": "Take rest and avoid stress."
    }
    return recommendations.get(disease, "Consult a doctor.")