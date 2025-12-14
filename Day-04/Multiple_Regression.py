import numpy as np

# Input data
# Features: x1, x2
X = np.array([
    [1, 1, 2],
    [1, 2, 1],
    [1, 3, 4],
    [1, 4, 3],
    [1, 5, 5]
])

# Output variable
y = np.array([
    [5],
    [6],
    [9],
    [10],
    [13]
])

# Normal Equation: beta = (X^T X)^-1 X^T y
XT = X.T
beta = np.linalg.inv(XT.dot(X)).dot(XT).dot(y)

# Extract coefficients
beta0 = beta[0][0]
beta1 = beta[1][0]
beta2 = beta[2][0]

# Regression Equation
print("Beta0:", beta0)
print("Beta1:", beta1)
print("Beta2:", beta2)

print(f"Regression Equation: y = {beta0} + {beta1}x1 + {beta2}x2")

# Prediction
x1_new = 6
x2_new = 4
y_pred = beta0 + beta1 * x1_new + beta2 * x2_new
print("Predicted value:", y_pred)

