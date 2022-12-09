import pymysql
import os
from sandbox import converter

dbName = 'TermProject'
password = os.environ.get('MYSQLPW')

class Database():
    def __init__(self):
        self.db= pymysql.connect(host='localhost', port= 3306,
                                  user='root',
                                  password=password,
                                  db=dbName,
                                  charset='utf8')
        self.cursor= self.db.cursor(pymysql.cursors.DictCursor)
        '''
        sql_create = 'CREATE DATABASE TermProject'
        sql_use = 'USE TermProject'
        cursor.execute(sql_create)
        cursor.execute(sql_use)
        #테이블 생성
        sql = open("DBP-e14-MySQL-VRG-Create-Tables.sql").read()
        #데이터 생성
        sql = open("DBP-e14-MySQL-VRG-Insert-Data.sql").read()
        for statement in sql.split(';'):
            if len(statement) > 5:
            cursor.execute(statement + ';')
        '''
    def logcheck(self,id,password):
        sql = "select CustomerID from customer WHERE Id=%s AND Password = %s"
        result = self.cursor.execute(sql, (id, password))
        #print(id,password)
        welcome = f'Hello {id}, Successfully Logged In!'
        if result == 0:
            return False
        else :
            customerID = dict(self.cursor.fetchone())['CustomerID']
            return True,welcome, customerID

    def get_list(self, TableName, *columnName):
        columnNames = converter(*columnName)
        sql =f"""select {columnNames} 
                from {TableName};"""
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        return data
    '''
    def get_days_meal_list(self):
        sql ="""select * 
                from days_meal"""
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        return data

    def get_customer_id_list(self):
        sql ="""select CustomerID 
                from customer"""
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        return data
    '''
    def get_primary_keys_info(self, tablename):
        sql = f"""SHOW keys
                    FROM {tablename}
                    WHERE Key_name = 'PRIMARY';"""
        self.cursor.execute(sql)
        keys_info = self.cursor.fetchall()
        n = len(keys_info)
        primary_keys = []
        for i in range(n):
            primary_keys.append(keys_info[i]['Column_name'])

        return primary_keys

    def getdata(self):
        sql= """select work.Title, artist.LastName, trans.AcquisitionPrice, trans.TransactionID 
                from work, artist, trans
                where trans.WorkID = work.WorkID and work.ArtistID = artist.ArtistID AND trans.CustomerID is null"""
        num=self.cursor.execute(sql)
        data = self.cursor.fetchall()
        return num, data

    def sign_up(self,PhoneNumber, id, password, SchoolMail):
        sql = f"""INSERT INTO customer
        (PhoneNumber, Id, Password, SchoolMail)VALUES('{PhoneNumber}','{id}', '{password}','{SchoolMail}');"""
        self.cursor.execute(sql)
        self.db.commit()

    def update_work(self,TransactionID,CustomerID,DateSold,SalesPrice):
        sql= "UPDATE trans SET DateSold=%s, SalesPrice=%s, CustomerID = %s WHERE TransactionID =%s ;"
        result = self.cursor.execute(sql,(DateSold, SalesPrice, CustomerID, TransactionID))
        self.db.commit()

    def execute(self, query, args={}):
        self.cursor.execute(query, args) 
 
    def executeOne(self, query, args={}):
        self.cursor.execute(query, args)
        row= self.cursor.fetchone()
        return row
 
    def executeAll(self, query, args={}):
        self.cursor.execute(query, args)
        row= self.cursor.fetchall()
        return row
 
    def commit(self):
        self.db.commit()

    def close(self):
        self.db.close()

'''
db = pymysql.connect(
    user='root',
    port = 3306,
    password=password,
    host='127.0.0.1',
    charset='utf8'
)

cursor = db.cursor()
# 결과를 Dictionary 형태로 받고싶은 경우
cursor = db.cursor(pymysql.cursors.DictCursor)

#sql_create = 'CREATE DATABASE practice'
#sql_use = 'USE practice'
#cursor.execute(sql_create)
#cursor.execute(sql_use)

# 테이블 생성
#sql = open("DBP-e14-MySQL-VRG-Create-Tables.sql").read()

# 데이터 생성
#sql = open("DBP-e14-MySQL-VRG-Insert-Data.sql").read()

for statement in sql.split(';'):
    if len(statement) > 5:
       cursor.execute(statement + ';')

sql = "select * from artist"
b = cursor.execute(sql)
print(b)
# 모든 데이터를 한번에 클라이언트로 가져오기
a = cursor.fetchmany(3)
for row in a:
    print(row)
    print(row['ArtistID'],row['LastName'],row['FirstName'])

# Parameter Placeholder
sql_placeholder = "select * from artist where ArtistID=%s and LastName=%s"

a = cursor.execute(sql_placeholder, (1, 'Miro'))
data = cursor.fetchall()
print(a, data)

#Data Insert
insert = """INSERT INTO ARTIST
(ArtistID, LastName, FirstName, Nationality, DateOfBirth, DateDeceased)VALUES(60, 'Park', 'John', 'Spanish', 1893, 1983);"""

#cursor.execute(insert)



db.commit()
db.close()
'''
