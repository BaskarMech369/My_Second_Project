from tabulate import tabulate

import mysql.connector

conn = mysql.connector.connect(host='localhost',username='root',password='Baskar369@#',database='python_db')
my_cursor=conn.cursor()

def insert(name,age,city):
    res=conn.cursor()
    sql="insert into users (name,age,city) values (%s,%s,%s)"
    user=(name,age,city)
    res.execute(sql,user)
    conn.commit()
    print("Data Insert Success")

def update(name,age,city,id):
    res=conn.cursor()
    sql="update users set name=%s,age=%s,city=%s where id=%s "
    user=(name,age,city,id)
    res.execute(sql,user)
    conn.commit()
    print("Data update Success")

def select():
    res=conn.cursor()
    sql="SELECT ID,NAME,CITY from users"
    res.execute(sql)
    result=res.fetchall()
    print(tabulate(result,headers=["ID","NAME","AGE","CITY"]))

def delete(id):
    res=conn.cursor()
    sql="delete from users where id=%s "
    user=(id,)
    res.execute(sql,user)
    conn.commit()
    print("Data Delete Success")
    
while True:
      print("1.Insert Data")
      print("2.Update Data")
      print("3.Select Data")
      print("4.Delete Data")
      print("5.Exit")
      choice=int(input("Enter Your Choice : "))
    
      if choice == 1:
            name=input("Enter Name : ")
            age=input("Enter Age : ")
            city=input("Enter City : ")
            insert(name,age,city)
      
      elif choice == 2:
            id=input("Enter the id : ")
            name=input("Enter Name : ")
            age=input("Enter Age : ")
            city=input("Enter City : ")
            update(name,age,city,id)
    
      elif choice == 3:
            select()
     
      elif choice == 4:
            id=input("Enter The Id to Delete : ")
            delete(id)
      
      elif choice == 5:
            exit("sucessfully exited")
     
      else:
            print("Invalid Selection . please Try Again !")
      
      
      