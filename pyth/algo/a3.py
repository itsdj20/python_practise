def selection(lst):
    for a in range(1,len(lst)):
        x=lst[a-1]
        if  x>lst[a]:
            return
            
        

# lst=list(map(int,input("input the no to be sorted").split()))   
lst = [9, 1, 15, 28, 6]
selection(lst)
print(lst)