
import time
import datetime
from tkinter import *
from tkinter import ttk
import tkinter.messagebox
#from tkinter.ttk import *
#from PIL import *
import mysql.connector
print("started the code")


root=Tk()
root.title("Employee payroll system")
p1=PhotoImage(file='mypic.png')
d1=PhotoImage(file='date.png')
root.iconphoto(False,p1)
root.geometry('%dx%d+0+0'%(root.winfo_screenwidth(),root.winfo_screenheight()))
#root.attributes('-fullscreen', True)
#canvas=Canvas(root,width=1000,height=667)
#canvas.pack()
#mi=PhotoImage(file='C:\\Users\\praveen\\Downloads\\python.png')
#canvas.create_image(0,0,anchor=NW,image=mi)

root.configure(background="powder blue")
Tops=Frame(root,width=1350,height=500,bd=8,bg="powder blue",relief=SUNKEN)
Tops.pack(side=TOP,fill=X)
f3=Frame(root,width=1340,height=140,bd=8,bg="RED",relief=SUNKEN)
f3.pack(side=BOTTOM,expand=1,fill=BOTH)


f1=Frame(root,width=600,height=600,bd=8,bg="powder blue",relief='sunken',borderwidth=10)
f1.pack(side=LEFT,expand=1,fill=X)
f2=Frame(root,width=300,height=700,bd=8,bg="powder blue")
f2.pack(side=RIGHT,fill=X)


fla=Frame(f1,width=600,height=200,bd=8,bg="powder blue",relief='ridge')
fla.pack(side=TOP,expand=1,fill=X)
flb=Frame(f1,width=300,height=600,bd=10,bg="powder blue",relief='sunken')
flb.pack(side=TOP,expand=1,fill=X)


lblinfo=Label(Tops,font=('arial',45,'bold'),text="Employee Payment Management system ",bd=25,fg="light green")
lblinfo.grid(row=0,column=0,sticky="nsew")
Tops.grid_rowconfigure(0, weight=1)
Tops.grid_columnconfigure(0, weight=1)
lblinfo.config(image=p1,compound=RIGHT)
#lblinfo.config(image=p1,compound=LEFT)

def exit():
  exit=tkinter.messagebox.askyesno("Employee system","Do you want to exit the system")
  if exit>0:
    root.destroy()
    return

def reset():
  Name.set("")
  Address.set("")
  HoursWorked.set("")
  wageshour.set("")
  Payable.set("")
  Taxable.set("")
  NetPayable.set("")
  GrossPayable.set("")
  OverTimeBonus.set("")
  Employer.set("")
  NINumber.set("")
  txtpayslip.delete("1.0",END)
def enterinfo():
  txtpayslip.delete("1.0",END)
  txtpayslip.insert(END,"\t\tPay Slip\n\n")
  txtpayslip.insert(END,"Name :\t\t"+Name.get()+"\n\n")
  txtpayslip.insert(END,"Address :\t\t"+Address.get()+"\n\n")
  txtpayslip.insert(END,"Employer :\t\t"+Employer.get()+"\n\n")
  txtpayslip.insert(END,"Emp ID :\t\t"+NINumber.get()+"\n\n")
  txtpayslip.insert(END,"Hours Worked :\t\t"+HoursWorked.get()+"\n\n")
  txtpayslip.insert(END,"Net Payable :\t\t"+NetPayable.get()+"\n\n")
  txtpayslip.insert(END,"Wages per hour :\t\t"+wageshour.get()+"\n\n")
  txtpayslip.insert(END,"Tax Paid :\t\t"+Taxable.get()+"\n\n")
  txtpayslip.insert(END,"Payable :\t\t"+Payable.get()+"\n\n") 
def weeklywages():
  txtpayslip.delete("1.0",END)
  hoursworkedperweek=float(HoursWorked.get())
  wagesperhours=float(wageshour.get())
  
  paydue=wagesperhours*hoursworkedperweek
  paymentdue="INR",str('%.2f'%(paydue))
  Payable.set(paymentdue)
  payable1.set(paydue)

  
  tax=paydue*0.2
  taxable="INR",str('%.2f'%(tax))
  Taxable.set(taxable)
  tax1.set(tax)
  
  netpay=paydue-tax
  netpays="INR",str('%.2f'%(netpay))
  NetPayable.set(netpays)
  netpay1.set(netpay)
  if hoursworkedperweek > 40:
    overtimehours=(hoursworkedperweek-40)+wagesperhours*1.5
    overtime="INR",str('%.2f'%(overtimehours))
    OverTimeBonus.set(overtime)
    overtime1.set(overtimehours)
  elif hoursworkedperweek<=40:
    overtimepay=(hoursworkedperweek-40)+wagesperhours*1.5
    overtimehrs="INR",str('%.2f'%(overtimepay))
    OverTimeBonus.set(overtimehrs)
    overtime1.set(overtimepay)  
  return  
def save():
  if Name.get()=="":
    tkinter.messagebox.showerror("Error","All fields are required")
  else:
    con=mysql.connector.connect(host="localhost",username="root",password="root",database="mysql")
    c=con.cursor()

    try:
      c.execute("create table payroll(empid INT,Name varchar(45),Address varchar(45),Employer varchar(45),HoursWorked varchar(45),wageshour varchar(45),Tax varchar(45),OverTimeBonus varchar(45),Payable varchar(45),Net_pay varchar(45),date_of_pay DATE,PRIMARY KEY (empid))")
    except Exception as e:
      print(e)
    finally:
      try:
        c.execute("insert into payroll values({},'{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(int(NINumber.get()),Name.get(),Address.get(),Employer.get(),HoursWorked.get(),wageshour.get(),tax1.get(),overtime1.get(),payable1.get(),netpay1.get(),DateOfOrder.get()))
      except Exception as e:
        tkinter.messagebox.showerror("Error","u have entered empid wrong plz try agian ")
        print(e)  
      finally:
        tkinter.messagebox.showinfo("SUCCESS","SUCCESSFULLY INSERTED VALUES")
      con.commit()
      con.close()
def display():
  con=mysql.connector.connect(host="localhost",username="root",password="root",database="mysql")
  c=con.cursor()
  c.execute("select * from payroll")
  rows= c.fetchall()
  for i in rows:
        print(i)
  con.commit()
  con.close()      
#=============================== Variables ========================================================

Name=StringVar()
Address=StringVar()
HoursWorked=StringVar()
wageshour=StringVar()
Payable=StringVar()
payable1=StringVar()
Taxable=StringVar()
tax1=StringVar()
NetPayable=StringVar()
netpay1=StringVar()
GrossPayable=StringVar()
overtime1=StringVar()
OverTimeBonus=StringVar()
Employer=StringVar()
NINumber=StringVar()
TimeOfOrder=StringVar()
DateOfOrder=StringVar()

DateOfOrder.set(time.strftime("%Y-%m-%d"))
print(DateOfOrder.get())

#================================ Label Widget =================================================

lblName=Label(fla,text="Name",font=('arial',16,'bold'),bd=20,fg="red",bg="powder blue").grid(row=0,column=0,sticky="nsew")
lblAddress=Label(fla,text="Address",font=('arial',16,'bold'),bd=20,fg="red",bg="powder blue").grid(row=0,column=2)
lblEmployer=Label(fla,text="Employer",font=('arial',16,'bold'),bd=20,fg="red",bg="powder blue").grid(row=1,column=0,sticky="nsew")
lblNINumber=Label(fla,text="Emp ID",font=('arial',16,'bold'),bd=20,fg="red",bg="powder blue").grid(row=1,column=2)
lblHoursWorked=Label(fla,text="Hours Worked",font=('arial',16,'bold'),bd=20,fg="red",bg="powder blue").grid(row=2,column=0,sticky="nsew")
lblHourlyRate=Label(fla,text="Hourly Rate",font=('arial',16,'bold'),bd=20,fg="red",bg="powder blue").grid(row=2,column=2)
lblTax=Label(fla,text="       Tax",font=('arial',16,'bold'),bd=20,anchor='w',fg="red",bg="powder blue").grid(row=3,column=0,sticky="nsew")
lblOverTime=Label(fla,text="OverTime",font=('arial',16,'bold'),bd=20,fg="red",bg="powder blue").grid(row=3,column=2)
lblGrossPay=Label(fla,text="GrossPay",font=('arial',16,'bold'),bd=20,fg="red",bg="powder blue").grid(row=4,column=0,sticky="nsew")
lblNetPay=Label(fla,text="Net Pay",font=('arial',16,'bold'),bd=20,fg="red",bg="powder blue").grid(row=4,column=2)
fla.grid_rowconfigure(2, weight=2)
fla.grid_columnconfigure(2,weight=2)

#=============================== Entry Widget =================================================

etxname=Entry(fla,textvariable=Name,font=('arial',16,'bold'),bd=10,width=22,justify='left')
etxname.grid(row=0,column=1)

etxaddress=Entry(fla,textvariable=Address,font=('arial',16,'bold'),bd=10,width=22,justify='left')
etxaddress.grid(row=0,column=3)

etxemployer=Entry(fla,textvariable=Employer,font=('arial',16,'bold'),bd=10,width=22,justify='left')
etxemployer.grid(row=1,column=1)

etxnin=Entry(fla,textvariable=NINumber,font=('arial',16,'bold'),bd=10,width=22,justify='left')
etxnin.grid(row=1,column=3)

etxhoursworked=Entry(fla,textvariable=HoursWorked,font=('arial',16,'bold'),bd=10,width=22,justify='left')
etxhoursworked.grid(row=2,column=1)

etxwagesperhours=Entry(fla,textvariable=wageshour,font=('arial',16,'bold'),bd=10,width=22,justify='left')
etxwagesperhours.grid(row=2,column=3)

etxtax=Entry(fla,textvariable=Taxable,font=('arial',16,'bold'),bd=10,width=22,justify='left')
etxtax.grid(row=3,column=1)

etxovertime=Entry(fla,textvariable=OverTimeBonus,font=('arial',16,'bold'),bd=10,width=22,justify='left')
etxovertime.grid(row=3,column=3)

etxgrosspay=Entry(fla,textvariable=Payable,font=('arial',16,'bold'),bd=10,width=22,justify='left')
etxgrosspay.grid(row=4,column=1)

etxnetpay=Entry(fla,textvariable=NetPayable,font=('arial',16,'bold'),bd=10,width=22,justify='left')
etxnetpay.grid(row=4,column=3)


#=============================== Text Widget ============================================================

payslip=Label(f2,textvariable=DateOfOrder,font=('arial',21,'bold'),fg="red",bg="powder blue")
payslip.grid(row=0,column=0)
payslip.config(image=d1,compound=LEFT)
txtpayslip=Text(f2,height=22,width=34,bd=16,font=('arial',13,'bold'),fg="green",bg="powder blue")
txtpayslip.grid(row=1,column=0)



#=============================== buttons ===============================================================

btnsalary=Button(flb,text='Weekly Salary',padx=60,pady=5,bd=8,font=('arial',16,'bold'),width=14,fg="red",bg="light green",command=weeklywages)
btnsalary.grid(row=0,column=0)

btnreset=Button(flb,text='Reset',padx=50,pady=9,bd=8,font=('arial',16,'bold'),width=10,command=reset,fg="red",bg="light green")
btnreset.grid(row=0,column=1)

btnpayslip=Button(flb,text='View Payslip',padx=65,pady=9,bd=8,font=('arial',16,'bold'),width=10,command=enterinfo,fg="red",bg="light green")
btnpayslip.grid(row=0,column=3)

btnmysql=Button(flb,text='save',padx=50,pady=12.3,bd=8,font=('arial',16,'bold'),width=10,command=save,fg="red",bg="light green")
btnmysql.grid(row=0,column=2)

btnexit=Button(flb,text='Exit System',padx=75,pady=50,bd=8,font=('arial',10,'bold'),width=8,height=8,command=exit,fg="red",bg="light green")
btnexit.grid(row=0,column=4)

btndisplay=Button(flb,text='Display',padx=30,pady=36,bd=8,font=('arial',16,'bold'),width=10,command=display,fg="red",bg="light green")
btndisplay.grid(row=0,column=5)
#===============================scroll bar==================================================================
"""scroll_x=tkinter.Scrollbar(f3,orient=HORIZONTAL)
scroll_y=tkinter.Scrollbar(f3,orient=VERTICAL)
view_table=ttk.Treeview(f3,column=("NINumber","Name","Address","Employer","HoursWorked","wageshour","tax1","overtime1","payable1","netpay1","DateOfOrder"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)

scroll_x=ttk.Scrollbar(command=view_table.xview)
scroll_y=ttk.Scrollbar(command=view_table.yview)

view_table.heading("NINumber",text="Emp ID")
view_table.heading("Name",text="Name")
view_table.heading("Address",text="Adress")
view_table.heading("Employer",text="Employer")
view_table.heading("HoursWorked",text="HoursWorked")
view_table.heading("wageshour",text="wages per hour")
view_table.heading("tax1",text="Tax")
view_table.heading("overtime1",text="Over time bonus")
view_table.heading("payable1",text="Payable")
view_table.heading("netpay1",text="Netpay")
view_table.heading("DateOfOrder",text="Date of pay")

view_table['show']='headings'
view_table.pack(fill=BOTH,expand=1)
"""#===============================BUTTON IMAGES===============================================================

m1=PhotoImage(file='reset.png')
btnreset.config(image=m1,compound=TOP)

m2=PhotoImage(file='salary.png')
btnsalary.config(image=m2,compound=TOP)

m3=PhotoImage(file='payslip.png')
btnpayslip.config(image=m3,compound=TOP)

m4=PhotoImage(file='exit.png')
btnexit.config(image=m4,compound=TOP)

m5=PhotoImage(file='save2.png')
btnmysql.config(image=m5,compound=TOP)


root.mainloop()



