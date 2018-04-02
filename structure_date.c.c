/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <stdio.h>
#include <conio.h>
struct date
{
  int day, month, year;
};
void
main ()
{
  struct date d;
  printf ("Enter the day\n");
  scanf ("%d", &d.day);
  printf ("Enter the month\n");
  scanf ("%d", &d.month);
  printf ("Enter the year\n");
  scanf ("%d", &d.year);
  printf ("\n DATE:");
  printf ("%d/%d/%d", d.day, d.month, d.year);
  getch ();
}
