##def find_length(x):
##    count = 0
##    for i in x:
##        count += 1
##    return count
##
##list1 = [10,300,20,40,200]
##print(find_length(list1))

##import array as arr
##
##def find_length(x):
##    count = 0
##    for i in x:
##        count += 1
##    return count
##a = arr.array('i',[10,300,20,40,200])
##print(find_length(a))


##from functools import reduce
##import array as arr
##
##def string_length(string):
##    return reduce(lambda x,y: x+1, a, 0)
##
##a = arr.array('i',[10,300,20,40,200])
##print(string_length(a))

import array as arr

def array_length(x):
    return sum(1 for char in x)

a = arr.array('i',[10,300,20,40,200,1000,20])
print(array_length(a))



