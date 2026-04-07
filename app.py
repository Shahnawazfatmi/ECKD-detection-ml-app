from flask import Flask, render_template, request
import joblib
import numpy as np

# -------------------------------
# Initialize Flask App
# -------------------------------
app = Flask(__name__)

# -------------------------------
# Load Model & Features Safely
# -------------------------------
try:
    model = joblib.load("ckd_model.pkl")
    features = joblib.load("features.pkl")
except Exception as e:
    print("❌ Error loading model or features:", e)
    model = None
    features = None


# -------------------------------
# Home Page
# -------------------------------
@app.route('/')
def home():
    return render_template('index.html')


# -------------------------------
# About Page
# -------------------------------
@app.route('/about')
def about():
    return render_template('about.html')


# -------------------------------
# Prediction Route
# -------------------------------
@app.route('/predict', methods=['POST'])
def predict():

    # Check model loaded
    if model is None or features is None:
        return "Model not loaded properly. Please check server."

    try:
        input_data = []

        # Collect input safely
        for feature in features:
            value = request.form.get(feature)

            if value is None or value.strip() == "":
                return f"⚠️ Missing value for: {feature}"

            try:
                value = float(value)
            except:
                return f"⚠️ Invalid input for: {feature}"

            input_data.append(value)

        # Convert to numpy array
        input_array = np.array(input_data).reshape(1, -1)

        # Prediction
        prediction = int(model.predict(input_array)[0])

        # Probability handling
        if hasattr(model, "predict_proba"):
            probability = model.predict_proba(input_array)[0][1]
            probability = round(probability * 100, 2)
        else:
            probability = None

        # Risk level logic
        if probability is not None:
            if probability >= 75:
                risk_level = "High"
            elif probability >= 40:
                risk_level = "Moderate"
            else:
                risk_level = "Low"
        else:
            risk_level = "Unknown"

        # Result & Suggestions
        if prediction == 1:
            result = "⚠️ Early CKD Risk Detected"
            suggestions = [
                "Consult a nephrologist",
                "Get kidney function tests (Creatinine, eGFR)",
                "Monitor blood pressure regularly",
                "Control blood sugar levels",
                "Reduce salt intake",
                "Follow a kidney-friendly diet"
            ]
        else:
            result = "✅ No Significant CKD Risk Detected"
            suggestions = [
                "Maintain a healthy lifestyle",
                "Regular health checkups",
                "Monitor blood pressure and sugar levels"
            ]

        return render_template(
            'result.html',
            result=result,
            risk_score=probability,
            risk_level=risk_level,
            suggestions=suggestions
        )

    except Exception as e:
        return f"❌ Unexpected error: {str(e)}"


# -------------------------------
# Global Error Handling
# -------------------------------
@app.errorhandler(404)
def not_found(e):
    return "<h3>❌ Page not found</h3><a href='/'>Go Home</a>", 404


@app.errorhandler(500)
def server_error(e):
    return "<h3>❌ Internal Server Error</h3><a href='/'>Go Home</a>", 500


# -------------------------------
# Run App
# -------------------------------
if __name__ == "__main__":
    app.run(debug=True)