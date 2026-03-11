# Mutable Default Argument Concept

def auti (item, lst = []):
    lst.append(item)
    return lst
    
print(auti(1))
print(auti(2))
print(auti(3))

# [1]
# [1, 2]
# [1, 2, 3]


def auti (item, lst = None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst
    
print(auti(1))
print(auti(2))
print(auti(3))

# [1]
# [2]
# [3]

# ---------------------------------



## UnboundLocalError

x = 10

def auti ():
    x = x + 5
    return x

print(auti())
# UnboundLocalError: cannot access local variable 'x' where it is not associated with a value




x = 10

def auti ():
    global x
    x = x + 5
    return x

print(auti())

#15

#--------------------------------------

# List Multiplication Pitfall

lst = [[0]*3]*3
lst[0][0] = 1

print(lst)

# [[1, 0, 0], [1, 0, 0], [1, 0, 0]]


lst = [[0]*3 for _ in range(3) ]
lst[0][0] = 1

print(lst)
# [[1, 0, 0], [0, 0, 0], [0, 0, 0]]


#-----------------------------------------


#Late Binding in Closures

lst = []

for i in range(3):
    lst.append(lambda : i)

print([f() for f in lst])
# [2,2,2]


lst = []

for i in range(3):
    lst.append(lambda i = i: i)

print([f() for f in lst])
#[0,1,2]

#------------------------------------------
    
a = [1,2,3]
b = a
c = a[:]

print(a is b)
print(a is c)
print(a == c)

# True
# False
# True

#----------------------------------------------




