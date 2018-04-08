#include <stdio.h>
#include <conio.h>
#include <math.h>
void main ()
{
    int a[15]={2,4,5,6,7,8,9,2,14,24,26,365,241,134,12};
    int i,n;
    printf("ENTER N\n");
    scanf("%d",&n);
    for(i=0;i<15;i++)
    {
        if(a[i]%n==0)
        {
            printf("\n%d",a[i]);
        }
    }
    getch();
}
