import pandas as pd

# Create a sample dataset
data = {
    'label': ['ham', 'spam', 'ham', 'spam'],
    'message': [
        'Hello, how are you?',  # ham message
        'You won a lottery! Click here to claim your prize.',  # spam message
        "Let's meet tomorrow.",  # ham message
        'Get cheap medications online now!'  # spam message
    ]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
df.to_csv('spam.csv', index=False)

print("spam.csv file created!")
