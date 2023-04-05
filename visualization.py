#!/usr/bin/env python
# coding: utf-8

# In[18]:


import  matplotlib.pyplot as pit
get_ipython().run_line_magic('matplotlib', 'inline')


# In[19]:


import numpy as np


# In[20]:


import pandas as pd


# In[21]:


mp=pd.read_csv("C:\\Users\\aedpu\\OneDrive\\Desktop\\Pokemon (1).csv")


# In[22]:


mp


# In[23]:


mpp=mp.head()


# In[24]:


mpp


# In[25]:


pit.scatter(mpp['Speed'],mpp['Total'])


# In[26]:


pit.bar(mpp['Speed'],mpp['Total'])


# In[27]:


pit.plot(mpp['Speed'],mpp['Total'])


# In[28]:


pit.plot(mpp['Speed'],mpp['Total'],linestyle='dashed')


# In[29]:


pit.plot(mpp['Speed'],mpp['Total'],linestyle='dotted')


# In[30]:


pit.pie(mpp['Speed'],labels=mpp['Total'])


# In[31]:


pip install seaborn


# In[32]:


import seaborn as sbn


# In[33]:


import numpy as np


# In[34]:


time=np.arange(0,1000,0.5)


# In[35]:


time


# In[36]:


pit.plot(mpp['Speed'],mpp['Total'])


# In[37]:


sbn.displot(mp['Attack'])


# In[38]:


mpp


# In[39]:


sbn.set(style='darkgrid')


# In[40]:


sbn.displot(mp["HP"])


# In[41]:


sbn.relbolt(x='Name',y='Attack',data=mpp,col='Speed',hue="Total",style='HP',kind='')sbn.relbolt(x='Name',y='Attack',data=y,col='Speed',hue="Total",style='HP',kind='Defense')


# In[42]:


sbn.catplot(x='Speed',y='Total',kind='box',data=mpp)


# In[43]:


sbn.regplot(x='Speed',y='Total',data=mpp)


# In[47]:


sbn.pairplot(mpp)


# In[48]:


sbn.pairplot(mp,hue='HP',palette='Set1')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




