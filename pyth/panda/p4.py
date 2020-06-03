#count line
with open("a.txt", 'r') as f:
    a=f.readlines()
    x=0
    for lines in a:
        x+=1
print(x)
