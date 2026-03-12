# Level 3: Advanced

# Write an infinite generator that yields powers of 2 and stops externally using next().

def inf_2 ():
    n = 0
    while True:
        yield 2 ** n
        n += 1

i = inf_2()

print(next(i))
print(next(i))
print(next(i))
