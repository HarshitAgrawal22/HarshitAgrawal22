#include<stdio.h>
void main()
{int p,r,t,a;
printf("enter the principle value  ");
scanf("%d",&p);
printf("enter the rate of intrest in %%  ");
scanf("%d",&r);
printf("enter the time period  ");
scanf("%d",&t);
a=p*r*t/100;
printf("%d",a);
}