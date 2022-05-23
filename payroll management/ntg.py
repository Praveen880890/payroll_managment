import mysql.connector
con=mysql.connector.connect(host="localhost",username="root",password="root",database="mysql")
c=con.cursor()

try:
    c.execute("create table payroll(empid INT,Name varchar(45),Address varchar(45),Employer varchar(45),HoursWorked varchar(45),wageshour varchar(45),Tax varchar(45),OverTimeBonus varchar(45),Payable varchar(45),Net_pay varchar(45),PRIMARY KEY (empid))")
except Exception as e:
    print(e)
finally:
    try:
        c.execute("insert into payroll values({},'{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(2,"ghana","badangpet","director",'120','300','7200','530','36000','28800'))
    except Exception as e:
        print(e)    
    c.execute("select * from payroll")
    rows= c.fetchall()
    for i in rows:
        print(i)
    con.commit()
    con.close()