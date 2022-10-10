#include<stdio.h>

int main()
{
    FILE *fp = fopen("yfile.txt", "w");
    double x[6] = {1, 2, 3, 4, 2, 1};
    double y[20];
    y[0] = x[0];
    y[1] = -0.5*y[0]+x[1];
    fprintf(fp, "%lf\n%lf\n", y[0], y[1]);
    int  k  = 20;
    for (int i = 2; i <= k - 1; i++) 
    {
        if (i < 6) y[i] = -0.5*y[i-1]+x[i]+x[i-2];
        
        else if (i > 5 && i < 8) y[i] = -0.5*y[i-1]+x[i-2];
        
        else y[i] = -0.5*y[i-1];
        
        fprintf(fp, "%lf\n", y[i]);
    }
    fclose(fp);
    return 0;
}

