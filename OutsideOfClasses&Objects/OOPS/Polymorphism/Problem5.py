
# 5. Create a class that overloads:
#   - `__str__()` and `__len__()` to show polymorphic behavior


class Dummy:
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return "Dummy object containing data"

    def __len__(self):
        return len(self.data)

# Testing
d = Dummy([1, 2, 3, 4])

print(d)          # Calls __str__()
print(len(d))     # Calls __len__()
        

