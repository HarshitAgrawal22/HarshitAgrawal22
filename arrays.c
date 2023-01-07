#include <stdio.h>
int harshit(int a,int b);
void main()
{int a,b;
scanf("%d%d",&a,&b);

printf("%d",harshit());


}
int harshit(int a,int b)
{printf("your entered numbers are %D and %d",a,b);
int c=(a+b)/2;
return c;



}