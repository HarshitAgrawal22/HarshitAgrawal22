#include <stdio.h>
void main()
{int a;
printf("enter the size of your array");
scanf("%d",&a);
int i,b[a];
for(i=0;i<=(a-1);i++)
        {printf("enter the %dth term of your array",i);
        scanf("%d",&b[i]);}




for(int j=0;j<=a-1;j++)
        {for(i=0;i<=a-1;i++)
            {if(b[i]>b[i+1])
                {//swap
                int c=b[i];
                b[i]=b[i+1];
                b[i+1]=c;}
            }
        }

for(i=0;i<=a-1;i++)
{printf("%d,",b[i]);}
}