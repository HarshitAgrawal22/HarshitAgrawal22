#include <stdio.h>
int main()
{int a,d;
scanf("%d",&a);
    d=a;
    for(int i=1;i<=a;i++)
{         for(int j=a;j>=i;j--)
            {printf(" ");}
                for(int k=1;k<=i;k++)
                    {printf("%d",k);}
                    for(int l=1;l<=i;l++)
                        {printf("%d",l);}
                        printf("\n");
}



for(int m=0;m<=a;m++)
{for(int o=1;o<=m;o++)
{
printf(" ");}
for(int n=a;n>=m;n--)
{printf("%d",n);} 
for(int p=(d-m);p>=1;p--)
{printf("%d",p);

}



printf("\n");

}
}