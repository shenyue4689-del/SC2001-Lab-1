import math
import random

def HybridMergeSort(A, start, end, S):
    ## Switch to Insertion Sort if size <= S
    if end - start <= S:
        return InsertionSort(A, start, end)

    mid = start + math.floor((end - start) / 2)

    left_comp = HybridMergeSort(A, start, mid, S)
    right_comp = HybridMergeSort(A, mid, end, S)
    merge_comp = Merge(A, start, mid, end)

    return left_comp + right_comp + merge_comp

def InsertionSort(A, start, end):
    key_comp = 0

    for i in range(start + 1, end): 
        j = i - 1
        while j >= start:
            key_comp += 1  # Comparison A[j] vs A[j+1] occurs here
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]
                j -= 1
            else:
                break  # Comparison evaluated to False; stop shifting

    return key_comp

def Merge(A, start, mid, end):
    key_comp = 0
    i = 0
    k = start
    B_left = A[start:mid]
    B_right = A[mid:end]

    for j in range(0, len(B_right)):
        while i < len(B_left):
            key_comp += 1  # Comparison B_left[i] vs B_right[j] occurs here
            if B_left[i] <= B_right[j]:
                A[k] = B_left[i]
                i += 1
                k += 1
            else:
                break  # Comparison evaluated to False; take B_right[j]
        A[k] = B_right[j]
        k += 1

    # Remaining elements in B_left do not require any key comparisons
    while i < len(B_left):
        A[k] = B_left[i]
        i += 1
        k += 1

    return key_comp

def generate_array(n, x):
    # Generates an array of size n with random integers in range [1, x]
    return [random.randint(1, x) for i in range(n)]

def key_comparison (arr, S):
    return HybridMergeSort(arr, 0, len(arr), S)


if __name__ == "__main__":
    # Example: generate array of size 1,000 with x = 1,000,000
    arr = generate_array(1000, 1000000)
    
    A = [2, 3, 4, 1]
    comparison = key_comparison (A, S=4)
    print(A)
    print("comparison:", comparison)
