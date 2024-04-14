import math
import matplotlib.pyplot as plt
import numpy as np


# Define the PDF for Normal distribution manually
def normal_pdf(x, mean, std_dev):
    return (1 / (std_dev * math.sqrt(2 * math.pi))) * math.exp(
        -0.5 * ((x - mean) / std_dev) ** 2
    )


# Define the PMF for Poisson distribution manually
def poisson_pmf(k, lambda_):
    return (lambda_**k * math.exp(-lambda_)) / math.factorial(k)


# Define the PMF for Binomial distribution manually
def binomial_pmf(n, k, p):
    def binomial_coefficient(n, k):
        return math.factorial(n) / (math.factorial(k) * math.factorial(n - k))

    return binomial_coefficient(n, k) * (p**k) * ((1 - p) ** (n - k))


# Define the PDF for Exponential distribution manually
def exponential_pdf(x, lambda_):
    return lambda_ * math.exp(-lambda_ * x) if x >= 0 else 0


# Setup parameters
# Normal distribution parameters
mean, std_dev = 1000, 150  # Daily site visits

# Poisson distribution parameters
lambda_poisson = 50  # Average orders per hour

# Binomial distribution parameters
n, p = 100, 0.95  # Number of transactions and success rate

# Exponential distribution parameters
lambda_exponential = 1 / 40  # Average 40 minutes between orders

# Generate data points
x_values = np.linspace(700, 1300, 600)
k_values = range(100)
binom_k_values = range(n + 1)
exp_x_values = np.linspace(0, 200, 400)

# Calculate distributions
normal_probs = [normal_pdf(x, mean, std_dev) for x in x_values]
poisson_probs = [poisson_pmf(k, lambda_poisson) for k in k_values]
binomial_probs = [binomial_pmf(n, k, p) for k in binom_k_values]
exponential_probs = [exponential_pdf(x, lambda_exponential) for x in exp_x_values]

# Plotting
fig, ax = plt.subplots(2, 2, figsize=(14, 10))

# Normal Distribution
ax[0, 0].plot(x_values, normal_probs, color="blue")
ax[0, 0].set_title("Normal Distribution: Daily Site Visits")
ax[0, 0].set_xlabel("Site Visits")
ax[0, 0].set_ylabel("Density")

# Poisson Distribution
ax[0, 1].bar(k_values, poisson_probs, color="green")
ax[0, 1].set_title("Poisson Distribution: Orders per Hour")
ax[0, 1].set_xlabel("Number of Orders")
ax[0, 1].set_ylabel("Probability")

# Binomial Distribution
ax[1, 0].bar(binom_k_values, binomial_probs, color="red")
ax[1, 0].set_title("Binomial Distribution: Successful Transactions")
ax[1, 0].set_xlabel("Number of Successes")
ax[1, 0].set_ylabel("Probability")

# Exponential Distribution
ax[1, 1].plot(exp_x_values, exponential_probs, color="purple")
ax[1, 1].set_title("Exponential Distribution: Time Between Orders")
ax[1, 1].set_xlabel("Time (minutes)")
ax[1, 1].set_ylabel("Density")

plt.tight_layout()
plt.show()
