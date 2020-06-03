#buuble sort

def bubble(lst):
    swap=True   
    while swap:
        swap=False
        for i in range(len(lst)-1):
            if lst[i]>lst[i+1]:
                lst[i],lst[i+1]=lst[i+1],lst[i]
                swap=True   
            
a=[21,22,4,64,34]
bubble(a)
print(a)
