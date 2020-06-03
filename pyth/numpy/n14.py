#print 10x10 matrix with 1 on border
import numpy as np 
r= np.ones((10,10))
r[1:-1,1:-1]=0
print(r)