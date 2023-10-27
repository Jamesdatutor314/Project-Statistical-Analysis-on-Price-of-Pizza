#!/usr/bin/env python
# coding: utf-8

# In[219]:


import pandas as pd
import numpy as np
import scipy.stats as stats
import random as r
import matplotlib.pyplot as plt
import seaborn as sns
import scipy as sp
import random as r

# ignore stupid warnings
import warnings
warnings.filterwarnings('ignore')


# In[220]:


df = pd.read_csv('pizza_data.csv')
df.head()


# In[221]:


df.isnull().sum()


# In[222]:


df.dtypes


# Good dataset but now I want pizza
# 
# summarize price first then summarize it by company
# 
# then you can look for relationships between price and other factors such as size

# In[223]:


len(df['Price'].unique())


# In[224]:


df['Price'].unique()


# In[225]:


df[df['Company'] == "Domino's Pizza"]['Type'].unique()


# In[226]:


df[df['Company'] == "Godfather's Pizza"]['Type'].unique()


# In[227]:


df[df['Company'] == "IMO's Pizza"]['Type'].unique()


# In[228]:


df[df['Company'] == "Pizza Hut"]['Type'].unique()


# ## 1.) Delete dollar signs and conver price to float

# In[229]:


df = pd.read_csv('pizza_data.csv')
df.head()


# In[230]:


for i,j in enumerate(df['Price']):
    df['Price'][i] = df['Price'][i][1:]

df['Price'] = pd.to_numeric(df['Price'])
df.head()


# ## 2.) Converting Size To Inches

# In[231]:


df['Diameter(inches)'] = 'n/a'
df.head()


# In[232]:


df[df['Company'] == "Domino's Pizza"]['Size'].unique()


# In[233]:


df[df['Company'] == "Godfather's Pizza"]['Size'].unique()


# In[234]:


df[df['Company'] == "IMO's Pizza"]['Size'].unique()


# In[235]:


df[df['Company'] == "Pizza Hut"]['Size'].unique()


# In[236]:


pizza_inches = {'Small (10")':10, 'Medium (12")':12, 'Large (14")':14, 'X-Large (16")':16, # Domino
                'Mini':6, 'Small':10, 'Medium':12, 'Large':14, 'Jumbo':18, # godfather
                'X Large (16")':16, # IMO
                'Medium':12, 'Large':14, 'Personal':6, 'Small':8 } # pizza hut
                


# In[237]:


df['Diameter(inches)'] = df['Size'].map(pizza_inches)
df.head()


# ## 3.) Condensing the Pizza name into 8 toppings

# In[ ]:





# In[238]:


pizza_name_cat = {'Hand Tossed':'cheese',
        'Handmade Pan':'cheese',
        'Crunchy Thin Crust':'cheese',
       'Brooklyn Style':'cheese',
        'Gluten Free Crust':'cheese',
       'Spinach & Feta (Hand Tossed or Thin Crust)':'other',
       'Spinach & Feta (Hand Tossed, Handmade Pan or Thin Crust)':'other',
       'Spinach & Feta (Hand Tossed, Thin Crust or Brooklyn Style)':'other',
       'Spinach & Feta (Brooklyn Style)':'other',
       'Spinach & Feta (Gluten Free Crust)':'other',
       'Wisconsin 6 Cheese (Hand Tossed or Thin Crust)':'other',
       'Wisconsin 6 Cheese (Hand Tossed, Handmade Pan or Thin Crust)':'other',
       'Wisconsin 6 Cheese (Hand Tossed, Thin Crust or Brooklyn Style)':'other',
       'Wisconsin 6 Cheese (Brooklyn Style)':'other',
       'Wisconsin 6 Cheese (Gluten Free Crust)':'other',
       'Honolulu Hawaiian (Hand Tossed or Thin Crust)':'hawaiian',
       'Honolulu Hawaiian (Hand Tossed, Handmade Pan or Thin Crust)':'hawaiian',
       'Honolulu Hawaiian (Hand Tossed, Thin Crust or Brooklyn Style)':'hawaiian',
       'Honolulu Hawaiian (Brooklyn Style)':'hawaiian',
       'Honolulu Hawaiian (Gluten Free Crust)':'hawaiian',
       'Philly Cheese Steak (Hand Tossed or Thin Crust)':'other',
       'Philly Cheese Steak (Hand Tossed, Handmade Pan or Thin Crust)':'other',
       'Philly Cheese Steak (Hand Tossed, Thin Crust or Brooklyn Style)':'other',
       'Philly Cheese Steak (Brooklyn Style)':'other',
       'Philly Cheese Steak (Gluten Free Crust)':'other',
       'Pacific Veggie (Hand Tossed or Thin Crust)':'veggie',
       'Pacific Veggie (Hand Tossed, Handmade Pan or Thin Crust)':'veggie',
       'Pacific Veggie (Hand Tossed, Thin Crust or Brooklyn Style)':'veggie',
       'Pacific Veggie (Brooklyn Style)':'veggie',
       'Pacific Veggie (Gluten Free Crust)':'veggie',
       'Cali Chicken Bacon Ranch™ (Hand Tossed or Thin Crust)':'other',
       'Cali Chicken Bacon Ranch™ (Hand Tossed, Handmade Pan or Thin Crust)':'other',
       'Cali Chicken Bacon Ranch™ (Hand Tossed, Thin Crust or Brooklyn Style)':'other',
       'Cali Chicken Bacon Ranch™ (Brooklyn Style)':'other',
       'Cali Chicken Bacon Ranch™ (Gluten Free Crust)':'other',
       'Fiery Hawaiian™ (Hand Tossed or Thin Crust)':'hawaiian',
       'Fiery Hawaiian™ (Hand Tossed, Handmade Pan or Thin Crust)':'hawaiian',
       'Fiery Hawaiian™ (Hand Tossed, Thin Crust or Brooklyn Style)':'hawaiian',
       'Fiery Hawaiian™ (Brooklyn Style)':'hawaiian',
       'Fiery Hawaiian™ (Gluten Free Crust)':'hawaiian',
       'Buffalo Chicken (Hand Tossed or Thin Crust)':'chicken',
       'Buffalo Chicken (Hand Tossed, Handmade Pan or Thin Crust)':'chicken',
       'Buffalo Chicken (Hand Tossed, Thin Crust or Brooklyn Style)':'chicken',
       'Buffalo Chicken (Brooklyn Style)':'chicken',
       'Buffalo Chicken (Gluten Free Crust)':'chicken',
       'Memphis BBQ Chicken (Hand Tossed or Thin Crust)':'chicken',
       'Memphis BBQ Chicken (Hand Tossed, Hnadmade Pan or Thin Crust)':'chicken',
       'Memphis BBQ Chicken (Hand Tossed, Thin Crust or Brooklyn Style)':'chicken',
       'Memphis BBQ Chicken (Brooklyn Style)':'chicken',
       'Memphis BBQ Chicken (Gluten Free Crust)':'chicken',
       "America's Favorite Feast® (Hand Tossed or Thin Crust)":'other',
       "America's Favorite Feast® (Handmade Pan)":'other',
       "America's Favorite Feast® (Hand Tossed, Thin Crust or Brooklyn Style)":'other',
       "America's Favorite Feast® (Brooklyn Style)":'other',
       "America's Favorite Feast® (Gluten Free Crust)":'other',
       'Bacon Cheeseburger Feast® (Hand Tossed or Thin Crust)':'bacon cheeseburger',
       'Bacon Cheeseburger Feast® (Handmade Pan)':'bacon cheeseburger',
       'Bacon Cheeseburger Feast® (Hand Tossed, Thin Crust or Brooklyn Style)':'bacon cheeseburger',
       'Bacon Cheeseburger Feast® (Brooklyn Style)':'bacon cheeseburger',
       'Bacon Cheeseburger Feast® (Gluten Free Crust)':'bacon cheeseburger',
       'Deluxe Feast® (Hand Tossed or Thin Crust)':'supreme',
       'Deluxe Feast® (Handmade Pan)':'supreme',
       'Deluxe Feast® (Hand Tossed, Thin Crust or Brooklyn Style)':'supreme',
       'Deluxe Feast® (Brooklyn Style)':'supreme',
       'Deluxe Feast® (Gluten Free Crust)':'supreme',
       'ExtravaganZZa Feast® (Hand Tossed or Thin Crust)':'supreme',
       'ExtravaganZZa Feast® (Hand Tossed, Handmade Pan or Thin Crust)':'supreme',
       'ExtravaganZZa Feast® (Hand Tossed, Thin Crust or Brooklyn Style)':'supreme',
       'ExtravaganZZa Feast® (Brooklyn Style)':'supreme',
       'ExtravaganZZa Feast® (Gluten Free Crust)':'supreme',
       'MeatZZa Feast® (Hand Tossed or Thin Crust)':'meat',
       'MeatZZa Feast® (Hand Tossed, Handmade Pan or Thin Crust)':'meat',
       'MeatZZa Feast® (Hand Tossed, Thin Crust or Brooklyn Style)':'meat',
       'MeatZZa Feast® (Brooklyn Style)':'meat',
       'MeatZZa Feast® (Gluten Free Crust)':'meat',
       'Ultimate Pepperoni Feast™ (Hand Tossed or Thin Crust)':'pepperoni',
       'Ultimate Pepperoni Feast™ (Hand Tossed, Handmade Pan or Thin Crust)':'pepperoni',
       'Ultimate Pepperoni Feast™ (Hand Tossed, Thin Crust or Brooklyn Style)':'pepperoni',
       'Ultimate Pepperoni Feast™ (Brooklyn Style)':'pepperoni',
       'Ultimate Pepperoni Feast™ (Gluten Free Crust)':'pepperoni',
                  
        'Cheese (Original Crust)':'cheese',
        'Cheese (Original or Golden Crust)':'cheese',
       'Cheese (Original, Golden or Thin Crust)':'cheese',
       'Cheese (Mozza-Loaded Crust)':'cheese',
        'Cheese (Original or Thin Crust)':'cheese',
       'All-Meat Combo Pizza (Original Crust)':'meat',
       'All-Meat Combo Pizza (Original or Golden Crust)':'meat',
       'All-Meat Combo Pizza (Original, Golden or Thin Crust)':'meat',
       'All-Meat Combo Pizza (Mozza-Loaded Crust)':'meat',
       'Bacon Cheeseburger Pizza (Original Crust)':'bacon cheeseburger',
       'Bacon Cheeseburger Pizza (Original or Golden Crust)':'bacon cheeseburger',
       'Bacon Cheeseburger Pizza (Original, Golden or Thin Crust)':'bacon cheeseburger',
       'Bacon Cheeseburger Pizza (Mozza-Loaded Crust)':'bacon cheeseburger',
       'Bacon Cheeseburger Pizza (Original or Thin Crust)':'bacon cheeseburger',
       'Taco Pie Pizza (Original Crust)':'other',
       'Taco Pie Pizza (Original or Golden Crust)':'other',
       'Taco Pie Pizza (Original, Golden or Thin Crust)':'other',
       'Taco Pie Pizza (Mozza-Loaded Crust)':'other',
       'Taco Pie Pizza (Original or Thin Crust)':'other',
       'Classic Combo Pizza (Original Crust)':'supreme',
       'Classic Combo Pizza (Original or Golden Crust)':'supreme',
       'Classic Combo Pizza (Original, Golden or Thin Crust)':'supreme',
       'Classic Combo Pizza (Mozza-Loaded Crust)':'supreme',
       'Classic Combo Pizza (Original or Thin Crust)':'supreme',
       'Humble Pie Pizza (Original Crust)':'other',
       'Humble Pie Pizza (Original or Golden Crust)':'other',
       'Humble Pie Pizza (Original, Golden or Thin Crust)':'other',
       'Humble Pie Pizza (Mozza-Loaded Crust)':'other',
       'Humble Pie Pizza (Original or Thin Crust)':'other',
       'Veggie Pie Pizza (Original Crust)':'veggie',
       'Veggie Pie Pizza (Original or Golden Crust)':'veggie',
       'Veggie Pie Pizza (Original, Golden or Thin Crust)':'veggie',
       'Veggie Pie Pizza (Mozza-Loaded Crust)':'veggie',
       'Veggie Pie Pizza (Original or Thin Crust)':'veggie',
       'Hot Stuff Pizza (Original Crust)':'other',
       'Hot Stuff Pizza (Original or Golden Crust)':'other',
       'Hot Stuff Pizza (Original, Golden or Thin Crust)':'other',
       'Hot Stuff Pizza (Mozza-Loaded Crust)':'other',
       'Hot Stuff Pizza (Original or Thin Crust)':'other',
       'Hawaiian Pizza (Original Crust)':'hawaiian',
       'Hawaiian Pizza (Original or Golden Crust)':'hawaiian',
       'Hawaiian Pizza (Original, Golden or Thin Crust)':'hawaiian',
       'Hawaiian Pizza (Mozza-Loaded Crust)':'hawaiian',
       'Hawaiian Pizza (Original or Thin Crust)':'hawaiian',
       'BLT Pizza (Original Crust)':'other',
       'BLT Pizza (Original or Golden Crust)':'other',
       'BLT Pizza (Original, Golden or Thin Crust)':'other',
       'BLT Pizza (Mozza-Loaded Crust)':'other',
       'BLT Pizza (Original or Thin Crust)':'other',
       'Buffalo Chicken Pizza (Original Crust)':'chicken',
       'Buffalo Chicken Pizza (Original or Golden Crust)':'chicken',
       'Buffalo Chicken Pizza (Original, Golden or Thin Crust)':'chicken',
       'Buffalo Chicken Pizza (Mozza-Loaded Crust)':'chicken',
       'Buffalo Chicken Pizza (Original or Thin Crust)':'chicken',
       'Super Combo Pizza (Original or Golden Crust)':'supreme',
       'Super Combo Pizza (Original, Golden or Thin Crust)':'supreme',
       'Super Combo Pizza (Mozza-Loaded Crust)':'supreme',
       'Super Combo Pizza (Original or Thin Crust)':'supreme',
       'Super Hawaiian Pizza (Original or Golden Crust)':'hawaiian',
       'Super Hawaiian Pizza (Original, Golden or Thin Crust)':'hawaiian',
       'Super Hawaiian Pizza (Mozza-Loaded Crust)':'hawaiian',
       'Super Hawaiian Pizza (Original or Thin Crust)':'hawaiian',
       'Super Taco Pizza (Original or Golden Crust)':'other',
       'Super Taco Pizza (Original, Golden or Thin Crust)':'other',
       'Super Taco Pizza (Mozza-Loaded Crust)':'other',
       'Super Taco Pizza (Original or Thin Crust)':'other',
       'The Don (Original or Golden Crust)':'other',
       'The Don (Original, Golden or Thin Crust)':'other',
       'The Don (Mozza-Loaded Crust)':'other',
        'The Don (Original or Thin Crust)':'other',
       'Super Veggie Pizza (Original or Golden Crust)':'veggie',
       'Super Veggie Pizza (Original, Golden or Thin Crust)':'veggie',
       'Super Veggie Pizza (Mozza-Loaded Crust)':'veggie',
       'Super Veggie Pizza (Original or Thin Crust)':'veggie',
       'BBQ Bacon Cheeseburger Pizza (Original Crust)':'bacon cheeseburger',
       'BBQ Bacon Cheeseburger Pizza (Original, Golden or Thin Crust)':'bacon cheeseburger',
       'BBQ Bacon Cheeseburger Pizza (Mozza-Loaded Crust)':'bacon cheeseburger',
       'Chipotle Chicken and Bacon Pizza (Original Crust)':'other',
       'Chipotle Chicken and Bacon Pizza (Original, Golden or Thin Crust)':'other',
       'Chipotle Chicken and Bacon Pizza (Mozza-Loaded Crust)':'other',
       'Margherita Pizza (Original, Golden or Thin Crust)':'other',
       'Margherita Pizza (Thin Crust)':'other',
       'Margherita Chicken Pizza (Original, Golden or Thin Crust)':'other',
       'Margherita Chicken Pizza (Thin Crust)':'other',
        'Thin Crust':'cheese',
       'Original Crust':'cheese',
        'Original or Golden Crust':'cheese',
       'Original, Golden or Thin Crust':'cheese',
        'Mozza-Loaded Crust':'cheese',
       'Original or Thin Crust':'cheese',
                  
        'Deluxe Pizza':'supreme',
        'Veggie Pizza':'veggie',
        'Cheese Pizza':'cheese',
        'All Meat Pizza':'meat',
       'BBQ Chicken Pizza':'chicken',
        'Egg-Ceptional Pizza':'other',
                  
                  
        'Hand-Tossed':'cheese',
        'Pan Pizza':'cheese',
        'Thin N Crispy':'cheese',
        'Stuffed Crust':'cheese',
       'Skinny Slice':'cheese',
        "Pepperoni Lover's® Pizza (Hand-Tossed)":'pepperoni',
       "Pepperoni Lover's® Pizza (Pan Pizza)":'pepperoni',
       "Pepperoni Lover's® Pizza (Thin N Crispy)":'pepperoni',
       "Pepperoni Lover's® Pizza (Stuffed Crust)":'pepperoni',
       "Pepperoni Lover's® Pizza (Skinny Slice)":'pepperoni',
       "Meat Lover's® Pizza (Hand-Tossed)":'meat',
       "Meat Lover's® Pizza (Pan Pizza)":'meat',
       "Meat Lover's® Pizza (Thin N Crispy)":'meat',
       "Meat Lover's® Pizza (Stuffed Crust)":'meat',
       "Meat Lover's® Pizza (Skinny Slice)":'meat',
       "Ultimate Cheese Lover's Pizza (Hand-Tossed)":'other',
       "Ultimate Cheese Lover's Pizza (Pan Pizza)":'other',
       "Ultimate Cheese Lover's Pizza (Thin N Crispy)":'other',
       "Ultimate Cheese Lover's Pizza (Stuffed Crust)":'other',
       "Ultimate Cheese Lover's Pizza (Skinny Slice)":'other',
       "Veggie Lover's® Pizza (Hand-Tossed)":'veggie',
       "Veggie Lover's® Pizza (Pan Pizza)":'veggie',
       "Veggie Lover's® Pizza (Thin N Crispy)":'veggie',
       "Veggie Lover's® Pizza (Stuffed Crust)":'veggie',
       "Veggie Lover's® Pizza (Skinny Slice)":'veggie',
       'Supreme Pizza (Hand-Tossed)':'supreme',
        'Supreme Pizza (Pan Pizza)':'supreme',
       'Supreme Pizza (Thin N Crispy)':'supreme',
        'Supreme Pizza (Stuffed Crust)':'supreme',
       'Supreme Pizza (Skinny Slice)':'supreme',
        "BBQ Lover's™ (Hand-Tossed)":'other',
       "BBQ Lover's™ (Pan Pizza)":'other',
        "BBQ Lover's™ (Thin N Crispy)":'other',
       "BBQ Lover's™ (Stuffed Crust)":'other',
        "BBQ Lover's™ (Skinny Slice)":'other',
       'Chicken Supreme Pizza (Hand-Tossed)':'supreme',
       'Chicken Supreme Pizza (Pan Pizza)':'supreme',
       'Chicken Supreme Pizza (Thin N Crispy)':'supreme',
       'Chicken Supreme Pizza (Stuffed Crust)':'supreme',
       'Chicken Supreme Pizza (Skinny Slice)':'supreme',
       'New Primo Meat Pizza (Hand-Tossed)':'meat',
       'New Primo Meat Pizza (Pan Pizza)':'meat',
       'New Primo Meat Pizza (Thin N Crispy)':'meat',
       'New Primo Meat Pizza (Stuffed Crust)':'meat',
       'New Primo Meat Pizza (Skinny Slice)':'meat',
       'Hawaiian Luau (Hand-Tossed)':'hawaiian',
        'Hawaiian Luau (Pan Pizza)':'hawaiian',
       'Hawaiian Luau (Thin N Crispy)':'hawaiian',
        'Hawaiian Luau (Stuffed Crust)':'hawaiian',
       'Hawaiian Luau (Skinny Slice)':'hawaiian',
       'Super Supreme Pizza (Hand-Tossed)':'supreme',
       'Super Supreme Pizza (Pan Pizza)':'supreme',
       'Super Supreme Pizza (Thin N Crispy)':'supreme',
       'Super Supreme Pizza (Stuffed Crust)':'supreme',
       'Super Supreme Pizza (Skinny Slice)':'supreme',
       'Garden Party™ (Thin N Crispy)':'other',
       'Old Fashioned Meatbrawl™ (Pan Pizza)':'other',
       'Cock-a-doodle Bacon™ (Hand-Tossed)':'other',
       'Hot and Twisted™ (Hand-Tossed)':'other',
        'Pretzel Piggy™ (Hand-Tossed)':'other',
       'BBQ Bacon Cheeseburger (Hand-Tossed)':'bacon cheeseburger',
       'Giddy-Up BBQ Chicken™ (Hand-Tossed)':'chicken',
       'Buffalo State of Mind™ (Hand-Tossed)':'chicken',
       'Cherry Pepper Bombshell™ (Thin N Crispy)':'other',
       '7-Alarm Fire™ (Hand-Tossed)':'other',
        'Skinny Beach™ (Skinny Slice)':'other',
       'Skinny With A Kick™ (Skinny Slice)':'other',
       'Skinny Italy (Skinny Slice)':'other',
        'Skinny Luau™ (Skinny Slice)':'other',
       'Skinny Club™ (Skinny Slice)':'other',
       'Create Your Own (Gluten-Free Crust)':'other' }
                  
        


# In[239]:


df['Toppings'] = 'n/a'
df['Toppings'] = df['Pizza Name'].map(pizza_name_cat)
df.head()


# In[240]:


df['Company'].value_counts()


# In[241]:


df['Pizza Name'].value_counts()


# In[242]:


df['Type'].value_counts()


# In[243]:


df['Size'].value_counts()


# In[244]:


df.columns


# ## Make a catogorical variable for price

# In[245]:


price = df['Price']
q13 = df['Price'].quantile(1/3)
q23 = df['Price'].quantile(2/3)
price_level = []
for i in price:
    if i < q13:
        price_level.append('low')
    elif (q13 <= i < q23):
        price_level.append('medium')
    else:
        price_level.append('high')       


# In[246]:


df['Price_Level'] = price_level


# In[ ]:





# ### Rearange columns

# In[247]:


column_names_order = ['Company', 'Pizza Name', 'Type', 'Size', 'Diameter(inches)','Toppings','Price_Level','Price']


# In[248]:


df = df.reindex(columns=column_names_order)
df.head()


# ### Delete related Columns

# In[249]:


del df['Pizza Name']
del df['Size']
df.head()


# ## Condense The Pizza Type
# 
# Specialty Pizzas:         186
# 
# Classic Recipe Pizzas:     90
# 
# Feast Pizzas:              33
# 
# 
# Rest:                      other type

# In[250]:


for i,j in enumerate(df['Type']):
    if (df['Type'][i] == 'Specialty Pizzas') or (df['Type'][i] == 'Classic Recipe Pizzas') or (df['Type'][i] == 'Feast Pizzas'):
        None
    else:
        df['Type'][i] = 'other'

df.head()


# In[263]:


df['Price_Level'].value_counts()


# In[251]:


df.dtypes


# In[259]:


len(df['Type'].value_counts())


# In[253]:


df['Price_Level'].value_counts()


# In[254]:


df.to_csv (r'pizza_updated.csv', index = False, header=True)


# 

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




