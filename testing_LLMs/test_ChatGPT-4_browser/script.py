import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import sys
import argparse

def main(data_file):
    # Load dataset
    data = pd.read_csv(data_file)

    # Split the dataset into features and target variable
    X = data.drop(columns=['y'])
    y = data['y']

    # Create a linear regression model
    model = LinearRegression()

    # Fit the model
    model.fit(X, y)

    # Predict the target variable
    y_pred = model.predict(X)

    # Calculate mean squared error
    mse = mean_squared_error(y, y_pred)

    with open("results.txt", "w") as f:
        f.write(f"Mean Squared Error: {mse}\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run regression analysis on the dataset.")
    parser.add_argument("--data_file", type=str, required=True, help="Path to the dataset file")
    args = parser.parse_args()

    main(args.data_file)
