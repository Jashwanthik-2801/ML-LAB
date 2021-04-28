#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sqlite3


# In[2]:


conn = sqlite3.connect('exp2.db')
cur = conn.cursor()
conn = sqlite3.connect('test.db')
print("Opened Database Successfully")


# In[10]:


conn.execute('''CREATE TABLE COMPANY3
               (ID INT PRIMARY KEY   NOT NULL,
                NAME            TEXT  NOT NULL,
                AGE             INT   NOT NULL,
                ADDRESS         CHAR(50),
                SALARY          REAL);''')
print("Table created Successfully");


# In[11]:


conn.execute("Insert into COMPANY3 values(100,'paul',26,'hyderabad',100000.00)");
conn.execute("Insert into COMPANY3 values(101,'allen',28,'mumbai',300000.00)");
conn.execute("Insert into COMPANY3 values(102,'sania',29,'chennai',300000.00)");
conn.execute("Insert into COMPANY3 values(103,'teddy',26,'hyderabad',200000.00)");
conn.commit()

print("Records created successfully");


# In[12]:


for row in conn.execute('select * from COMPANY3'):
    print(row)


# In[13]:


conn.commit()


# In[14]:


conn.close()

