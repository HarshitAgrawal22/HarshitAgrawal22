#include <stdio.h>
void main()
{int a,b,i;
printf("enter the length of array");
scanf("%d",&a);
printf("enter the breadth of array");
scanf("%d",&b);
char x[a][b];
for(i=0;i<=a-1;i++)
{printf("enter your names in array");
scanf("%s",&x[i]);



}
for(i=0;i<=a-1;i++)
{
printf("%s\n",x[i]);

77 
}





}