##s = "hi, i am vipul's"
##
##li = s.split()
##
##li1 = []
##i = 0
##while i < len(li):
##    
##    li1.append(li[i][::-1])
##    i += 1
##output = " ".join(li1)
##print(output)

import re
inp = "Hi, I am Vip's"
output = re.sub(r'\w+',lambda x:x.group(0)[len(x.group(0))::-1],inp)
print(output)
