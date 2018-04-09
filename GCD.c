/*first find product of both the numbers and then loop from 1 till product value to find the number divisible to both the numbers*/
#include<stdio.h>
#include<conio.h>
void main()
{
    int a,b,pro,i,gcd;
    clrscr();
    printf("Enter two numbers\n");
    scanf("%d%d",&a,&b);
    pro=(a*b);
    for(i=1;i<pro;i++)
    {
        if((a%i==0)&&(b%i==0))
        {
        gcd = i;
        }
    }
    printf("\nGCD = %d",gcd);
    getch();
}