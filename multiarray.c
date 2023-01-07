#include <stdio.h>
void main(){
int a,b,c,d,i,j,k,l;
printf("enter the height of array");
scanf("%d",&a);
printf("enter the width of array");
scanf("%d",&b);
printf("enter the depth of array");
scanf("%d",&c);
printf("enter the time of array");
scanf("%d",&d);
int x[a][b][c][d];
for(i=0;i<=a-1;i++)
    {for(j=0;j<=b-1;j++)
        {for(k=0;k<=c-1;k++)
            {for(l=0;l<=d-1;l++)
                {printf("enter the value of %dth    %dth term",i,j);
                scanf("%d",&x[i][j][k][l]);
                }
            }
        }
    }



for(i=0;i<=a-1;i++)
    {for(j=0;j<=b-1;j++)
        {for(k=0;k<=c-1;k++)
            {for(l=0;l<=d-1;l++)
                {printf("your %dth %dth %dth %dth term is =>%d\n",i,j,k,l,x[i][j][k][l]);
                }
            }
        }
    }
}