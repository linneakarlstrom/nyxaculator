def hello_world(x):
    if x % 15 == 0:
        return "Hello world"
    elif x % 3 == 0:
        return "Hello"
    return "world"
       
   


print(hello_world(3))
print(hello_world(4))
print(hello_world(15))