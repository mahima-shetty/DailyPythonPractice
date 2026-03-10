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

# -------------------------------
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



## 
