# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 11:32:28 2019

@author: l
"""

# Python program to demonstrate  
# basic array characteristics 
import numpy as np 

  
# Creating array object 
arr = np.array( [[ 1, 2, 3], 
                 [ 4, 2, 5]] ) 
  
# Printing type of arr object 
print("Array is of type: ", type(arr)) 
  
# Printing array dimensions (axes) 
print("No. of dimensions: ", arr.ndim) 
  
# Printing shape of array 
print("Shape of array: ", arr.shape) 
  
# Printing size (total number of elements) of array 
print("Size of array: ", arr.size) 
  
# Printing type of elements in array 
print("Array stores elements of type: ", arr.dtype) 

#creating array
b = np.array((1 , 3, 2)) 
print ("\nArray created using passed tuple:\n", b)
 # Creating a 3X4 array with all zeros 
c = np.zeros((2, 2)) 
print ("\nAn array initialized with all zeros:\n", c) 
# Create a sequence of integers  
# from 0 to 30 with steps of 5 
f = np.arange(0, 30, 5) 
print ("\nA sequential array with steps of 5:\n", f) 

#array manipulation
a = np.array([1, 2, 5, 3]) 
print ("Adding 1 to every element:", a+1) 
print ("Subtracting 3 from each element:", a-3) 
print ("Multiplying each element by 10:", a*10) 
print ("Squaring each element:", a**2) 
a *= 2
print ("Doubled each element of original array:", a)  
a = np.array([[1, 2, 3], [3, 4, 5], [9, 6, 0]]) 
print ("\nOriginal array:\n", a) 
print ("Transpose of array:\n", a.T) 
print ("Largest element is:", arr.max()) 
print ("Column-wise minimum elements:", 
                        arr.min(axis = 0)) 
print ("Cumulative sum along each row:\n", 
                        arr.cumsum(axis = 1))

#pandas

  
dict = {"country": ["Brazil", "Russia", "India", "China", "South Africa"],
       "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
       "area": [8.516, 17.10, 3.286, 9.597, 1.221],
       "population": [200.4, 143.5, 1252, 1357, 52.98] }

import pandas as pd
a = pd.DataFrame(dict)
print(a)


  