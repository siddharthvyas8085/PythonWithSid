## Tuple methods
## tuple ()
t = (1,2,1)
lt = [t]
print(type(lt),lt)
print(type(t))

l = [1,2,3]
l[0] = 4
# print(l)
# t[0] =4 #ERROR
# print(t)

# 1. count
print(t.count(1))

# 2. index
print(t.index(2))

print(t[1])
t2 = (1,'e')
print(t2)
ll = list([1,2,3])
print(ll)

t3 = set([1,2,3])
print(t3)


#%%
# set
s1 = {1,2,3}
print(s1,type(s1))

s2 = {1,2,3,1,3,2,3}
# print(s2)

## set methods
s3 = set([4,6,2])
# 1. union
print(s2.union(s3))

# 2. intersection
print(s2.intersection(s3))

# 3. add
s2.add(6)
s2.add(5)
# print(s2)

# 4. clear
# s2.clear()
# print(s2)

# 5. copy
s4 = s2.copy()
# print(s4)

# 6. diffrence
# print(s2,s3)
# print(s2.difference(s3))

# 7. diffrence_update
s2.difference_update(s3)
# print(s2)

# 8. discard
s2.discard(1)
# print(s2)

# 9. issubser
print(set([]).issubset(s2))

# 10. pop
s2.pop()
# print(s2)

# 11. update
s2.update(s3)
# print(s2)

# 12. symmetric
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple","ee"}

z = x.symmetric_difference(y)

# print(z)

#%% dict(keys:value)
# d1 = dict({"c1":1,"c2":2})
d1 = dict({"name":["richa",'anin','jay'],"EN":[1,2,3],"Marks":[9,8,7]})
# import pandas as pd
# df = pd.DataFrame(d1)
# print(d1["Marks"])
# print(df)
# print(type(d1),d1)

