import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score

# Helper function to safely read integer input
def read_positive_int(prompt):
    while True:
        try:
            val = int(input(prompt))
            if val > 0:
                return val
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

# Helper function to read a single (x, y) pair
def read_xy_pair(index):
    while True:
        try:
            x = float(input(f"Enter x value for point {index + 1}: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid real number for x.")
    
    while True:
        try:
            y = int(input(f"Enter y (class label) for point {index + 1} (non-negative integer): "))
            if y >= 0:
                break
            else:
                print("Class label must be a non-negative integer.")
        except ValueError:
            print("Invalid input. Please enter a valid integer for y.")
    
    return x, y

# Step 1: Read training set
N = read_positive_int("Enter number of training data points (N): ")
train_X = np.empty((N, 1))
train_y = np.empty(N, dtype=int)

for i in range(N):
    x, y = read_xy_pair(i)
    train_X[i, 0] = x
    train_y[i] = y

# Step 2: Read test set
M = read_positive_int("Enter number of test data points (M): ")
test_X = np.empty((M, 1))
test_y = np.empty(M, dtype=int)

for i in range(M):
    x, y = read_xy_pair(i)
    test_X[i, 0] = x
    test_y[i] = y

# Step 3: Grid search for best k
param_grid = {'n_neighbors': list(range(1, 11))}
knn = KNeighborsClassifier()
cv_folds = min(5, N)  # Ensure cv <= number of training samples
grid_search = GridSearchCV(knn, param_grid, cv=cv_folds)

grid_search.fit(train_X, train_y)

best_k = grid_search.best_params_['n_neighbors']
print(f"\nBest k found by GridSearchCV: {best_k}")

# Step 4: Evaluate on test data
best_model = grid_search.best_estimator_
predictions = best_model.predict(test_X)
accuracy = accuracy_score(test_y, predictions)

print(f"Test accuracy with best k={best_k}: {accuracy:.4f}")