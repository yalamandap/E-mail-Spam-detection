from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# Load the pre-trained spam detection model
try:
    model = joblib.load('spam_model.pkl')
    print("Model loaded successfully!")
except Exception as e:
    print(f"Error loading the model: {e}")

@app.route('/')
def home():
    return render_template('index.html', prediction=None, email_text=None)

@app.route('/predict', methods=['POST'])
def predict():
    email_text = request.form.get('email_text', '')
    
    print(f"Received email text: {email_text[:100]}...")  # For debugging
    
    try:
        prediction_label = model.predict([email_text])[0]
        print(f"Prediction: {prediction_label}")
    except Exception as e:
        print(f"Error during prediction: {e}")
        prediction_label = None

    if prediction_label is not None:
        # Assuming your model outputs 0 for ham (not spam), 1 for spam
        result = "This email is NOT SPAM." if prediction_label == 0 else "This email is SPAM."
    else:
        result = "Error in making the prediction."

    return render_template('index.html', prediction=result, email_text=email_text)

if __name__ == '__main__':
    app.run(debug=True)
