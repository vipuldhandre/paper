#question 1
l1 = [1,4,3,7]
l2 = [4,9,7,6]

for i in l1:
    for j in l2:
        if (i+j) == 13:
            print("pair:",i,j)
###################

# question 2
li = [-1,-2,-3]

output = list(map(lambda x:(-x),li))
#print(output)
from functools import reduce

add = reduce((lambda x,y:x+y),output)
print(output)
print(add)

