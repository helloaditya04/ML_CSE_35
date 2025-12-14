# Linear Regression using Gradient Descent

# Dataset
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Initial values
beta0 = 0
beta1 = 0

# Hyperparameters
alpha = 0.01      # learning rate
iterations = 1000
n = len(x)

# Gradient Descent
for i in range(iterations):
    sum_error_b0 = 0
    sum_error_b1 = 0
    
    for j in range(n):
        y_pred = beta0 + beta1 * x[j]
        error = y_pred - y[j]
        
        sum_error_b0 += error
        sum_error_b1 += error * x[j]
    
    # Update bita values
    beta0 = beta0 - alpha * (2/n) * sum_error_b0
    beta1 = beta1 - alpha * (2/n) * sum_error_b1

# Final parameters
print("Beta0 (Intercept):", beta0)
print("Beta1 (Slope):", beta1)

# Regression Equation
print(f"Regression Equation: y = {beta0} + {beta1}x")

# Prediction
x_new = 6
y_new = beta0 + beta1 * x_new
print("Predicted value for x =", x_new, "is", y_new)

