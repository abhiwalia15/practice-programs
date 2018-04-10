/*first find product of both the numbers and then loop from 1 till product value to find the number divisible to both the numbers*/
//to find lcm divide product by hcf in for loop

#include<stdio.h>
#include<conio.h>
void main()
{
    int a,b,pro,i,gcd,lcm;
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
        lcm = pro/gcd;
    }
    printf("\nGCD = %d",gcd);
    printf("\nLCM = %d",lcm);
    getch();
}