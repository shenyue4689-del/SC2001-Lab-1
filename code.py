import math
import random

def HybridMergeSort(A, start, end, S, key_comp):
    ## Switch to Insertion Sort if size <= S
    if end - start <= S:
        InsertionSort(A, start, end, key_comp) 
        return        ## A and key_comp are mutable
    else:
        mid = start + math.floor((end - start) / 2)
        HybridMergeSort(A, start, mid,S ,key_comp)
        HybridMergeSort(A, mid, end,S ,key_comp)
        Merge(A, start, mid, end, key_comp)
        return        ## A and key_comp are mutable

def InsertionSort(A, start, end, key_comp):
    for i in range(start + 1, end): 
        j = i - 1
        while j >= start:
            key_comp[0] += 1  # Comparison A[j] vs A[j+1] occurs here
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]
                j -= 1
            else:
                break  # Comparison evaluated to False; stop shifting

def Merge(A, start, mid, end, key_comp):
    i = 0
    k = start
    B_left = A[start:mid]
    B_right = A[mid:end]

    for j in range(0, len(B_right)):
        while i < len(B_left):
            key_comp[0] += 1  # Comparison B_left[i] vs B_right[j] occurs here
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

def generate_array(n, x):
    # Generates an array of size n with random integers in range [1, x]
    return [random.randint(1, x) for i in range(n)]

def key_comparison (arr, S):
    key_comp = [0]
    HybridMergeSort (arr, 0, len(arr), S, key_comp)
    return key_comp[0]

# Example: generate array of size 1,000 with x = 1,000,000
arr = generate_array(1000, 1000000)

A = [2, 3, 4, 1]
comparison = key_comparison (A, S=4)
print(A)
print("comparison:", comparison)
