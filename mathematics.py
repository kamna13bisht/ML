#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
height=[170,130,120,170,111]
me = np.mean(height)
me


# In[3]:


height.sort()
med = np.median(height)
med


# In[5]:


import statistics as stat
mo = stat.mode(height)
mo


# In[6]:


v = np.var(height)
v


# In[7]:


sd = np.std(height)
sd


# In[9]:


#import matplotlib.pyplot as plt
import numpy as np
import sympy as sy


def f(x):
	return x**2

x = sy.Symbol("x")
print(sy.integrate(f(x), (x, 0, 2)))


# In[ ]:





# In[ ]:





# In[11]:


import sympy as sy


def f(x):
	return x**2

x = sy.Symbol("x")
print(sy.integrate(f(x), (x, 0, 2)))


# In[ ]:





# In[12]:


import sympy as sy


def f(x):
	return x**2

x = sy.Symbol("x")
print(sy.integrate(f(x), (x, 0, 2)))


# In[16]:


from sympy import symbols , diff
x = symbols('x')
f = x**3 - 2*x**2 -5*x + 1
f_prime = diff(f,x)
f_prime


# In[ ]:




