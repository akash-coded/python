import math
import matplotlib.pyplot as plt


# Define the Poisson PMF
def poisson_pmf(k, lambda_):
    return (lambda_**k * math.exp(-lambda_)) / math.factorial(k)


# Parameters
lambda_ = 10  # Average number of orders per hour

# Generate data points for the k values (number of orders)
k_values = range(0, 30)  # Considering up to 30 orders per hour
probabilities = [poisson_pmf(k, lambda_) for k in k_values]

# Basic visualization using a bar chart
plt.figure(figsize=(8, 4))
plt.bar(k_values, probabilities, color="blue")
plt.title("Poisson Distribution - Average Orders per Hour")
plt.xlabel("Number of Orders")
plt.ylabel("Probability")
plt.grid(True)
plt.show()
