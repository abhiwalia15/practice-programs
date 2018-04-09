/*First we find which of the two numbers are small and then we find*/
/* modulus of long number with smaller number to find its highest divisor of the number*/ 

#include<stdio.h>
#include<conio.h>
void main()
{
    int a,b,small,lo,ans;
    clrscr();
    printf("Enter two numbers\n");
    scanf("%d%d",&a,&b);
    if(a<b)
    {
        small=a;
        lo=b;
    }
    else
    {
        small=b;
        lo=a;
    }
    do
    {
        ans=small;
        small=lo%small;
    }
    while(small!=0);
    printf("\nHCF=%d",ans);
    getch();
    
}

