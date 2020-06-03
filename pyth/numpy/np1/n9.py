import numpy as np
m,n=map(int,input().split())
arr1 =np.zeros((m,n),int)
arr2 =np.zeros((m,n),int)
for i in range(n):
    arr1[i]=list(map(int,input().split()))
for i  in range(n):
    arr2[i]=list(map(int,input().split()))

print(arr1+arr2))
print(arr1-arr2)
print(arr1*arr2)
print(arr1/arr2)
print(arr1%arr2)