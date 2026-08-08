#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
from sqlalchemy import create_engine


engine = create_engine(
    "postgresql://postgres:darry%402005@localhost/postgres"
)

df = pd.read_csv("clean_financial_transactions.csv")

df.to_sql(
    "finincial_transactions",
    engine,
    if_exists="replace",
    index=False
)

print("==============Data loaded in your Database==============")

