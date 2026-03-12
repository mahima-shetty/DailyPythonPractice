# Level 2: Intermediate

# Write a generator that yields Fibonacci numbers up to a given limit
def gen_fibo(n):
    a = 1
    b = 1
    yield a
    yield b
    n -= 2 
    while n != 0 :
        c = a + b
        yield c
        a = b
        b = c
        n -= 1


gen1 = gen_fibo(7)

while True:
    try:
        print(next(gen1))
    except StopIteration:
        pass



# Create a generator that reads a file line by line and yields each line without loading the full file into memory.

def generator(file):
    with open(file, "r") as fi1:
        for i in fi1:
            yield i
        
gen1 = generator("file.txt")

try:
    while True:
        print(next(gen1))
except StopIteration:


    # Write a generator that yields prime numbers within a given range.

num = int(input("Enter number "))
def prime_gen(num):
    is_Prime = True
    for n in range(2, num+1): # 2 3 4 5 6 7 
        for i in range(2, n): # 2 
            if n%i == 0:
                is_Prime =  False
                break
        if is_Prime:
            yield n
        is_Prime = True
p = prime_gen(num)
       
try :
    while True:
        print(next(p))
except StopIteration:
    pass


# Implement a generator that flattens a nested list (one level deep).

lst = [1,[2,3], [4,5,6], 7]
def flatten_lst(lst):
    for item in lst:
        if isinstance(item, int) or isinstance(item, str) :
            yield item
            
        if isinstance(item, list):
            for i in item:
                yield i

g = flatten_lst(lst)
try :
    while True:
        print(next(g))
except StopIteration:
    pass


# Write a generator that yields running cumulative sums of a list.


lst = [1,2,3,4,5,6,7,8,9]

def cum_sum(lst):
    sum = 0
    for i in lst:
        sum += i
        yield sum
        
c = cum_sum(lst)
try :
    while True:
        print(next(c))
except StopIteration:
    pass
