nth=int(input("enter nth number: "))
a=0
b=1
c=0
for i in range(2,nth+1):
    c=a+b
    a=b
    b=c
    
print(f" {nth}-th Fibonacci number if {c}")