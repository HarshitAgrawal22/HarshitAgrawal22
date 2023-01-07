#include <stdio.h>
void main()
{int a,b,c,d,e;
a=16;
b=++a;
c=b++;
c*=b;
b+=c;
d=c--;
d+=a;
e=--d;
e%=a;
printf(" the values of your variables are  \na=%d\nb=%d\nc=%d\nd=%d\ne=%d",a,b,c,d,e);}