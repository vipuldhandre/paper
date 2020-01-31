#method 1
import array as arr
list1 = arr.array('i',[90,80,200,45,301])
list1.sort()
print("Second highest is:",list1[-2])

#method 2

list1 = [90,80,200,45,301]
new_list = set(list1)
new_list.remove(max(new_list))
print(max(new_list))

#method 3

list1 = [90,80,200,45,301]
first_max = max(list1[0],list1[1])
second_max = min(list1[0],list1[1])

for i in range(2,len(list1)):
    if list1[i] > first_max:
        second_max = first_max
        first_max = list1[i]
    else:
        if list1[i] > second_max:
            second_max = list1[i]
print(second_max)

