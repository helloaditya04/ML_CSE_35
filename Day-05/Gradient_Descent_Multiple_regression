# Multiple Linear Regression using Gradient Descent

# Dataset
x1 = [1, 2, 3, 4, 5]
x2 = [2, 1, 4, 3, 5]
y  = [5, 6, 9, 10, 13]

n = len(y)

# Initial parameters
beta0 = 0
beta1 = 0
beta2 = 0

# Hyperparameters
alpha = 0.01
iterations = 2000

# Gradient Descent
for i in range(iterations):
    db0 = 0
    db1 = 0
    db2 = 0

    for j in range(n):
        y_pred = beta0 + beta1 * x1[j] + beta2 * x2[j]
        error = y_pred - y[j]

        db0 += error
        db1 += error * x1[j]
        db2 += error * x2[j]

    # Update parameters
    beta0 -= alpha * (2/n) * db0
    beta1 -= alpha * (2/n) * db1
    beta2 -= alpha * (2/n) * db2

# Final coefficients
print("Beta0:", beta0)
print("Beta1:", beta1)
print("Beta2:", beta2)

print(f"Regression Equation: y = {beta0} + {beta1}x1 + {beta2}x2")

# Prediction
x1_new = 6
x2_new = 4
y_pred = beta0 + beta1 * x1_new + beta2 * x2_new
print("Predicted value:", y_pred)
