def calpieboi(x):
    string = x
    substring = "C"
    count = string.count(substring)
    return count
    
# räkna hur många capital letters det är i

print(calpieboi("ClaClaClaClap!"))
print(calpieboi("ClClClaClaClaClap!"))
print(calpieboi("CCClaClClap!Clap!ClClClap!"))