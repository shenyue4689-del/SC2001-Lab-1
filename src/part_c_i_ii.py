import matplotlib.pyplot as plt
import time
from part_a import generate_array, key_comparison


# C(i): Fixed S, different n
S = 16
n_values = [1000, 10000, 100000, 1000000, 10000000]
comparisons = []

for n in n_values:
    arr = generate_array(n, 1000000)
    comparisons.append(key_comparison(arr, S))

plt.plot(n_values, comparisons, marker="o")
plt.xscale("log")
plt.yscale("log")
plt.xlabel("Input size n")
plt.ylabel("Number of key comparisons")
plt.title("C(i): Key Comparisons vs Input Size")
plt.show()
plt.close()
del arr


# C(ii): Fixed n, different S
n = 100000
S_values = [1, 2, 3, 4, 5, 6, 8, 16, 32]
comparisons = []

original = generate_array(n, 1000000)
assert all(isinstance(x, int) for x in original)

for S in S_values:
    arr = original.copy()
    comparisons.append(key_comparison(arr, S))

plt.plot(S_values, comparisons, marker="o")
plt.xlabel("Threshold S")
plt.ylabel("Number of key comparisons")
plt.title("C(ii): Key Comparisons vs S")
plt.show()
plt.close()
del arr
del original


# # C(iii): Find optimal S for different n
# n_values = [10000, 100000, 1000000]
# S_values = [1, 2, 3, 4, 5, 6, 8, 16, 32, 64]

# for n in n_values:
#     print("START n =", n)

#     original = generate_array(n, 1000000)
#     assert all(isinstance(x, int) for x in original)
#     times = []

#     for S in S_values:
#         print("  S =", S)

#         total_time = 0

#         for _ in range(5):
#             arr = original.copy()

#             start = time.perf_counter()
#             key_comparison(arr, S)
#             end = time.perf_counter()

#             total_time += end - start

#         times.append(total_time / 5)

#     best_S = S_values[times.index(min(times))]
#     print("n =", n, "optimal S =", best_S)

#     plt.plot(S_values, times, marker="o", label="n=" + str(n))
#     del arr
#     del original

# plt.xlabel("Threshold S")
# plt.ylabel("CPU Time (seconds)")
# plt.title("C(iii): Finding Optimal S")
# plt.legend()
# plt.show()