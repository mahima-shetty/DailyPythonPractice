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
    pass
    
