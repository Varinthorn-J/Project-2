
# coding: utf-8

# In[1]:


import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb
import xlrd


# In[2]:


database = MySQLdb.connect (host="localhost" , user="root" , passwd="1234" ,db="mysql")
cursor = database.cursor()


# In[3]:


product_details_table = ("CREATE TABLE IF NOT EXISTS student_details(no int,id int,name text,score varchar(255), PRIMARY KEY (id))")


# In[4]:


cursor.execute(product_details_table)


# In[5]:


#read excel_sheet


# In[6]:


excel_sheet = xlrd.open_workbook('D:\2-2563\project\2\projectII\book.xlsx')
excel_sheet


# In[7]:


sheet_name = excel_sheet.sheet_names()
sheet_name


# In[8]:


insert_query = "INSERT INTO product_details (product_id,product_name,product_price,product_rating,product_star_rating,product_url) VALUES (%s,%s,%s,%s,%s,%s)"


# In[9]:


for sh in range(0,len(sheet_name)):
    sheet= excel_sheet.sheet_by_index(sh)
    
    for r in range(1,sheet.nrows):
        product_id = sheet.cell(r,0).value

        product_name = sheet.cell(r,1).value

        product_price = sheet.cell(r,2).value
     
        product_rating = sheet.cell(r,3).value
      
        product_star_rating = sheet.cell(r,4).value
        
        product_url = sheet.cell(r,5).value
        
        product_details_value = (product_id,product_name,product_price,product_rating,product_star_rating,product_url)
        
        
        cursor.execute(insert_query,product_details_value)
        database.commit()