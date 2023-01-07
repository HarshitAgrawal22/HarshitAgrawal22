#include <stdio.h>
void main()
{
int a,b,c;
printf("enter the two number to swap");
scanf("%d",&a);
scanf("%d",&b);
c=a;
a=b;
b=c;
printf("%d\n%d",a,b);
}