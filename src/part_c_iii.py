import statistics
import matplotlib.pyplot as plt
import time
from part_a import generate_array, key_comparison


# C(iii): Find optimal S for different n
n_values = [10000, 100000, 1000000]
S_values = [1, 2, 3, 4, 5, 6, 8, 16, 32, 64]

# Store scores for each S
scores = {S: 0 for S in S_values}
# Appearance times in top 3 for each S
counts = {S: 0 for S in S_values}

for n in n_values:
    print("\nSTART n =", n)

    original = generate_array(n, 1000000)
    assert all(isinstance(x, int) for x in original)
    times = []

    for S in S_values:

        run_times = []

        for _ in range(7):
            arr = original.copy()

            start = time.perf_counter()
            key_comparison(arr, S)
            end = time.perf_counter()

            run_times.append(end - start)

        median_time = statistics.median(run_times)
        times.append(median_time)
        print("S =", S, "median time =", median_time)


    # Find top 3 S values
    ranked = sorted(zip(times, S_values))

    top1 = ranked[0][1]
    top2 = ranked[1][1]
    top3 = ranked[2][1]

    print("Top 3 for n =", n, ":", top1, top2, top3)

    # Give scores
    scores[top1] += 3
    scores[top2] += 2
    scores[top3] += 1
    # Record times in top 3
    counts[top1] += 1
    counts[top2] += 1
    counts[top3] += 1

    plt.plot(S_values, times, marker="o", label="n=" + str(n))
    del arr
    del original


# overall ranking
overall_ranking = sorted(
    S_values,
    key=lambda S: (scores[S], counts[S]),
    reverse=True
)

print("\nOverall ranking:")

for S in overall_ranking:
    print(
        "S =", S,
        "score =", scores[S],
        "top3 appearances =", counts[S]
    )

best_S = overall_ranking[0]

print("\nFinal selected S =", best_S)


plt.xlabel("Threshold S")
plt.ylabel("Median Running Time (seconds)")
plt.title("C(iii): Running Time vs Threshold S")
plt.legend()
plt.show()