#%%
# data Structure
# 1. List
# 2. tuple
# 3. Dict
# 4. Range
# 5. Set
import numpy as np


#%%
l = [1,2,3]
# l1 = ['a','b','c']
# l2 = [1,'a1']
# l3 = [(1,2),(3,4)]
# l3 = [{"A", 2},{"B",4}]
# l = list([1,2,3])

#%% Methos of list

## 1. append(): append the value at the end
# print(l.clear())
l.append(4)
# print(l)
# # print(l.append(4))

fruits = ['apple', 'banana', 'cherry']
fruits.append("orange")

# print(fruits)


# 2. insert: insert the value at defined index
fruits = ['apple', 'banana', 'cherry']
fruits.insert(2,4)#(index,item)
# print(fruits)


## Q. cummulative sum
li = [1,3,5,6,7,8]
li1 = [1]
for item in li:
    if item==li[0]:
        continue
    else:
        li2 = li1[-1]+item
        li1.append(li2)
# print(li1)


## Q. sum of all elements
li1=0
for item in li:
    li1 = li1+item
# print(li1)

# 3. clear : clear all values
ll = [1,2,3]
ll.clear()
# print(ll)

# 4. copy(): copy the entire list
l22 = [2,3,4,2,2]
ll33 = l22

ll4 = l22.copy()
print(id(l22),id(ll33),id(ll4))

# 5. count: counts the defined element
print(l22.count(2))

f_str = 'jayavardhan'
str_j = []
for l in f_str:
    str_j.append(l)
# print(str_j)
print(str_j.count('a'))

# 6. index: index of first appearance of defined element
print(str_j.index('a'))


# 7. pop: remove the value
print(str_j.pop())# remove from end
print(str_j)
print(str_j.pop(-2))#remove from -2 index
print(str_j)

# 8. remove# remove the element
str_j.remove('a')
# print(str_j)
for j in str_j:
    if j == 'a':
        str_j.remove('a')
# print(str_j)
while 'a' in str_j:
    str_j.remove('a')
# print(str_j)

# 9. REVERSE : reverse the order of list
str_j.reverse()
print(str_j)

# 10. sort : sort the values
k = [1,7,3,8,2]
k.sort(reverse=False)


names = ["anindita","richa","sid","jay","anant","richy"]
names.sort(reverse=True)
# print(names)

# 11. Extend : merge the lists
fruits = ['apple', 'banana', 'cherry']
cars = ['Ford', 'BMW', 'Volvo']
fruits.extend(cars)
# print(fruits)

#%% Indexing of list
arr = [1,3,5,8,0,9]
p = arr[2:]
# print(p)

arr_2d = np.array([[1,2,3],[2,3,4],[5,6,7]])
# print(arr_2d)
p = arr_2d[1:3,0]
# print(p)

# 12. len: length of list or number of present element
lis = [2,5,8]
# print(len(lis))

