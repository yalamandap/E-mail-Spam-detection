✉️ **Email Spam Detection**
A web-based machine learning app that classifies emails as spam or ham (not spam). Built with Python, Flask, and a trained spam detection model, it provides an interactive UI for real-time predictions with a clean and responsive design featuring light and dark themes, social media links, and enhanced UX.

## Live Demo

Check out the live app here: [Spam Email Detector on Render](https://e-mail-spam-detection-wsao.onrender.com)


🗂️ **Project Structure**

```
email-spam-detection/
├── app.py               # Flask web app
├── train_model.py       # Model training script
├── test.py              # Model testing script
├── spam.csv             # Dataset used for training
├── spam_model.pkl       # Trained and serialized ML model
├── requirements.txt     # Project dependencies
├── static/              # Static files for frontend (CSS, JS, images)
│   ├── css/
│   │   └── styles.css   # Custom stylesheet
│   └── js/
│       └── scripts.js   # JavaScript for interactivity
├── templates/
│   └── index.html       # Frontend UI for predictions
└── README.md            # Project documentation
```

🚀 **Getting Started**

1. Clone the Repository

```bash
git clone https://github.com/yourusername/email-spam-detection.git
cd email-spam-detection
```

2. Create & Activate Virtual Environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate
```

3. Install Dependencies

```bash
pip install -r requirements.txt
```

4. Train the Model (only if spam\_model.pkl doesn't exist)

```bash
python train_model.py
```

5. Run the Web App

```bash
python app.py
```

Then open your browser and go to 👉 [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

💡 **How It Works**

* Uses the SMS Spam Collection Dataset for training.
* Text is preprocessed and vectorized.
* A machine learning model predicts if the input is spam or ham.
* Results are shown on a simple web interface using index.html.

✅ **Features**

* 📬 Web-based spam email detector
* 🎨 Clean UI with light/dark theme toggle
* 🔄 Easy retraining with new data
* ⚡ Fast, lightweight, and easy to use


📸 **Screenshot**
*(Add your app screenshot here)*

🚀 Deployment Steps
This project is deployed on Render — a simple and free platform for hosting web apps.

How to deploy this app on Render:

Push your project to GitHub
Make sure your code (including app.py, requirements.txt, templates/, and static/ folders) is pushed to a GitHub repository.

Create a new Web Service on Render

Go to Render dashboard and create a new Web Service.

Connect your GitHub repository containing this project.

Select the branch (e.g., main) to deploy from.

Configure build and start commands

Build Command:

bash
Copy
Edit
pip install -r requirements.txt
Start Command:

bash
Copy
Edit
gunicorn app:app
Set instance type

Choose the free instance for testing or paid instances for production use.

Deploy

Click "Create Web Service" and Render will automatically build and deploy your app.

After a few minutes, your app will be live on a Render URL.

Access your live app

Visit the URL Render provides (e.g., https://your-app-name.onrender.com) to see your deployed spam detection app.



📦 **Future Improvements**

* 📧 Add email validation and formatting
* 🔌 Create REST API endpoints for external integration
* 🧠 Experiment with deep learning models (e.g., LSTM, BERT)
* 🐳 Dockerize for easier deployment

🤝 **Contributing**
Contributions are welcome! Open issues, suggest features, or submit pull requests.

📜 **License**
This project is licensed under the MIT License.

🙌 **Acknowledgments**

* UCI SMS Spam Collection Dataset
* Flask, Scikit-learn, NLTK

---


