/*first find product of both the numbers and then loop from 1 till product value to find the number divisible to both the numbers*/
//to find lcm divide product by hcf in for loop

#include<stdio.h>
#include<conio.h>
void main()
{
    int n,i;
    clrscr();
    printf("Enter any number\n");
    scanf("%d",&n);
    printf("THE FACTORS OF %d ARE\n",n);
    for(i=1;i<=n;i++)
    {
        if(n%i==0)
        {
            printf("%d\n",i);
        }
    }
    getch();
}    