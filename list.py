lst = list()
lst.append(22)
lst.append(23)
lst.append(24)
lst.append(25)

print(lst[0])
lst[0] = 28
print(lst)

 # count the frequency of names
 # list of names are Gideon, Andrew, Benard, Selah, Mercy, Erick, Faith

counts = dict()

names =['Gideon', 'Andrew', 
'Benard', 'Selah', 'Mercy', 
'Gideon', 'Andrew', 'Erick',
'Gideon', 'Faith',]

for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name]+1
print(counts)
