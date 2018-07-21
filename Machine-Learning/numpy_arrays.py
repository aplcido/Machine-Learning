"""Creating NumPy arrays."""

import numpy as np

def test_run():
   #list to 1D array
   #print (np.array([2,3,4]))
   
   #list to 2D array
   #print (np.array([(2,3,4),(5,6,7)]))
   
   #empty array
   #print np.empty(5)
   #empty matrix
   #print (np.empty((5,4)))
   
   #matrix of 1s
   #print (np.ones((5,4)))
   
   #specifying datatype (int) of matrix of 1s
   #print (np.ones((5,4), dtype=np.int_))
   
   #generate an array full of random numbers, uniformly sampled from [0.0,1.0]
   #print (np.random.random((5,4)))
   
   #sample numbers from a Gaussian (normal) distribution
   print (np.random.normal(size=(2,3))) 
   print (np.random.normal(50,10,size=(2,3))) #change mean to 50 and standard deviation to 10
   
   #random numbers
   print (np.random.randint(0,10, size=5)) #5 random numbers between 0 and 10
   print (np.random.randint(0,10, size=(2,3))) #2x3 size matrix with random numbers between 0 and 10
 
   a = np.random.random((5,4))
   print (a.shape)
   print (a.shape[0]) #number of rows
   print (a.shape[1]) #number of columns
   print (a.size) #number of elements in array/matrix
   
   np.random.seed(693) #seed the random number generator
   a = np.random.randint(0,10, size=(5,4))
   print ("Array:\n",a)
   
   #sum of all elements
   print("Sum of all elements:",a.sum())
   
   #iterate over rows, to compute sum of each column
   print("Sum of each column:",a.sum(axis=0))
   
   #iterate over columns, to compute sum of each row
   print("Sum of each row:",a.sum(axis=1))
   
   #Statistics: min, max, mean (across rows,cols and overall)
   print("Minimum of each column:",a.min(axis=0))
   print("Maximum of each row:",a.max(axis=1))
   print("Mean of all elements:",a.mean())
   

if __name__ == "__main__":
    test_run()