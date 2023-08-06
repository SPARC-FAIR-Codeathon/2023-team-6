from sklearn.datasets import make_regression
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set aesthetics for seaborn
sns.set_style("whitegrid")

# Number of samples
N = 1000

# Generate the dataset
X, y, coef = make_regression(n_samples=N, n_features=5, noise=0.1, coef=True)

# Convert the dataset to a pandas DataFrame for easier visualization
feature_names = [f'X{i+1}' for i in range(X.shape[1])]
data = pd.DataFrame(X, columns=feature_names)
data['y'] = y

# Save data to CSV
data.to_csv('regression_dataset.csv', index=False)

# Plotting
# Here we'll generate a pair plot (scatter plot matrix) using seaborn.
# This will allow you to visualize relationships between each pair of features, including the response y.
pairplot = sns.pairplot(data)
pairplot.savefig("scatter_plot_matrix.png")
plt.show()

# If you want to print the true coefficients
print("True coefficients:", coef)
