purse = dict()
purse['money'] = 100
purse['phone'] = 1
purse['laptop'] = 1


purse['money'] = purse['money'] + 100
print(purse['money'])
print(purse)

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

# dictionary to count the number of words
# in the paragraph you enter


counts = dict()
line = input("Enter your text here: ")
words = line.split()
#print(words)
for word in words:
    counts[word] = counts.get(word, 0) + 1
print('Counts', counts)