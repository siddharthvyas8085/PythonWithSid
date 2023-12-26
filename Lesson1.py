"""
1. Overview of python
2. Reserved word
3. Identifiers
4. Inbuilt data types(Int, float, complex, bool)
5. Operators in python
        Arithemetic operation (+, -, *, /, %, //, **)
        Relational operators for Comparison operators(>, >=, <, <=, ==)
        Logical operators (and, or, not)
        Bitwise operators(&, |, ^, ~, <<, >>)
        Assignment operators(+=, -=, *=, /=, %=, //=, **=, &=, |=, ^=, >>=, <<=)
        Special operators(is, is not)

"""




#%% Dont assign reserved keywords as an identifier
#True = 5 #will affect in future
a=5
print(a==5)

# int = 5
# print("Type: ", int(3))


#%% Identifiers
a = 6
_a = 5
# 4r = 55 #invalid


#%% inbuilt datatypes
#numeric == int,float,complex,bool,byte
cnum = complex(1,3)
cnum2 = 6+6j
print("Complex numbers: ",cnum,type(cnum),cnum2,type(cnum2))


#%% OPERATORS
# ss = 5(44) #error
precedence = 5*(4/4)
print("precedence: ",precedence)
reminder_operator = 23%5
print("reminder operator: ",reminder_operator)

f_division = 23//5
print("floor division: ",f_division)

import numpy as np
k = np.array([1,2,35,7,9])
kk = ((k>3)&(k<99))
print("Bitwise operations: ",kk)

#%% Assignment Operators: repeats ourself
i = 2
i = i+5  #equivalent to i += 5
print(i)

j = 3
j += 2
j += 3
print(j)


# Special operator
r = [6,7,8]
g = [6,7,8]
print("Id of r and g: ",id(r), id(g))
print(r is g)

s1 = 3
s2 = 3
s3 = s1+3
s4 = s2
print(id(s1), id(s2),s3,s4,id(s3), id(s4))



