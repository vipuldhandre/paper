list1 = [10,22,11,222,300,12]

for i in range(0,len(list1),2):
    
    list1.sort(reverse = True)
print(list1)
        
for i in range(0,len(list1),1):
    list1.sort()

print(list1)
