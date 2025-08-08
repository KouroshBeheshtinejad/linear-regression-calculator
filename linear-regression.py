import numpy as np
import matplotlib.pyplot as plt

print("Linear Regression & Correlation Calculator")
print("Enter your data separated by spaces.\nExample: 1 2 3 4 5")


try:
    x = list(map(float, input("Enter X values: ").split()))
    y = list(map(float, input("Enter Y values: ").split()))
except ValueError:
    print("Invalid input! Please enter only numbers.")
    exit()


if len(x) != len(y):
    print("The number of X and Y values must be equal!")
    exit()


x_mean = np.mean(x)
y_mean = np.mean(y)

numerator = np.sum((np.array(x) - x_mean) * (np.array(y) - y_mean))
denominator = np.sum((np.array(x) - x_mean) ** 2)

slope = numerator / denominator
intercept = y_mean - slope * x_mean


r = numerator / np.sqrt(np.sum((np.array(x) - x_mean) ** 2) * np.sum((np.array(y) - y_mean) ** 2))


print(f"\nRegression line: y = {slope:.4f}x + {intercept:.4f}")
print(f"Correlation coefficient (r): {r:.4f}")

plt.scatter(x, y, color="blue", label="Data points")
plt.plot(x, slope * np.array(x) + intercept, color="red", label="Regression line")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.title("Linear Regression")
plt.legend()
plt.grid(True)
plt.show()
