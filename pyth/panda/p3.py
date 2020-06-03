#reverse 
with open("a.txt", 'r') as f:
    a=f.readlines()
    for words in a:
        print(words[::-1])
