#word count
with open("a.txt", 'r') as f:
    a=f.read().split()
    x=0
    for lines in a:
        x+=1
print(x)
