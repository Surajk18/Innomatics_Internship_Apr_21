#!/usr/bin/env python
# coding: utf-8

# # Q1

# In[6]:


print ("Hello, World!")


# # Q2

# In[ ]:


if __name__ == '__main__':
    a = int(raw_input())
    b = int(raw_input())
    print a+b
    print a-b
    print a*b


# # Q3

# In[ ]:


from __future__ import division

if __name__ == '__main__':
    a = int(raw_input())
    b = int(raw_input())

print(a//b)
print(a/b)


# # Q4

# In[7]:


if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print(i*i)


# # Q5

# In[ ]:


def is_leap(year):
    leap = False
    
    if year%400==0 :
        leap = True;
    elif year%4 == 0 and year%100 != 0:
        leap = True;
    
    return leap


# # Q6

# In[ ]:


from __future__ import print_function

if __name__ == '__main__':
    n = int(raw_input())
    
    for i in range(1,n+1):
        print(i,end='');

