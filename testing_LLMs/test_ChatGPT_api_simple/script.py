import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load the dataset from CSV
df = pd.read_csv('/app/regression_dataset.csv')

# Split the dataset into features and target variable
X = df.iloc[:, :-1]
y = df.iloc[:, -1]

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and fit the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict on the test set
y_pred = model.predict(X_test)

# Save the results to a text file
with open('/app/results.txt', 'w') as file:
    file.write('Predicted\tActual\n')
    for pred, actual in zip(y_pred, y_test):
        file.write(f'{pred}\t{actual}\n')