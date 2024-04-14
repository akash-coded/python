import math
import numpy as np
import matplotlib.pyplot as plt


# Define the PDF of normal distribution
def normal_pdf(x, mean, std_dev):
    return (1 / (std_dev * math.sqrt(2 * math.pi))) * math.exp(
        -0.5 * ((x - mean) / std_dev) ** 2
    )


# Parameters
mean = 0.0  # Average daily return (mean return close to 0 for this example)
std_dev = 0.02  # Standard deviation of returns (2% daily return variability)

# Generate data points for the x-axis (representing daily returns from -10% to +10%)
x_values = np.linspace(-0.1, 0.1, 400)
y_values = [normal_pdf(x, mean, std_dev) for x in x_values]

# Basic visualization
plt.figure(figsize=(8, 4))
plt.plot(
    x_values, y_values, label=f"Normal Distribution\nMean = {mean}, SD = {std_dev}"
)
plt.title("Simulated PDF of Daily Stock Returns")
plt.xlabel("Daily Return")
plt.ylabel("Probability Density")
plt.legend()
plt.grid(True)
plt.show()
