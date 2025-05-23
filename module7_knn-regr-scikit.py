# Loading the required libraries
import numpy as np
from sklearn.neighbors import KNeighborsRegressor

# Asking user for input N and k
N = int(input("Enter the number of numbers (N): "))
k = int(input("Enter the number of neighbors (k): "))

X_data = np.zeros((N, 1))
y_data = np.zeros(N)

for i in range(N):
    x = float(input(f"Enter x value for point {i + 1}: "))
    y = float(input(f"Enter y value for point {i + 1}: "))
    X_data[i] = x
    y_data[i] = y
    
# Checking if k is valid
if k > N:
    print("Error: k cannot be greater than N.")
else:
    X_input = float(input("\nEnter the X value to predict Y: "))
# Creating and training the k-NN Regressor
    model = KNeighborsRegressor(n_neighbors=k)
    model.fit(X_data, y_data)
# Predicting the Y value for the input X
    y_pred = model.predict(np.array([[X_input]]))
    print(f"\nPredicted Y value for X = {X_input}: {y_pred[0]}")

# Variance of Label (Results)
label_variance = np.var(y_data)
print(f"\nVariance of labels in the training dataset: {label_variance}")