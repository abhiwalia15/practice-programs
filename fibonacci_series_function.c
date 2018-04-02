#include<stdio.h>
#include<conio.h>

fib(int n)
{
    int a=0,b=1,c,i;
    printf("\n%d\t%d",a,b);
    for(c=3;c<+n;c++)
    {
        c=(a+b);
        a=b;
        b=c;
        printf("%d\t",c);
    }
    return (c);
}
void main()
{
    int series,m;
    clrscr();
    printf("Enter the limit\n");
    scanf("%d",&m);
    series=fib(m);
    getch();
}
