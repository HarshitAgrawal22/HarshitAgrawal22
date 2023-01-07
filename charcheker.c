#include <stdio.h>
void main()
{char a,b;
printf("enter the character to be checked ");
scanf("%c",&a);
if(a>'a' && (a<'z'))
{printf("your entered character is in lowercase");}
else if(a>'A' && a<'Z')
{printf("your enetered upper case");}
else{printf("you entered a non valid number ");}
}