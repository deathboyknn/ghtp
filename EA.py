
from sys import stdin

max_3 = 0
max_7 = 0
max_21 = 0
max_all = 0

for elem in stdin:
    elem = int(elem)
    
    if elem % 21 == 0 and max_21 < elem:
        max_all = max(max_all, max_21)
        max_21 = elem
        continue
    
    if elem % 7 == 0:
        max_7 = max(elem, max_7)
    elif elem % 3 == 0:
        max_3 = max(elem, max_3)
        
    max_all = max(max_all, elem)
print(max(max_7 * max_3, max_all * max_21))

