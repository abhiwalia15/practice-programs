#include <stdio.h>
#include <conio.h>
int isprime(int x);
void main()
{
    int n1,n2,r,i;
    clrscr();
    printf("Enter the range\n");
    scanf("%d%d",&n1,&n2);
    printf("The prime numbers between your range is\n");
    for (i=n1;i<=n2;i++)
    {
        r = isprime(i);
        if(r==1)
        printf("%d\t",i);
    }
    getch();
}
int isprime(int x)
{
    int i,count = 0;
    for(i=0;i<=x;i++)
    {
        if(x%i==0)
        count++;
    }
    if(count==2)
    return 1;
    else
    return 0;
}

