#printing occurences of a no in an array
import numpy as np 
arr=np.array([10,20,10,20,30,40,50,60,50,40,30,20,10,0])
print(np.count_nonzero(arr==10))
print(np.count_nonzero(arr==20))
print(np.count_nonzero(arr==30))

print(np.count_nonzero(arr==40))
print(np.count_nonzero(arr==50))
print(np.count_nonzero(arr==60))
print(np.count_nonzero(arr==0))