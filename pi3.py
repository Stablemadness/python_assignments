import copy
list1 = [1, 1, 1, 2, 3, 4]
list2 = [4,3,2,1,6]
if list1 == list2:
    print('equals')
if list1 < list2:
    print('list1 less than list2')
print(list1, list2)
list2.sort()
print(list2)
if list1 == list2:
    print('equals')
if list1 > list2:
    print('list1 greater than 2')
if list2 > list1:
    print('list2 bigger')
list3 = []
list3 = list2.copy()
for item in list1:
    list2.remove(item)

print(list2, list3)
print(list3.index(9))
print('fin')
