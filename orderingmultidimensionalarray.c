#include <stdio.h>
void main(){
int a,b,i,j;
printf("enter the height of array");
scanf("%d",&a);
printf("enter the width of array");
scanf("%d",&b);
int x[a][b];
for(i=0;i<=a-1;i++)
    {for(j=0;j<=b-1;j++)
        {printf("enter the value of %dth   %dth term",i,j);
        scanf("%d",&x[i][j]);}
    }
for(int l=0;l<=(a-1)*(b-1);l++)    
    {for(int k=0;k<=(a-1)*(b-1);k++)
        {for(i=0;i<=a-1;i++)
            {for(j=0;j<=b-1;j++)
                {if(x[i][j]>x[i][j+1])
                {int c=x[i][j+1];
                x[i][j+1]=x[i][j];
                x[i][j]=c;
                }
                else if(x[i][j]>x[i+1][j])
                {int c=x[i+1][j];
                x[i+1][j]=x[i][j];
                x[i][j]=c;
                }
                }
            }
        }
    }

for(i=0;i<=a-1;i++)
    {for(j=0;j<=b-1;j++)
        {printf("%d\n",x[i][j]);
        }
    }




}