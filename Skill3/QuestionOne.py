import mysql.connector
import pymysql

pymysql.install_as_MySQLdb()
while(True):
    print("|-------------------------------------------------------------------|")
    print("|  *-*-* Welcome to the Lexux Ross Machine Manufacturing Co. *-*-*  |")
    print("|-------------------------------------------------------------------|")
    print("1. Displaying Tables ")
    print("2. Creating a new table")
    print("3. Insert into the new Table")
    print("4. Display of the table")
    print("5. Rename of the Table")
    print("6. Drop the Table")
    choice = int(input('Enter your Choice : '))
    if choice==1:
        conn = pymysql.connect(host="localhost", user='root', password='muni2002', database='mydb')
        cursor = conn.cursor()
        cursor.execute("SHOW Tables")
        print(cursor.fetchall())
        conn.close()
    elif (choice == 2):
        conn = pymysql.connect(host="localhost",user='root', password='muni2002', database='mydb')
        cursor = conn.cursor()
        sql = '''CREATE TABLE Machine(SNo bigint, Product_specialisation_and_name varchar(50),Date_of_product_manufacturing date,MRP_on_the_Product int,Invoice_bill_no int,Product_manufacturer varchar(30));'''
        try:
           cursor.execute(sql)
           conn.commit()
        except:
           conn.rollback()
           print("Table Created Successfully")
        conn.close()
    elif(choice==3):
        Sno = int(input('Enter S.No : '))
        product_name = input('Enter the Product specification and its table : ')
        date = input('Enter the Date of product manufacturing in (YYYY-MM-DD) : ')
        mrp = int(input('Enter the MRP on the Product : '))
        invoice = int(input('Enter Invoice bill Number : '))
        manufacturer = input('Enter Product Manufacturer : ')

        conn = mysql.connector.connect(host="localhost",user='root', password='muni2002', database='mydb')
        cursor = conn.cursor()
        sql="insert into Machine(SNo, Product_specialisation_and_name ,Date_of_product_manufacturing ,MRP_on_the_Product,Invoice_bill_no,Product_manufacturer) values(%s,%s,%s,%s,%s,%s);"

        val=(Sno,product_name,date,mrp,invoice,manufacturer)
        try:
            cursor.execute(sql,val)
            conn.commit()
        except:
            conn.rollback()
        print(cursor.rowcount, "Record Inserted!")
        conn.close()
    elif(choice==4):
        conn = mysql.connector.connect(host="localhost", user='root', password='muni2002', database='mydb')
        cursor=conn.cursor()
        cursor.execute("select * from machine")
        try:
           result=cursor.fetchall()
           for x in result:
               print(x)
        except Exception as e:
            print (e)
        conn.close()
    elif (choice == 5):
        conn = mysql.connector.connect(host="localhost", user='root', password='muni2002', database='mydb')
        cursor = conn.cursor()
        cursor.execute("SHOW Tables")
        print(cursor.fetchall())
        try:
            cursor.execute("Alter table manufactoring_machine rename to machine;")
            cursor.execute("Show Tables")
            print(cursor.fetchall())
        except Exception as e:
            print (e)
    elif(choice==6):
        conn = mysql.connector.connect(host="localhost", user='root', password='muni2002', database='mydb')
        cursor = conn.cursor()
        cursor.execute("SHOW Tables")
        print(cursor.fetchall())
        try:
           cursor.execute("Drop table Machine;")
           #cursor.execute("Drop table manufactoring_machine;")
           print('Table dropped..!')
           print('List of tables after dropping the machine table :')
           cursor.execute("Show Tables")
           print(cursor.fetchall())
        except Exception as e:
            print (e)
        conn.close()
    else:
        exit()