from collections import Counter
d1={'Math':81, 'Physics':83, 'Chemistry':87,"bio":262,"arts":77777}
x=Counter(d1)
print(x.most_common())
print(x)