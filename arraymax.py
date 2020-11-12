def arrayMax(A, n):
    if len(A) != n:
        raise "Error: the size of A must be equal to n"
        return 0
    currentMax = A[0]
    for i in range(n):
        if currentMax < A[i]:
            currentMax = A[i]
    return currentMax


A = [1, 2, 10, 4, 50, 3, 47, 0]
print(arrayMax(A, len(A)))
