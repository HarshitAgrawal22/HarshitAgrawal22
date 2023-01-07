#include <stdio.h>
void main()
{int a,b;
printf("enter the number for fibbonacci series");
scanf("%d",&b);
printf("%d",fib(b));
}

int fib();
int fib(int a)
{int b;
if(a==1)
{b=0;}
else if (a==2)
{b=1;}
else{b=fib(a-1)+fib(a-2);
return b;}







}
