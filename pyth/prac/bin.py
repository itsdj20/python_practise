def bin(f,l,x,y):
    m=int((f+l)/2)
    if y==x[m]:
        print("found at",m,"posion")
    elif y<x[m]:
        return bin(f,m-1,x,y)
    elif y!=x[m]:
        print(y,"not in list")
    else:
        return bin(m+1,l,x,y) 
    

x=eval(input("enter sorted elemnts\n"))
y=eval(input("enter the number to be searched"))

f=0
l=len(x)

bin(f,l,x,y)