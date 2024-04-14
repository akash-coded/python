import math
import matplotlib.pyplot as plt
import numpy as np  # Only used for generating the range of x values for plotting


# Define the exponential PDF
def exponential_pdf(x, lambda_):
    if x < 0:
        return 0  # The exponential distribution is only defined for x >= 0
    return lambda_ * math.exp(-lambda_ * x)


# Parameters
lambda_ = (
    0.5  # Rate parameter, say on average 2 minutes between transactions (lambda = 1/2)
)

# Generate data points for x values (time in minutes)
x_values = np.linspace(0, 10, 400)  # 0 to 10 minutes
y_values = [exponential_pdf(x, lambda_) for x in x_values]

# Basic visualization using a plot
plt.figure(figsize=(8, 4))
plt.plot(x_values, y_values, label=f"Exponential Distribution\nlambda = {lambda_}")
plt.title("PDF of Time Between Transactions")
plt.xlabel("Time (minutes)")
plt.ylabel("Probability Density")
plt.legend()
plt.grid(True)
plt.show()
