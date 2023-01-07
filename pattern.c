#include <stdio.h>
void main(){
int b,a=0,c;
printf("enter teh number of times you want to run the loop");
scanf("%d",&c);
while(a<=c)
{a++;
printf("\n");
for(b=a;b<=c;b++)
{printf("*");}
}

}