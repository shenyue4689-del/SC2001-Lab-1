import math
import random

def HybridMergeSort(A, start, end):
    S = 4
    ## Switch to Insertion Sort if size <= S
    if end - start <= S:
        InsertionSort(A, start, end) 
        return A
    else:
        mid = start + math.floor((end - start) / 2)
        HybridMergeSort(A, start, mid)
        HybridMergeSort(A, mid, end)
        Merge(A, start, mid, end)
        return A

def InsertionSort(A, start, end):
    for i in range(start+1, end):
        j = i-1
        while j >= start and A[j] > A[j+1]:
            A[j], A[j+1] = A[j+1], A[j]
            j -= 1

def Merge(A,start,mid,end):
    i = 0
    k = start
    B_left = A[start:mid]
    B_right = A[mid:end]

    for j in range(0, len(B_right)):
        while i < len(B_left) and B_left[i] <= B_right[j]:
            A[k] = B_left[i]
            i += 1
            k += 1
        A[k] = B_right[j]
        k += 1

    while (i < len(B_left)):
        A[k] = B_left[i]
        i += 1
        k += 1


def generate_array(n, x):
    # Generates an array of size n with random integers in range [1, x]
    return [random.randint(1, x) for i in range(n)]

# Example: generate array of size 1,000 with x = 1,000,000
arr = generate_array(1000, 1000000)

A = [2, 3, 4, 1]
HybridMergeSort(A,0,len(A))
print(A)
