# 4. finally Block

# Write a program where:

# A file is opened and read

# The file is always closed using finally



try:
    f = open("main_test.py", "r")
    content = f.read()
    print("File is opened")

except FileNotFoundError:
    print("No file")

finally:
    if 'f' in locals():
        f.close()
        print("Closed main_test.py")
