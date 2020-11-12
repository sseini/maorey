#include <stdio.h>


int arrayMax(int *const A[], int n)
{
    //A=calloc(n, sizeof(int);
    printf("%ld\n",sizeof(A)/sizeof(*A));
    // if (sizeof(A)/sizeof(A[0]) != n)
    // {
    //     printf("Error: the number of elemets of A must be equal to n\n");
    //     return 0;
    // }
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
    int A[]={1, 2, 10, 4, 50, 3, 47, 0};
    int n=sizeof(A)/sizeof(A[0]) ;
    printf("%d\n",n);
    int result = arrayMax(A, n);
    printf("result: %d", result);
}