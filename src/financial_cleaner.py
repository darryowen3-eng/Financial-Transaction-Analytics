#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
import numpy as np
from sqlalchemy import create_engine
df = pd.read_csv("dirty_financial_transactions.csv")

df=df.drop_duplicates()
df=df.reset_index(drop=True)

df['Price'] = df['Price'].astype(str).str.extract(r'(-?\d+\.\d+|-?\d+)')
df['Price'] = pd.to_numeric(df['Price'], errors='coerce').abs().round(2)
df['Quantity'] = df['Quantity'].abs()
df['Transaction_Date'] = pd.to_datetime(df['Transaction_Date'], errors='coerce', format='mixed')

df.replace(r'^\s*$',np.nan,regex=True,inplace=True)

num_cols = df.select_dtypes(include=np.number).columns
cat_cols = df.select_dtypes(include=["object", "string"]).columns

for i in num_cols:
    df[i] = df[i].fillna(df[i].median())

for j in cat_cols:
    df[j] = df[j].fillna(df[j].mode()[0])

df['Transaction_Date'] = df['Transaction_Date'].fillna(pd.Timestamp('2005-01-01'))


def clean_products(name):
    if not isinstance(name, str):
        return name
    name = name.strip()
    if name.startswith('Coffee M'):
        return 'Coffee Machine'
    elif name.startswith('H'):
        return 'Headphones'
    elif name.startswith('T'):
        return 'Tablet'
    elif name.startswith('L'):
        return 'Laptop'
    elif name.startswith('S'):
        return 'Smartphone'
    elif name.startswith('C'):
        return 'Coffee'
    return name


def clean_payments(method):
    if not isinstance(method, str):
        return method
    method = method.strip().title()
    if method.startswith('Credit'):
        return 'Credit Card'
    elif method.startswith('P'):
        return 'PayPal'
    elif method.startswith('C'):
        return 'Cash'
    return method

df['Product_Name'] = df['Product_Name'].apply(clean_products)
df['Payment_Method'] = df['Payment_Method'].apply(clean_payments)

df = df.sort_values(by=["Product_Name", "Transaction_Date"], ascending=False)
df.to_csv("clean_financial_transactions.csv", index=False)
print("\t==============Done===============\n")
print(df.head())



# In[ ]:




