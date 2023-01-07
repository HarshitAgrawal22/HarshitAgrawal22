#include <stdio.h>
void main()
{char a;
printf("enter the first letter of the pc component you want to search");
scanf("%c",&a);
switch(a){
case 'm':printf("your componet is mouse");
break;
case 'k':printf("your component is keyboard");
break;
case 'h':printf("your component is headphone");
break;
case 'u':printf("your component is UPS");
break;
case 's':printf("your component is speaker");
break;
case 'c':printf("your compnent is CPU");
break;
default:printf("CPU components are not listed above or your component is mot available");}
}