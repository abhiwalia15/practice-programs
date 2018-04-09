#include <stdio.h>
#include <conio.h>
#include <math.h>

struct employee
{
    int id,age;
    char name[20];
    float sal;
}e[50];

void main()

{
    int i,n;
    float sal;
    clrscr();
    printf("Enter the number of employee\n");
    scanf("%d",&n);
    for(i=0;i<=n;i++)
    {
        printf("Enter the details of employee\n");
        printf("Enter name\n");
        scanf("%s",e[i].name);
        printf("Enter age\n");
        scanf("%d",&e[i].age);
        printf("Enter id\n");
        scanf("%d",&e[i].id);
        printf("Enter salary\n");
        scanf("%f",&e[i].sal);
        e[i].sal = sal;
    }
    printf("******************************************\n");
    printf("EMP NAME\tEMP AGE\tEMP ID\tEMP SALARY\n");
    printf("------------------------------------------\n");
    for(i=0;i<n;i++)
    {
        printf("%s\t%d\t%d\t%f\n",e[i].name,e[i].age,e[i].id,e[i].sal);
    }
    getch();
}
