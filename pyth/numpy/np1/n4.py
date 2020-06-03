#finding unique elements and their counts
import numpy as np 
arr=np.array([[10,10,30,20,40,50,20,30,30,50,60,40]])
unique_elements,counts=np.unique(arr,return_counts=True)
print(np.asarray((unique_elements,counts)))
