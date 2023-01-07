#include <stdio.h>
void main()
{int i=1,a,b,c,d;
printf("enter the number to be checked ");
scanf("%d",&a);
while(a>=1)
{
    i=i*10;
    b=a%10;
    c=b;
a=a/10;
printf("%d\n",b);
d=c*i;
d=d+c;
printf("%d\n",d);

}
}