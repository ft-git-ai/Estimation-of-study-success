import numpy as np
from sklearn.neighbors import KNeighborsRegressor
from sklearn.preprocessing import StandardScaler
# data
X_train = np.array([[1, 2, 1, 2, 1], 
                    [3, 3, 4, 3, 4],
                    [2, 2, 3, 2, 1],
                    [1, 1, 1, 2, 1],
                    [3, 3, 4, 3, 4],
                    [4, 4, 3, 4, 2]])
y_train = np.array([1.1, 3.1, 2.3, 1.2, 3.6, 4.3])
# print(f"\nMatrix X_train (shape: {X_train.shape}):")
# print(X_train)
# print(f"\nVector y_train (shape: {y_train.shape}):")
# print(y_train)
# Input data normalization
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
# Creating and training a model
knn = KNeighborsRegressor(n_neighbors=3)
knn.fit(X_train_scaled, y_train)
# Predictions for new students
new_students = np.array([[1, 1, 1, 1, 1], [4, 3, 4, 3, 3]])
new_students_scaled = scaler.transform(new_students)
predictions = knn.predict(new_students_scaled)
for i in range(len(new_students)):
    print(f" Student no.{i}  with entry grade {new_students[i]} ")
    print(f" has a predicted final exam average of: {predictions[i]:.2f}")
    print(" ")
input("Press Enter to exit...")


