li=[{"id":1,"name":"ayush","term1":56,"term2":87},{"id":2,"name":"leo","term1":51,"term2":37},{"id":3,"name":"love","term1":26,"term2":47}]
for d in li:
    d["total"]=d.pop("term1")+d.pop("term2")
print(li)