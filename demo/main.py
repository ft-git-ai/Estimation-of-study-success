import numpy as np


# data
X_train = np.array([[1, 2, 1, 2, 1], 
              [3, 3, 4, 3, 4], 
              [2, 2, 3, 2, 1],
              [1, 1, 1, 2, 1], 
              [3, 3, 4, 3, 4], 
              [4, 4, 3, 4, 2]])
y_train = np.array([1.1, 3.1, 2.3,1.2, 3.6, 4.3])

#print(f"\nMatrix X_train (shape: {X_train.shape}):")
#print(X_train)
#print(f"\nVector y_train (shape: {y_train.shape}):")
#print(y_train)


from sklearn.neighbors import KNeighborsRegressor

# Creating and training a model
knn = KNeighborsRegressor(n_neighbors=3)
knn.fit(X_train, y_train)

# Predictions for new students
new_students = np.array([[1, 1 , 1, 1, 1],[4, 3 , 4, 3, 3]])
predictions = knn.predict(new_students)
for i in range(len(new_students)):
    print(f" Student no.{i}  with entry grade {new_students[i]}  has a predicted final exam average of: {predictions[i]:.2f}")
