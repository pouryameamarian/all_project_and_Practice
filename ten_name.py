names = []
human_number = 1
while human_number <= 3:
    inp = (input())
    human_number = human_number + 1
    names.append(inp)
names.sort()
print()
for i in names:
    print(i)
    
