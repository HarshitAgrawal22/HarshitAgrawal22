#include <stdio.h>
#include <string.h>
void main()
{int a,b,c;
printf("enter the size of your name");
scanf("%d",&a);
char d[a];
printf("enter your first name   ");
scanf("%s",&d);
printf("\n%s\n",d);
for(c=0;c<=a-1;c++)
{printf("%c",d[c]);


}






}