
# coding: utf-8

# In[ ]:


#Project-1: Data Wrangling
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[ ]:


#https://raw.githubusercontent.com/jackiekazil/data-wrangling/master/data/chp3/data-text.csv
df = pd.read_csv("https://raw.githubusercontent.com/jackiekazil/data-wrangling/master/data/chp3/data-text.csv")
df.head()


# In[ ]:


df1=pd.read_csv("https://raw.githubusercontent.com/kjam/data-wrangling-pycon/master/data/berlin_weather_oldest.csv")
df1.head();


# In[ ]:


df1.head(2)


# In[ ]:


#Q1
df.info()


# In[ ]:


df1.info()


# In[ ]:


#Q2
df_rownames = np.array(df.index)
df_rownames


# In[ ]:


df1_rownames = np.array(df1.index)
df1_rownames


# In[ ]:


#Q3
df.rename(columns = {'Indicator':'Indcator_ID'})


# In[ ]:


#Q4
df_c=df.rename(columns = {'Indicator':'Indcator_ID'})


# In[ ]:


df_c.head(2)


# In[ ]:


#Q5
df_new=df_c.rename(columns = {'PUBLISH STATES':'Publication States', 'WHO region':'WHO Region'})


# In[ ]:


df_new.head(2)


# In[ ]:


#Q6
df_new.sort_values('Year').head(2)


# In[ ]:


#Q7
df_new.sort_values(['Indicator_ID', 'Country',  'Year', 'WHO region', 'Publication States'], ascending=[True, True, True, True, True], inplace=True)


# In[ ]:


#df_new[['Indicator_ID', 'Country',  'Year', 'WHO region', 'Publication States']]


# In[ ]:


#df_new[['Country']]
type(df_new)


# In[ ]:


clist = df_new.columns.tolist
clist


# In[ ]:


#Q8
#clist = ['Country', 'Indicator_ID', 'Publication States', 'Year', 'WHO region',
#       'World Bank income group', 'Sex', 'Display Value', 'Numeric', 'Low', 'High', 'Comments']
clist = clist[5:6] + clist[:5] + clist[6:]
clist


# In[ ]:


df_new = df_new[clist]


# In[ ]:


df_new.head(2)


# In[ ]:


#Q9
colArr = np.array(df_new.columns.tolist)


# In[ ]:


colArr


# In[ ]:


#Q10
df.iloc[[11,24,37]]


# In[ ]:


#Q11
#remove rows with index---5,12,23,56
#print(len(df))
len(df.drop(df.index[[5, 12, 23, 56]]))


# In[ ]:


#new Datasets
#https://raw.githubusercontent.com/ben519/DataWrangling/master/Data/users.csv  -- users
#https://raw.githubusercontent.com/ben519/DataWrangling/master/Data/sessions.csv -- sessions
#https://raw.githubusercontent.com/ben519/DataWrangling/master/Data/products.csv -- products
#https://raw.githubusercontent.com/ben519/DataWrangling/master/Data/transactions.csv -- transactions
users = pd.read_csv("https://raw.githubusercontent.com/ben519/DataWrangling/master/Data/users.csv ")
sessions = pd.read_csv("https://raw.githubusercontent.com/ben519/DataWrangling/master/Data/sessions.csv ")
products = pd.read_csv("https://raw.githubusercontent.com/ben519/DataWrangling/master/Data/products.csv")
transactions = pd.read_csv("https://raw.githubusercontent.com/ben519/DataWrangling/master/Data/transactions.csv")
users.head(2)
sessions.head(2)
products.head(2)
transactions.head(2)


# In[ ]:


#merge(x,y,how="left", on='x1')
#12
pd.merge(transactions, users, how='left', on='UserID')


# In[ ]:


#13
transactions[~transactions.UserID.isin(users.UserID)]


# In[ ]:


#14
pd.merge(transactions, users, how='inner', on='UserID')


# In[ ]:


#15
pd.merge(transactions, users, how='outer', on='UserID')


# In[ ]:


#16
user_ses = pd.merge(users, sessions,how='inner', on='UserID')
#user_ses.groupby(by = 'UserID')
user_ses[user_ses.Registered == user_ses.SessionDate]


# In[ ]:


#17
products['key'] = 0
users['key'] = 0
xjoin = users.merge(products, how='outer')
xjoin[['UserID', 'ProductID']]


# In[ ]:


#18
#xjoin
transactions
#xjoin[['UserID','ProductID','Quantity']]
new_df = pd.merge(xjoin, transactions,  how='left', left_on=['UserID','ProductID'], right_on = ['UserID','ProductID'])


# In[ ]:


new_df[['UserID', 'ProductID', 'Quantity']]


# In[ ]:


#19
pd.merge(transactions, transactions, on = 'UserID', how = 'outer')


# In[ ]:


#20

filtered = new_df.drop_duplicates(['UserID'])


# In[ ]:


filtered


# In[ ]:


#21
my_columns = list(new_df.columns)
my_columns


# In[ ]:


#list(data.dropna(thresh=int(data.shape[0] * .9), axis=1).columns)
list(new_df.dropna(thresh=int(new_df.shape[0] * .9), axis=1).columns)


# In[ ]:


missing_info = list(new_df.columns[new_df.isnull().any()])
missing_info


# In[ ]:


for col in missing_info:
        num_missing = new_df[new_df[col].isnull() == True].shape[0]
        print('number missing for column {}: {}'.format(col, num_missing))


# In[ ]:


data = new_df
for col in missing_info:
       percent_missing = data[data[col].isnull() == True].shape[0] / data.shape[0]
       print('percent missing for column {}: {}'.format(col, percent_missing))

