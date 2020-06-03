#occurences of word
with open("a.txt", 'r') as f:
    inp=input("Enter letter:")
    k=0
    read=f.readlines()
    for word in read:
        if (inp==word):
            k+=1
print(k)