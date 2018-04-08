#include <stdio.h>
#include <conio.h>
#include <math.h>
void main ()
{
   int a,b,c,*ptr,*ptr1;
   clrscr();
   printf("ENTER A and B\n");
   scanf("%d%d",&a,&b);
   ptr=&a;
   ptr1=&b;
   c = *ptr+*ptr1;
   printf("%d\n%d\n%d\n%d\n%d",ptr,ptr1,*ptr,*ptr1,c);
   getch();
}   
   
