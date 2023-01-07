#include <stdio.h>
void main()
{int a,b,d,i,j,c;
printf("enter the size of array");
scanf("%d",&a);
printf("enter the size of second array");
scanf("%d",&b);
int x[a],y[b];
c=a+b;
int z[c],h[c];
for(i=0;i<a;i++)
    {printf("enter the %dth element",i);
    scanf("%d",&x[i]);
    }
printf("now you have to enter the values for second array\n");
for(i=0;i<b;i++)
    {printf("enter th %dth element",i);
    scanf("%d",&y[i]);
    }
for(i=0;i<a;i++)
    {z[i]=x[i];
    }
for(i=a,j=0;i<c,j<b;i++,j++)
    {z[i]=y[j];}

for(j=0;j<a+b;j++)
    {for(i=0;i<a+b-1;i++)
        {if(z[i]>z[i+1])
            {d=z[i];
            z[i]=z[i+1];
            z[i+1]=d;    
            }   
        }
    }

for(i=0;i<c;i++)
    {for(j=0;j<c;j++)
        {if(i!=j)
            {if(z[i]==z[j])
                {z[i]=0;
                }
            }
        }
    }
int k=0;
for(i=0;i<c;i++)
    {if(z[i]!=0)
        {h[k]=z[i];
        k++;
        }
    }

printf("here is the oupt put of your entered code\n\n\n\n\n");
for(i=0;i<k;i++)
    {printf("element is %d",h[i]);
    printf("\n");
    }
for(i=0;i<k;i++)
    {printf("%d,",h[i]);
    
    }


}