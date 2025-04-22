import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
import joblib

# Step 1: Load the CSV file
try:
    # Since the file uses tabs to separate columns, specify sep='\t'
    data = pd.read_csv('spam.csv', encoding='ISO-8859-1', sep='\t', on_bad_lines='skip')
    print("Data loaded successfully")
except Exception as e:
    print(f"Error loading CSV: {e}")

# Step 2: Check the columns and structure of the data
print(data.head())

# Step 3: Ensure columns are correctly labeled
# Assigning correct column names
data.columns = ['label', 'message']

# Step 4: Preprocessing the data
# Map 'ham' to 0 and 'spam' to 1
data['label'] = data['label'].map({'ham': 0, 'spam': 1})

# Step 5: Split data into features and labels
X = data['message']
y = data['label']

# Step 6: Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 7: Create a pipeline with CountVectorizer and Multinomial Naive Bayes
model = make_pipeline(CountVectorizer(), MultinomialNB())

# Step 8: Train the model
model.fit(X_train, y_train)

# Step 9: Evaluate the model
accuracy = model.score(X_test, y_test)
print(f"Model Accuracy: {accuracy * 100:.2f}%")

# Step 10: Save the trained model for later use
joblib.dump(model, 'spam_model.pkl')

# You can now use this model for predictions on new email messages.
