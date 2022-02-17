n = 5
for i in range(0, n):
     print(i)

#iterating over a list

print("list iteration")
l = ["hacker", "for", "life"]

for i in l:
    print(i)

#iterating over the list

print("\ntuple Iteration")
t = ("hacker", "for", "life")

for i in t:
    print(i)

#iterating over a string

print("\nDictionary Iteration")
d = dict()
d['xyz'] = 123
d['abc'] = 345

for i in d:
    print("%s %d" %(i, d[i]))