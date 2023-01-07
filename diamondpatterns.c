#include <stdio.h>
void main()
{int a,b,c=0;
scanf("%d",&a);

for(int i=1;i<=100;i++)
{while(a>0)
{a=i;
b=a%10;
c=c*10;c=c+b;
a=a/10;



}
printf("%d\n",c);}



}