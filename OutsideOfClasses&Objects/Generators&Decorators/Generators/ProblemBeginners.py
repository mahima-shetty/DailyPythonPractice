# Generators — Coding Problems
# Level 1: Beginner


# Write a generator function that yields numbers from 1 to N.



def generator(n):
    for i in range(1, n+1):
        yield i

gen = generator(7)

print(next(gen))
print(next(gen))



# Write a generator that yields even numbers up to a given limit.

n = int(input("take a number "))

def generator (n):
    for i in range (1, n+1):
        if i % 2 == 0:
            yield i
        


gen1 = generator(n)
print(next(gen1))
print(next(gen1))
print(next(gen1))



# Create a generator that yields characters of a string one by one.

# string1 = "water"

def generator2(string):
    for i in string:
        yield i
        
gen2 = generator2(string1)

try :
    while True:
        print(next(gen2))
except StopIteration:
    pass




# Write a generator that yields the square of numbers from 0 to 9.

def generator3():
    for i in range (10):
        yield i * i

gen3 = generator3()

try:
    while True:
        print(next(gen3))
except StopIteration:
    pass



# Convert a list comprehension that generates cubes of numbers into a generator expression.

n = int(input("Take a number:  "))

gen_comp = (i**3 for i in range(1, n+1))


try:
    while True:
        print(next(gen_comp))
except StopIteration:
    pass



