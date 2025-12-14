# Linear Regression using Direct Formula (Least Squares Method)

# Input data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

n = len(x)

# Calculating required sums
sum_x = sum(x)
sum_y = sum(y)
sum_xy = 0
sum_x2 = 0

for i in range(n):
    sum_xy += x[i] * y[i]
    sum_x2 += x[i] * x[i]

# Calculating beta1 (slope)
beta1 = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x ** 2)

# Calculating beta0 (intercept)
mean_x = sum_x / n
mean_y = sum_y / n
beta0 = mean_y - beta1 * mean_x

# Regression equation
print("Beta0 (Intercept):", beta0)
print("Beta1 (Slope):", beta1)
print("Regression Equation: y =", beta0, "+", beta1, "x")

# Prediction
x_new = 6
y_pred = beta0 + beta1 * x_new
print("Predicted value for x =", x_new, "is", y_pred)
