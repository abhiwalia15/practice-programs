#include <stdio.h>
#include <conio.h>
#include <math.h>
void main()
{
int n,i,result;
clrscr();
printf("ENTER THE NUMBER\n");
scanf("%d",&n);
printf("THE TERMS ARE\n");
for(i=0;i<=10;i++)
{
    result = pow(n,i);
    printf("%d\n",result);
}
getch();
}
