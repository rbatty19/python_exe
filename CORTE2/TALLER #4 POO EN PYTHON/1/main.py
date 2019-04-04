from class1 import *


# Output: 10
print(MyClass.a)

# Output: <function MyClass.func at 0x0000000003079BF8>
print(MyClass.func)

# Output: 'This is my second class'
print(MyClass.__doc__)

ob = MyClass()

# Output: 10
print(ob.a)

# Output: <function ob.func at 0x0000000003079BF8>
print(ob.func)

# Output: 'This is my second class'
print(ob.__doc__)