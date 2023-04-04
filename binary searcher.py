# friends=[("rachel",67),("chandler",17),("joey",14),("pheobe",12),("monica",23),("ross",19)]
# age=lambda data:data[1]>18
# drinkers=list(filter(age,friends))
# print(drinkers)
# age(("rachel",90))
import time

def binary(lists,query):

    hi,lo=len(lists)-1,0
    while lo<=hi:
         middle=(hi+lo)//2
         midnumber=lists[middle]

         if lists[middle]==query:

             print(f"{lists[middle]} is at {middle}")
             break
         elif midnumber<query:
             lo=middle+1
         elif midnumber>query:
             hi=middle-1
    print(time.perf_counter())

liast=[i for i in range(1000)]

binary(liast,78)
