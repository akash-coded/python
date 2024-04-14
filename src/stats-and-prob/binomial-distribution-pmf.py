import math
import matplotlib.pyplot as plt


# Define the Binomial PMF
def binomial_pmf(n, k, p):
    # Calculate the binomial coefficient
    def binomial_coefficient(n, k):
        return math.factorial(n) / (math.factorial(k) * math.factorial(n - k))

    return binomial_coefficient(n, k) * (p**k) * ((1 - p) ** (n - k))


# Parameters
n = 100  # Number of ads shown
p = 0.1  # Probability of an ad being clicked

# Generate data points for the k values (number of successes)
k_values = range(n + 1)  # From 0 to n, inclusive
probabilities = [binomial_pmf(n, k, p) for k in k_values]

# Basic visualization using a bar chart
plt.figure(figsize=(10, 5))
plt.bar(k_values, probabilities, color="skyblue")
plt.title("Binomial Distribution - Ad Clicks Probability")
plt.xlabel("Number of Clicks")
plt.ylabel("Probability")
plt.grid(True)
plt.show()
