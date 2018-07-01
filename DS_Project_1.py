
# coding: utf-8
#Project-1: Data Wrangling
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
#https://raw.githubusercontent.com/jackiekazil/data-wrangling/master/data/chp3/data-text.csv
df = pd.read_csv("https://raw.githubusercontent.com/jackiekazil/data-wrangling/master/data/chp3/data-text.csv")
df.head()
df1=pd.read_csv("https://raw.githubusercontent.com/kjam/data-wrangling-pycon/master/data/berlin_weather_oldest.csv")
df1.head();
df1.head(2)
#tasks

#Q1
df.info()
df1.info()

#Q2
df_rownames = np.array(df.index)
df_rownames
df1_rownames = np.array(df1.index)
df1_rownames

#Q3
df.rename(columns = {'Indicator':'Indcator_ID'})

#Q4
df_c=df.rename(columns = {'Indicator':'Indcator_ID'})
df_c.head(2)

#Q5
df_new=df_c.rename(columns = {'PUBLISH STATES':'Publication States', 'WHO region':'WHO Region'})
df_new.head(2)

#Q6
df_new.sort_values('Year').head(2)

#Q7
df_new.sort_values(['Indicator_ID', 'Country',  'Year', 'WHO region', 'Publication States'], ascending=[True, True, True, True, True], inplace=True)
#clist = df_new.columns.tolist
#clist

#Q8
#clist = ['Country', 'Indicator_ID', 'Publication States', 'Year', 'WHO region',
#       'World Bank income group', 'Sex', 'Display Value', 'Numeric', 'Low', 'High', 'Comments']
clist = clist[5:6] + clist[:5] + clist[6:]
clist
df_new = df_new[clist]
df_new.head(2)

#Q9
colArr = np.array(df_new.columns.tolist)
colArr

#Q10
df.iloc[[11,24,37]]

#Q11
#remove rows with index---5,12,23,56
#print(len(df))
len(df.drop(df.index[[5, 12, 23, 56]]))
#######################
#new Datasets
#https://raw.githubusercontent.com/ben519/DataWrangling/master/Data/users.csv  -- users
#https://raw.githubusercontent.com/ben519/DataWrangling/master/Data/sessions.csv -- sessions
#https://raw.githubusercontent.com/ben519/DataWrangling/master/Data/products.csv -- products
#https://raw.githubusercontent.com/ben519/DataWrangling/master/Data/transactions.csv -- transactions
########################
users = pd.read_csv("https://raw.githubusercontent.com/ben519/DataWrangling/master/Data/users.csv ")
sessions = pd.read_csv("https://raw.githubusercontent.com/ben519/DataWrangling/master/Data/sessions.csv ")
products = pd.read_csv("https://raw.githubusercontent.com/ben519/DataWrangling/master/Data/products.csv")
transactions = pd.read_csv("https://raw.githubusercontent.com/ben519/DataWrangling/master/Data/transactions.csv")
users.head(2)
sessions.head(2)
products.head(2)
transactions.head(2)
#merge(x,y,how="left", on='x1')

#12
pd.merge(transactions, users, how='left', on='UserID')

#13
transactions[~transactions.UserID.isin(users.UserID)]

#14
pd.merge(transactions, users, how='inner', on='UserID')

#15
pd.merge(transactions, users, how='outer', on='UserID')

#16
user_ses = pd.merge(users, sessions,how='inner', on='UserID')
#user_ses.groupby(by = 'UserID')
user_ses[user_ses.Registered == user_ses.SessionDate]

#17
products['key'] = 0
users['key'] = 0
xjoin = users.merge(products, how='outer')
xjoin[['UserID', 'ProductID']]

#18
#xjoin
transactions
#xjoin[['UserID','ProductID','Quantity']]
new_df = pd.merge(xjoin, transactions,  how='left', left_on=['UserID','ProductID'], right_on = ['UserID','ProductID'])
new_df[['UserID', 'ProductID', 'Quantity']]

#19
pd.merge(transactions, transactions, on = 'UserID', how = 'outer')

#20

filtered = new_df.drop_duplicates(['UserID'])
filtered

#21
my_columns = list(new_df.columns)
my_columns
#list(data.dropna(thresh=int(data.shape[0] * .9), axis=1).columns)
list(new_df.dropna(thresh=int(new_df.shape[0] * .9), axis=1).columns)
missing_info = list(new_df.columns[new_df.isnull().any()])
missing_info
for col in missing_info:
        num_missing = new_df[new_df[col].isnull() == True].shape[0]
        print('number missing for column {}: {}'.format(col, num_missing))
data = new_df
for col in missing_info:
       percent_missing = data[data[col].isnull() == True].shape[0] / data.shape[0]
       print('percent missing for column {}: {}'.format(col, percent_missing))

