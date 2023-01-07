#include <stdio.h>
#include <string.h>
void main()
{char name[50]="harshit";

int i;

for(i=0;i<=50;i++)
    {for(int j=0;j<=50;j++)
        {if(name[j]>name[j+1])
            {char c;
            c=name[j+1];
            name[j+1]=name[j];
            name[j]=c;}
        }
    }

for(i=0;i<=50;i++)
{printf("%c",name[i]);}

}