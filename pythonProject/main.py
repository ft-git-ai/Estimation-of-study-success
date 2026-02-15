import numpy as np
from sklearn.neighbors import KNeighborsRegressor

# data
input_file = np.genfromtxt('data.txt', delimiter=';', skip_header=1)
input_file_new_students = np.genfromtxt('data_new_students.txt', delimiter=';', skip_header=1)
X_train = np.asarray(input_file[:, :-1])  # all rows, all columns except the last one
y_train = np.asarray(input_file[:, -1])  # all rows, only the last column

# print(f"\nMatrix X_train (shape: {X_train.shape}):")
# print(X_train)
# print(f"\nVector y_train (shape: {y_train.shape}):")
# print(y_train)


# Creating and training a model
knn = KNeighborsRegressor(n_neighbors=3)
knn.fit(X_train, y_train)
# Predictions for new students
new_students = np.asarray(input_file_new_students)
predictions = knn.predict(new_students)
for i in range(len(new_students)):
    print(f" Student no.{i}  with entry grade {new_students[i]} ")
    print(f" has a predicted final exam average of: {predictions[i]:.2f}")
    print(" ")
input("Press Enter to exit...")
