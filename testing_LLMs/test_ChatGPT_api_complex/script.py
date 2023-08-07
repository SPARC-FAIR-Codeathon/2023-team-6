
import pandas as pd
from sklearn.linear_model import LinearRegression

# Load the data
data = pd.read_csv('data/datafile.csv')

# Split the data into features and target
X = data.drop('y', axis=1)
y = data['y']

# Train a linear regression model
model = LinearRegression()
model.fit(X, y)

# Make predictions
predictions = model.predict(X)

# Save the results
results = pd.DataFrame({'Predicted': predictions})
results.to_csv('results/results.txt', index=False)

# Record package versions
import subprocess
with open("requirements.txt", "w") as f:
    subprocess.run(["pip", "freeze"], stdout=f)