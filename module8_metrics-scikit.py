import numpy as np
from sklearn.metrics import precision_score, recall_score

# Step 1: Get the number of samples
while True:
    try:
        N = int(input("Enter the number of data points (positive integer): "))
        if N > 0:
            break
        else:
            print("Please enter a positive integer.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

# Step 2: Initialize NumPy arrays
ground_truth = np.empty(N, dtype=int)
predictions = np.empty(N, dtype=int)

# Step 3: Collect data
for i in range(N):
    while True:
        try:
            x = int(input(f"Enter ground truth (x) for point {i+1} (0 or 1): "))
            if x in [0, 1]:
                break
            else:
                print("Please enter 0 or 1.")
        except ValueError:
            print("Invalid input. Please enter 0 or 1.")

    while True:
        try:
            y = int(input(f"Enter predicted value (y) for point {i+1} (0 or 1): "))
            if y in [0, 1]:
                break
            else:
                print("Please enter 0 or 1.")
        except ValueError:
            print("Invalid input. Please enter 0 or 1.")

    ground_truth[i] = x
    predictions[i] = y

# Step 4: Compute metrics using scikit-learn
precision = precision_score(ground_truth, predictions)
recall = recall_score(ground_truth, predictions)

# Step 5: Output the results
print(f"\nPrecision: {precision:.4f}")
print(f"Recall: {recall:.4f}")
