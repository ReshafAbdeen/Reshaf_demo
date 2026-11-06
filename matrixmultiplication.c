#include <stdio.h>

int main()
{
    int r1, c1, r2, c2;
    // Fisrt Marix
    printf("Enter First Matrix row na columns: ");
    scanf("%d %d", &r1, &c1);

    // Second Matrix
    printf("Enter Second Matrix row na columns:  : ");
    scanf("%d %d", &r2, &c2);

    if (c1 != r2)
    {
        printf("\nMatirx multiplication is impossible! (First matrix ke columns aur second matrix ke rows barabar hone chahiye.)\n");
        return 0;
    }

    int a[r1][c1], b[r2][c2], result[r1][c2];
    
    // First matrix element
    printf("\nEnter Element of First matrix\n");
    for (int i = 0; i < r1; i++) {
        for (int j = 0; j < c1; j++) {
            printf("Element a[%d][%d]", i, j);
            scanf("%d", &a[i][j]);
        }
    }
    // second metrix element
    printf("\nEnter Element of Second matrix\n");
    for (int i = 0; i < r2; i++) {
        for (int j = 0; j < c2; j++) {
            printf("Element a[%d][%d]", i, j);
            scanf("%d", &b[i][j]);
        }
    }
    // Multiplication logic
    for (int i = 0; i < r1; i++){
        for (int j = 0; j <c2; j++){
            result[i][j] = 0;
            for (int k = 0; k < c1; k++){
                result[i][j] += a[i][j] * b[i][j];
            }
        }
    }

    // Result of matrix
    printf("\nResult Matrix (%dx%d) : \n", r1, c2);
    for (int i = 0; i < r1; i++){
        for (int j = 0; j <c2; j++){
            printf("%d\t", result[i][j]);
        }
        printf("\n");
    }
    return 0; 
}

