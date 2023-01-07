#include <stdio.h>
void main()
{int a,b,c,d,e;
a=10;
b=a++;
c=--b;
d=++c;
d*=a;
d-=b;
e=d++;
printf(" the values of your variables are  \na=%d\nb=%d\nc=%d\nd=%d\ne=%d",a,b,c,d,e);}