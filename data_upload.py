# import xlrd
# import xlwt
# import os
# import pandas.io.sql as sql
# from configparser import ConfigParser
# import mysql.connector
# class ExcelExample(object):
# def __init__(self):


# self.Title = "Work with Excel Example";
# config = ConfigParser()
# config.read('mypy.ini')
# database = config.get('dbinfo', 'database')
# dbusername = config.get('dbinfo', 'dbusername')
# dbpassword = config.get('dbinfo', 'dbpassword')
#         dbhost = config.get('dbinfo', 'dbhost')

#         self.myConnection = mysql.connector.connect(
#           host=config.get('dbinfo', 'dbhost'),
#           user=config.get('dbinfo', 'dbusername'),
#           password=config.get('dbinfo', 'dbpassword'),
#           database=config.get('dbinfo', 'database'))
#     def ReadFromExcel(self):
#         rootPath = os.getcwd()
#         rootPath=rootPath+"/excelFolder/";
#         loc = (rootPath+"emailList.xlsx"); 
  
#         wb = xlrd.open_workbook(loc) 
#         sheet = wb.sheet_by_index(0) 
#         for i in range(sheet.nrows): 
#                 print(sheet.cell_value(i, 0),sheet.cell_value(i, 1)) 
#         print("Successfully retrieved all excel data");
#     def WriteToExcel(self):
#         rootPath = os.getcwd()
#         rootPath=rootPath+"/excelFolder/newFile.xlsx";       
        
#         workbook = xlwt.Workbook(encoding='utf-8')
#         worksheet = workbook.add_sheet("mysheet1",cell_overwrite_ok=True)
#         worksheet.Title = "Email List";     
    
#         fileds = [u'ID',u'Name',u'Email']
#         for filed in range(0,len(fileds)):
#             worksheet.write(0,filed,fileds[filed])           
     
#         workbook.save(rootPath);
         
#         print("Successfully created excel file");
#     def WriteToExcel2(self):
#         rootPath = os.getcwd()
#         rootPath=rootPath+"/excelFolder/newFile.xlsx";       
        
#         workbook = xlwt.Workbook(encoding='utf-8')
#         worksheet = workbook.add_sheet("mysheet1",cell_overwrite_ok=True)
#         worksheet.Title = "Email List";     
    
#         df=sql.read_sql('SELECT firstName, LastName, RegDate FROM tbStudent',self.myConnection)
#         df.to_excel('ds.xls')
         
#         print("Successfully created excel file");