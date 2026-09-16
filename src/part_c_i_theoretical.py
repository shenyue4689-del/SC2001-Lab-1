import matplotlib.pyplot as plt
import math
from part_a import generate_array, key_comparison



# C(i): Fixed S, different n
S = 16
n_values = [1000, 10000, 100000, 1000000, 10000000]
comparisons = []

for n in n_values:
    arr = generate_array(n, 1000000)
    comparisons.append(key_comparison(arr, S))

# Scaled theoretical O(n log n) reference
c = comparisons[0] / (n_values[0] * math.log2(n_values[0]))

theoretical = []
for n in n_values:
    theoretical.append(c * n * math.log2(n))

# Plot empirical results and theoretical reference
plt.plot(
    n_values,
    comparisons,
    marker="o",
    label="Empirical key comparisons"
)
plt.plot(
    n_values,
    theoretical,
    linestyle="--",
    label="Scaled n log n reference"
)

plt.xscale("log")
plt.yscale("log")
plt.xlabel("Input size n")
plt.ylabel("Number of key comparisons")
plt.title("C(i): Empirical vs Theoretical Growth")
plt.legend()
plt.show()
plt.close()  
del arr