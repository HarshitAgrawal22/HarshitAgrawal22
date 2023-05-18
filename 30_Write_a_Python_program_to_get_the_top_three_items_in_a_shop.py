di= {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
for key,value in di.items():
    di2={key:sorted(value)}
    print(di2)