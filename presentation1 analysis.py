#!/usr/bin/env python
# coding: utf-8

# In[364]:


import pandas as pd
import numpy as np
import scipy.stats as stats
import random as r
import matplotlib.pyplot as plt
import seaborn as sns
import scipy as sp

# ignore stupid warnings
import warnings
warnings.filterwarnings('ignore')


# In[365]:


### Typography/styles

color_list = ['blue','green', 'red' , 'cyan','magenta','yellow']
seaborn_styles = ['darkgrid', 'whitegrid', 'dark', 'white', 'ticks']


# In[366]:


df = pd.read_csv('pizza_updated.csv')
df.head()


# summarize price first then summarize it by company
# 
# then you can look for relationships between price and other factors such as size

# In[254]:


def hist_freqTable_function(dataframe,variable_name):
    ''' This will make a histogram and frequency table for a numeric variable in the dataframe'''
    
    ##### Variables to make the Histogram 
    df = dataframe[variable_name]
    observations = len(df)
    num_of_bins = round(len(df)**(1/2))
    min_num = min(df)
    max_num = max(df)
    range_num = max_num - min_num
    bin_width = round(range_num/num_of_bins)
    bin_range = np.arange(min_num,max_num+bin_width,bin_width)
    #########################################################################
    
    ##### My Histogram ###
    fig, axes = plt.subplots(figsize = (20,7),dpi=200)
    color = r.choice(color_list)
    style = r.choice(seaborn_styles)
    sns.set_style(style)
    sns.histplot(data=df,bins=bin_range,color=color);
    axes.set_title(f'histogram for {variable_name}',color='black', fontsize = 15);
    plt.show()
    
    
    
    ##### My Frequency Table ###
    FTable= df.groupby(pd.cut(df,bin_range, right=False)).count()
    FTable = FTable.to_frame()
    FTable.columns = ['Frequencies']
    FTable['Relative Frequencies'] =     FTable['Frequencies']/FTable['Frequencies'].sum()
    print(FTable)
    print('#'*120)
    print('#'*120)


# In[255]:


def summary_statisics(dataframe,variable_name):
    '''This function will find and displays the count, mean, standard deviation, min, Q1,
    median, Q3, and max of the variable. 
    '''
    ### Summary Stats Varaibles 
    df = dataframe[variable_name].describe()
    count = df[0]
    mean = df[1]
    std =  df[2]
    min_num =  df[3]
    q1 = df[4]
    median = df[5]
    q3 = df[6]
    max_num = df[7]
    
    summary_statisics_names = ['Count','Mean','Standard Deviation','Min','Q1','Median','Q3','Max']
    summary_statisics_values = [count,mean,std,min_num,q1,median,q3,max_num]
    
   
    for i,j in zip(summary_statisics_names,summary_statisics_values):
        print(f"The {i} for {variable_name} is {j}")
    print('#'*120)
    print('#'*120)


# In[256]:


def boxplot_function(dataframe,variable_name,whis=1.5):
    '''
    This function will display outliers of the variable (outside the fences) and makes a boxwhisker plot of the variable.
    Whis argument is optional in case you want to change the outlier sensitivity 
    '''
    
    df = dataframe[variable_name]
    Q1 = df.quantile(0.25)
    Q3 = df.quantile(0.75)
    
    IQR = Q3 - Q1
    lower_bound = Q1 - IQR*whis
    upper_bound = Q3 + IQR*whis
    outliers = []
    
    fig, axes = plt.subplots(figsize = (20,7),dpi=200)
    
    color = r.choice(color_list)
    style = r.choice(seaborn_styles)
    sns.set_style(style)
    sns.boxplot(data=df,color=color, orient="h",whis=whis);
    axes.set_title('boxplot',color='black', fontsize = 15);
    plt.show()
    
    for i in df:
        if (i>upper_bound) or (i<lower_bound):
            outliers.append(i)
        
    if outliers == []:
        print('There are no outliers')
    else:
        outliers.sort()
        print(f'Here are the outlier(s): {outliers}')


# # 1.) Summary For Price

# In[291]:


df.describe().round(2)


# In[292]:


hist_freqTable_function(df,'Diameter(inches)')


# In[289]:


hist_freqTable_function(df,'Price')


# Interpretation: 

# In[259]:


summary_statisics(df,'Price')


# Interpretation: 

# In[260]:


boxplot_function(df,'Price')


# Interpretation: 

# # 2.) Summary For Price  by Group

# In[261]:


sns.set_style('darkgrid')
fig, axes = plt.subplots(figsize = (13,5),dpi=200)
sns.boxplot(data=df,y='Company',x='Price');


# In[262]:


sns.set_style('darkgrid')
fig, axes = plt.subplots(figsize = (13,5),dpi=200)
sns.boxplot(data=df,y='Type',x='Price');


# In[263]:


sns.set_style('darkgrid')
fig, axes = plt.subplots(figsize = (13,5),dpi=200)
sns.boxplot(data=df,y='Toppings',x='Price');


# In[293]:


df.groupby("Toppings").mean().round(2)


# Interpretation: 

# In[265]:


df.groupby("Company").std().round()


# Interpretation: 

# In[ ]:





# In[266]:


df.groupby("Company").min()


# Interpretation: 

# In[ ]:





# In[ ]:





# Interpretation: 

# In[267]:


df.groupby("Company").count()


# In[268]:


df.groupby("Company").describe().round(2)


# Interpretation: 

# In[269]:


sns.set_style('whitegrid')
fig, axes = plt.subplots(figsize = (10,4),dpi=200)
sns.countplot(data=df,x='Company',palette='hls');


# In[270]:


df['Company'].value_counts()


# In[271]:


sns.set_style('whitegrid')
fig, axes = plt.subplots(figsize = (13,4),dpi=200)
sns.countplot(data=df,x='Toppings',hue='Company',palette='hls');


# In[272]:


df['Toppings'].value_counts()


# In[273]:


sns.set_style('whitegrid')
fig, axes = plt.subplots(figsize = (13,4),dpi=200)
sns.countplot(data=df,x='Type',hue='Company',palette='hls');


# In[274]:


df['Type'].value_counts()


# In[275]:


sns.set_style('darkgrid')
fig, axes = plt.subplots(figsize = (10,5),dpi=200)
sns.scatterplot(data=df,x='Diameter(inches)',y='Price',color='green');


# In[276]:


sns.set_style('darkgrid')
fig, axes = plt.subplots(figsize = (10,5),dpi=200)
sns.scatterplot(data=df,x='Diameter(inches)',y='Price',color='red',hue="Company");


# In[277]:


sns.set_style('darkgrid')
fig, axes = plt.subplots(figsize = (10,5),dpi=200)
sns.scatterplot(data=df,x='Diameter(inches)',y='Price',color='red',hue="Toppings");


# In[278]:


sns.set_style('darkgrid')
sns.color_palette("rocket", as_cmap=True)
fig, axes = plt.subplots(figsize = (7,3),dpi=200)
sns.scatterplot(data=df,x='Diameter(inches)',y='Price',color='red',hue="Type");


# In[279]:


pizza_toppings = df["Toppings"].copy().value_counts().rename_axis('toppings').reset_index(name='counts')
pizza_toppings.head()


# In[280]:


labels = pizza_toppings['toppings']
values = pizza_toppings['counts']

sns.set_style('darkgrid')
sns.color_palette("rocket", as_cmap=True)
fig, axes = plt.subplots(figsize = (15,6),dpi=200)
axes.pie(x=values, labels = labels, autopct='%1.2f%%');


# In[297]:


df.head()


# In[282]:


df['Type'].value_counts()


# In[300]:


df[df["Company"] == "Pizza Hut"]['Price']


# In[311]:


from scipy.stats import shapiro

#perform Shapiro-Wilk test
shapiro(df[df["Company"] == "Domino's Pizza"]['Price'])


# In[302]:


len(df[df["Company"] == "Pizza Hut"]['Price'])


# In[307]:


from numpy.random import randn
x = randn(100)


# In[305]:





# In[309]:


df[df["Company"] == "Pizza Hut"]['Price']


# In[358]:


df[df['Toppings']== 'cheese']["Price_Level"].value_counts()


# In[339]:


df[df['Toppings']== 'bacon cheeseburger']["Price_Level"].value_counts()


# In[340]:


df[df['Toppings']== 'chicken']["Price_Level"].value_counts()


# In[341]:


df[df['Toppings']== 'hawaiian']["Price_Level"].value_counts()


# In[342]:


df[df['Toppings']== 'meat']["Price_Level"].value_counts()


# In[344]:


df[df['Toppings']== 'other']["Price_Level"].value_counts()


# In[345]:


df[df['Toppings']== 'pepperoni']["Price_Level"].value_counts()


# In[347]:


df[df['Toppings']== 'supreme']["Price_Level"].value_counts()


# In[348]:


df[df['Toppings']== 'veggie']["Price_Level"].value_counts()


# In[357]:


len(df[df['Toppings']== 'veggie']["Price_Level"])


# In[363]:


col = list(df['Toppings'].unique())
for i in col:
    print(i)
    print(len(df[df['Toppings']== i]["Price_Level"]))


# # Chi-Square Test

# In[380]:


table = pd.crosstab(df['Toppings'],df['Price_Level'])
table


# ### observe values

# In[381]:


observe_values = table.values
observe_values


# ### expect values

# In[382]:


val = stats.chi2_contingency(table)
expected_values = val[3]
expected_values


# In[383]:


degree_of_freedoms = (9-1)*(3-1)


# In[391]:


# chi square statistic
from scipy.stats import chi2
chi_square = sum([(o-e)**2/e for o,e in zip(observe_values,expected_values)])
chi_square_statistic = chi_square[0] + chi_square[1]
chi_square_statistic


# In[394]:


# critical Value
critical_value = chi2.ppf(q=1-0.05, df=degree_of_freedoms)
critical_value


# In[ ]:




