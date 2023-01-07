#include <stdio.h>
void main()
{int a,b;
printf("enter any two numbers to be compared");
scanf("%d%d",&a,&b);
(a>b)?printf("%d is greater than %d",a,b):printf("%d is greater than %d ",b,a);}