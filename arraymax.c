#include <stdio.h>

int arrayMax(int A[], int n)
{
    if (len(A) != n)
    {
        printf("Error: the number of elemets of A must be equal to n");
        return 0;
    }
    int currentMax = A[0];
    for (int i = 1; i < n; i++)
    {
        if (currentMax < A[i])
            currentMax = A[i];
    }
    return currentMax;
}

int main()
{
    int A[] = {1, 2, 10, 4, 50, 3, 47, 0};
    int result = arrayMax(A, len(A));
    printf("result: %d", result);
}