import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
data = np.array([42, 55, 47, 63, 58, 49, 51, 60, 53, 46])
mu = np.mean(data)
// below the function finds the standard deviation of the dataset.
def sd(data ,mu):
    variance = np.sum((data - mu) ** 2) / (len(data) - 1)
    sd = np.sqrt(variance)
    return sd
// calculating the z_scores ..
def calculate_zscores(data , mu , sd):
    z_scores = []
    for x in data:
        scores = (x - mu) / sd
        z_scores.append(scores)
    return z_scores

standard_deviation = sd(data , mu)
answer = calculate_zscores(data , mu , standard_deviation)

print(standard_deviation)
print(answer)

plt.subplot(1 , 2, 1)
plt.scatter(range(len(answer)), answer, color="blue", marker="o")
plt.title("Scatter Plot of Z-scores")
plt.xlabel("Index")
plt.ylabel("Z-score")

plt.subplot(1 , 2, 2)
stats.probplot(data, dist="norm", plot=plt)
plt.title("Q-Q Plot for Normality Check")
plt.grid(True)
plt.tight_layout()

plt.show()

