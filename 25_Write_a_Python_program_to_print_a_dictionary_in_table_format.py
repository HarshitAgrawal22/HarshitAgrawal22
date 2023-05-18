li= [{'id': 1, 'success': True, 'name': 'Lary'}, {'id': 2, 'success': False, 'name': 
'Rabi'}, {'id': 3, 'success': True, 'name': 'Alex'}]
count=0
for i in li:
    for j in i.keys():
        if i[j]==True:
            count+=1
print(count)