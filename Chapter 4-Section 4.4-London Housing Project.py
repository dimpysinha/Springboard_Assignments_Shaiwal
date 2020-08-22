#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd # import pandas
import numpy as np # import numpy
import matplotlib.pyplot as plt # import matplotlib


# In[2]:


url_LondonHousePrices = "https://data.london.gov.uk/download/uk-house-price-index/70ac0766-8902-4eb5-aab5-01951aaed773/UK%20House%20price%20index.xls"

properties = pd.read_excel(url_LondonHousePrices, sheet_name = 'Average price', index_col = None)


# In[3]:


properties.head()


# In[4]:


properties = properties.transpose()
properties.head(5)


# In[5]:


properties.index


# In[6]:


properties = properties.reset_index()
properties.index


# In[7]:


properties.head()


# In[8]:


properties.columns


# In[9]:


properties.columns = properties.iloc[0]
properties.head()


# In[10]:


properties.drop(0)


# In[11]:


properties = properties.rename(columns = {'Unnamed: 0' : 'BOROUGHS_LONDON', pd.NaT : 'CITY_ID'})
properties.drop(0)


# In[12]:


properties_1 = pd.melt(properties, id_vars = ['BOROUGHS_LONDON','CITY_ID'])
properties_1.head()


# In[13]:


properties_1.drop(0)


# In[14]:


properties_1 = properties_1.rename(columns = {0 : 'Month', 'value' : 'Average Price'})
properties_1.head()


# In[15]:


properties_1.drop(0)


# In[16]:


properties_1.shape


# In[17]:


properties_1.describe()


# In[18]:


properties_1 = properties_1.dropna(how='any',axis=0)
properties_1.describe()


# In[19]:


properties_1.dtypes


# In[20]:


properties_1['Average Price'] = pd.to_numeric(properties_1['Average Price'])
properties_1.dtypes


# In[21]:


properties_1.count()


# In[22]:


properties_1.shape


# In[23]:


properties_1.head()


# In[24]:


City_of_London_Prices = properties_1[properties_1['BOROUGHS_LONDON'] == 'City of London']
City_of_London_Prices.head()


# In[25]:


CoL_LC = City_of_London_Prices.plot.line(x = 'Month', y = 'Average Price', color = 'green', style = '+-')
CoL_LC.set_ylabel('Average Price')
plt.show()


# In[26]:


properties_1['Year'] = properties_1['Month'].apply(lambda t: t.year)
properties_1.head()


# In[27]:


prop_2 = properties_1.groupby(by = ['BOROUGHS_LONDON', 'Year']).mean()
prop_2.tail()


# In[28]:


Y_H_Prices = prop_2[prop_2['BOROUGHS_LONDON'] == 'YORKS & THE HUMBER']
Y_H_LC = Prop_2.plot.line(x = 'Month', y = 'Average Price', color = 'red', style = '*-')
Y_H_LC.set_ylabel('Average Price')
plt.show()


# In[29]:


prop_2.sample(15)


# In[30]:


prop_2 = prop_2.reset_index()
prop_2.head()


# In[31]:


def create_price_ratio(i):
    Year_1998 = float(i['Average Price'][i['Year'] == 1998])
    Year_2018 = float(i['Average Price'][i['Year'] == 2018])
    Price_Ratio = [Year_2018/Year_1998]
    return Price_Ratio


# In[32]:


create_price_ratio(prop_2[prop_2['BOROUGHS_LONDON']=='Barking & Dagenham'])


# In[33]:


Final = {}

for X in prop_2['BOROUGHS_LONDON'].unique():
    BOROUGH = prop_2[prop_2['BOROUGHS_LONDON'] == X]
    Final[X] = create_price_ratio(BOROUGH)
    
print(Final)


# In[34]:


Final_Ratios = pd.DataFrame(Final)
Final_Ratios.head()


# In[35]:


Final_Ratios_Tr = Final_Ratios.transpose()
Final_Ratios = Final_Ratios_Tr.reset_index()
Final_Ratios.head()


# In[36]:


Final_Ratios.rename(columns = {'index' : 'BOROUGH', 0 : '2018'}, inplace = True)
Final_Ratios.head()


# In[39]:


Top15_Boroughs = Final_Ratios.sort_values(by = '2018', ascending = False).head(15)
print(Top15_Boroughs)


# In[59]:


Top15_Chart = Top15_Boroughs[['BOROUGH','2018']].plot(kind = 'bar')

plt.show()


# In[ ]:




