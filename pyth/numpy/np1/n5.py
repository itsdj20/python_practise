#saving as csv
import numpy as np 
data=np.asarray([[10,20,30],[40,50,60],[70,80,90]],dtype=np.int16)
np.savetxt("test.csv",data,delimiter=",")