# include <stdio.h>
void main()
{int a,i,b,c=0;
printf("enter the size of array");
scanf("%d",&a);

int x[a];
for(i=0;i<a;i++)
    {printf("enter the %dth term of your array",i);
    scanf("%d",&x[i]);
    }
printf("enter the number you are searching for ");
scanf("%d",&b);
for(i=0;i<a;i++)
    {if(x[i]==b)
    {printf("your entered number is present at the %dth index\n",c);}
    else{c+=1;}
    }
if(c==0)
    {printf("your entered element isnt presesnt in the array");
    }
}