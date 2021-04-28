#!/usr/bin/env python
# coding: utf-8

# In[16]:


import sqlite3


# In[20]:


conn = sqlite3.connect('exp2.db')
cur = conn.cursor()
print("Connected to Database Successfully")


# In[21]:


conn.execute('''CREATE TABLE COMPANY
               (ID INT PRIMARY KEY   NOT NULL,
                NAME            TEXT  NOT NULL,
                AGE             INT   NOT NULL,
                ADDRESS         CHAR(50),
                SALARY          REAL);''')
print("Table created Successfully");


# In[22]:


conn.execute("Insert into COMPANY values(100,'paul',26,'hyderabad',100000.00)");
conn.execute("Insert into COMPANY values(101,'allen',28,'mumbai',300000.00)");
conn.execute("Insert into COMPANY values(102,'sania',29,'chennai',300000.00)");
conn.execute("Insert into COMPANY values(103,'teddy',26,'hyderabad',200000.00)");
conn.commit()

print("Records created successfully");


# In[23]:


for row in conn.execute('select * from COMPANY'):
    print(row)


# In[24]:


sql = 'Insert into COMPANY values(?, ?, ?, ?, ?)'
val = [(106,'daniel',24,'kolkata',50000.00),(107,'ria',25,'hyderabad',70000.00)]
cur.executemany(sql,val)


# In[25]:


for row in conn.execute('select * from COMPANY'):
    print(row)


# In[14]:


conn.commit()


# In[15]:


conn.close()

