#!/usr/bin/env python
# coding: utf-8

# In[4]:


money = 1000
value = 1000

for x in range(7):
    value = value + value * 12 / 100

print(value)

kazanc = value - money

print(kazanc)


# In[11]:


print('Hafta başında {} dolarlık bitcoin aldığımızda günde ortalama %12 kazançla,\nbir hafta sonunda {:.2f} dolar kazanırdık'.format(money,kazanc))


# In[13]:


dosya = input('Dosya adını giriniz : ')
print ("Dosyanın adı {}.py".format(dosya))


# In[ ]:




