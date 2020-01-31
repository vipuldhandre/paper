#method 1
def check(s1,s2):
    if (sorted(s1) == sorted(s2)):
        print("The strings are anagrams.")
    else:
        print("Strings are not anagrams.")

s1 = "listen"
#s2 = "Silent"
s2 = "silent"
check(s1,s2)


#method 2
from collections import Counter
a = "listen"
#b = "Silent"
b = "silent"

if (Counter(a) == Counter(b)):
    print("Anagrams")
else:
    print("not")


#method 3
def is_anagram(str1, str2):
    list_str1 = list(str1)
    list_str1.sort()
    list_str2 = list(str2)
    list_str2.sort()

    return (list_str1 == list_str2)

print(is_anagram('anagram','nagaram'))
print(is_anagram('cat','rat'))
