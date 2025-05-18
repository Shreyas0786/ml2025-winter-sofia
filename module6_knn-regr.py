import numpy as np

class KNNRegressor:
    def __init__(self):
        self.x_values = np.array([])
        self.y_values = np.array([])
    
    def get_input(self):
        N = int(input("Enter the number of points (N): "))
        while N <= 0:
            print("Please enter a positive integer.")
            N = int(input("Enter the number of points (N): "))
        
        k = int(input("Enter the number of neighbors (k): "))
        while k <= 0:
            print("Please enter a positive integer.")
            k = int(input("Enter the number of neighbors (k): "))
        
        print(f"Enter {N} (x, y) points one by one:")
        x_list = []
        y_list = []
        for i in range(N):
            x = float(input(f"Enter x value for point {i+1}: "))
            y = float(input(f"Enter y value for point {i+1}: "))
            x_list.append(x)
            y_list.append(y) 
        
        self.x_values = np.array(x_list)
        self.y_values = np.array(y_list)
        return k
    
    def predict(self, X, k):
        if k > len(self.x_values):
            return "Error: k cannot be larger than N"
        
        # Calculate distances from X to all points
        distances = np.abs(self.x_values - X)
        
        # Get indices of k smallest distances
        nearest_indices = np.argsort(distances)[:k]
        
        # Get the y values of nearest neighbors
        nearest_y = self.y_values[nearest_indices]
        
        # Return average of these y values
        return np.mean(nearest_y)

def main():
    knn = KNNRegressor()
    k = knn.get_input()
    
    X = float(input("Enter the X value to predict Y for: "))
    result = knn.predict(X, k)
    
    print(f"Predicted Y value: {result}")

if __name__ == "__main__":
    main()