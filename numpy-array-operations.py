#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install jovian --upgrade -q')


# In[2]:


import jovian


# In[3]:


jovian.commit(project='numpy-array-operations')


# Let's begin by importing Numpy and listing out the functions covered in this notebook.

# In[4]:


import numpy as np


# In[5]:


# List of functions explained 
function1 = np.eye()  
function2 = np.array()
function3 = np.reshape()
function4 = np.insert()
function5 = np.round()


# ## Function 1 - np.eye()
# 
# Returns 2D array with all diagonal element 1 and 0 else.

# In[ ]:


# Example 1 
np.eye(3,dtype = int)


# Return (3,3) 2D identity metrix with int data type

# In[ ]:


# Example 2 - working
np.eye(N=3,M=3,k=-1)


# Return (3,3) 2D metrix . k refers to diagonal by defult it is 0.If value of k is positve means upper diagonal and negitve means lower diagonal. 
# if you take -1 diagonal shifts one point downwards.
# and +2 means diagonal shifts two steps upwards.

# In[ ]:


# Example 3 - breaking 
np.eye(-3)


# It breaks because negative dimensions are not allowed. N,M can be positive int and 0
# try np.eye(0)

# np.eye is useful when we want metrix with prifered diagonal that's element is one.

# In[ ]:


jovian.commit()


# ## Function 2 - np.array()
# It helps to convert python list into Numpy array. by doing this we can use numpy's facilities.

# In[6]:


# Example 1 - working
arr1 = [1,2,3]
np.array(arr1)


# Convert list into 1-D array (array--have same with same datatypes. that's why array is diffrent from list.

# In[7]:


# Example 2 - working
arr2 = [[1,2,3],[4,5,6]]
np.array(arr2,dtype = complex)


# Gives 2-D array with complex datatype.

# In[8]:


# Example 3 - breaking
arr3= np.array(1,2,8,4)


# Here we want arr3 = [1,2,8,4] for that we should pass list of elements as argument.

# This function useful to use Numpy fanctionality. By creating list---> Numpy-array.

# In[9]:


jovian.commit()


# ## Function 3 - np.reshape()
# 
# It changes array's shape in define shape. 

# In[10]:


# Example 1 - working
arr4 = np.array([[1,2],[8,9],[45,56]])
arr4.reshape(2,3)


# before reshape shape of arr4 is (3,2) after reshape shape is (2,3)

# In[11]:


# Example 2 - working
arr5 = np.array([[[1,2,3],[7,8,9]],[[4,5,6],[9,8,10]]])
arr5.reshape(4,3)


# before reshape shape of arr4 is (2,2,3) and a 3D array 
# after reshape shape is (4,3) and a 2D array.

# In[12]:


# Example 3 - breaking
arr5.reshape(12)


# size is arr5 is 12 so you can only reshape it in multiplied of 12 like: (2,6), (3,2,2), (12,1)`[2D array]`,(12)`[1D array]`.

# It is useful when you want array in form ofspecific rows or colummns.

# In[13]:


jovian.commit()


# ## Function 4 - np.insert()
# 
# It is same like insert mathod in list you can add element at specified index

# In[14]:


# Example 1 - working
a=np.arange(12)
np.insert(a,5,10)


# At index number 5 value 10 is inserted

# In[15]:


# Example 2 - working
b = np.arange(12).reshape((3,4))
np.insert(b,1,10,axis=0)


# Here See that one `row` is added at index 1 because `axis=0`.
# If axis=1 it will be added as column
# --> Notice that here brodcasting is done by numpy.
# 

# In[16]:


# Example 3 - breaking (to illustrate when it breaks)
C = np.arange(5)
np.insert(C,1,10,11,axis=0)


# here we want to insert 10,11 at index 5 but numpy understand that it as argument.
# To fix it you can pass list of elements as inserting argument `[10,11]`
# Output:
# array([ 0, 10, 11,  1,  2,  3,  4])
# 
# 

# Some closing comments about when to use this function.

# In[ ]:


jovian.commit()


# ## Function 5 - np.round()
# 
# It is helpful when we want to round every item in array

# In[17]:


# Example 1 - working
arr1 = np.linspace(0,5.5,10)
np.around(arr1)


# Here`around` is rounding to 0 decimal value
# Note: Numpy Rounded to Nearest even value.

# In[18]:


# Example 2 - working
arr2 = np.array([0.899,1.785,2.56,6.7895,0.4785])
arr3 = np.around(arr2,2)
arr3


# Function is rounding values to two decimal points.

# In[19]:


# Example 3
arr4 = np.array([4.5,5,6.7,2.96,2.3,5.369,5.421])
arr5 = np.around(arr4,-1)
arr5               


# Here it is not breaking but we can get idea that if we gave value like 4.5 and want to rond it by one decimal point in negative side it will give `0.`

# *Remember :- `around` is diffrent from `floor` and `Celi`
# 

# In[20]:


jovian.commit()


# ## Conclusion
# 
# There are 5 function of Numpy is discussed. There are many Function in Numpy. When we need specific funtion, we can search for it and learn it. 

# ## Reference Links
# Provide links to your references and other interesting articles about Numpy arrays:
# * Numpy official tutorial : https://numpy.org/doc/stable/user/quickstart.html
# * ...

# In[21]:


jovian.commit()


# In[22]:


jovian.submit(assignment="zero-to-pandas-a2")


# In[ ]:




