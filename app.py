from flask import Flask, render_template, request
import joblib

# Load the pre-trained spam detection model
try:
    model = joblib.load('spam_model.pkl')
    print("Model loaded successfully!")
except Exception as e:
    print(f"Error loading the model: {e}")

# Initialize Flask app
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', prediction=None, email_text=None)

@app.route('/predict', methods=['POST'])
def predict():
    email_text = request.form['email_text']
    
    # Check if email_text is correctly received
    print(f"Received email text: {email_text[:100]}...")  # Print first 100 characters to confirm
    
    # Make prediction
    try:
        prediction = model.predict([email_text])[0]
        print(f"Prediction: {prediction}")
    except Exception as e:
        print(f"Error during prediction: {e}")
        prediction = None

    # Prepare result
    if prediction is not None:
        result = "This email is NOT SPAM." if prediction == 0 else "This email is SPAM."
    else:
        result = "Error in making the prediction."
    
    return render_template('index.html', prediction=result, email_text=email_text)

if __name__ == '__main__':
    app.run(debug=True)
