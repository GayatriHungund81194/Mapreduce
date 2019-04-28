#!/usr/bin/env python
# coding: utf-8

# In[6]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
plt.style.use('ggplot')

x = ['200', '206', '302', '304', '404']
energy = [4280, 42, 685, 399, 72]

x_pos = [i for i, _ in enumerate(x)]

plt.bar(x_pos, energy, color='blue')
plt.xlabel("Status Codes")
plt.ylabel("Number of requests for status code")
plt.title("Log Data Visualization")

plt.xticks(x_pos, x)

plt.show()
plt.savefig('foo.png')

# 200     4280
# 206     42
# 302     685
# 304     399
# 404     72
# No      19


# In[ ]:




