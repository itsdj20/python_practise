def selection(lst):
    for a in range(len(lst)):
        x=min(lst)
        lst2.append(x)
        lst.remove(x)

lst=list(map(int,input("input the no to be sorted").split()))   
lst2=[]
selection(lst)
print(lst2)