from cgitb import text
from dataclasses import dataclass
from sre_constants import SUCCESS
from tkinter import *
from tkinter import ttk
from typing import ValuesView
import mysql.connector
from tkinter import messagebox
import datetime
import tkinter



from pip import main
class library_management_system:
    def __init__(self,value):
        self.value=value
        self.value.title("library management system")
        self.value.geometry("1100x700+0+0")

        self.member_var=StringVar()
        self.pnrno_var=StringVar()
        self.fullname_var=StringVar()
        self.address_var=StringVar()
        self.postid_var=StringVar()
        self.phoneno_var=StringVar()
        self.bookid_var=StringVar()
        self.booktitle_var=StringVar()
        self.authorname_var=StringVar()
        self.dateofborrow_var=StringVar()
        self.dateofdue_var=StringVar()
        self.dateonbook_var=StringVar()
        self.latereturnbook_var=StringVar()
        self.newbookname_var=StringVar()
        self.newbookId_var=StringVar()
        self.newbookauthor_var=StringVar()

        lbltitle=Label(self.value,text="LIBRARY MANAGEMENT SYSTEM",fg="green",bd=20,relief=RIDGE,font=("times new roman",50,"bold"),padx=2,pady=6)
        lbltitle.pack(side=TOP,fill=X)

        frame=Frame(self.value,bd=12,relief=RIDGE,padx=2,bg="powder blue")
        frame.place(x=0,y=130,width=1440,height=400)
        

        dataframeleft=LabelFrame(frame,text="Library Membership information",bg="powder Blue",fg="green",bd=12,relief=RIDGE,font=("times new roman",12,"bold"))
        dataframeleft.place(x=0,y=5,width=900,height=350)
        lblmember=Label(dataframeleft,bg="powder blue",text="Member type",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblmember.grid(row=0,column=0,sticky=W)
        comMember=ttk.Combobox(dataframeleft,font=("times new roman",12,"bold"),textvariable=self.member_var,width=27,state="readonly")
        comMember["value"]=("Admin staf","student","lecturer")
        comMember.grid(row=0,column=1)

        lblPRN_no=Label(dataframeleft,bg="powder blue",text="PNR No",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblPRN_no.grid(row=1,column=0,sticky=W)
        txtPRN_no=Entry(dataframeleft,textvariable=self.pnrno_var,font=("times new roman",12,"bold"),width=29)
        txtPRN_no.grid(row=1,column=1)

        

        lblFull_name=Label(dataframeleft,bg="powder blue",text="Full Name",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblFull_name.grid(row=2,column=0,sticky=W)
        txtFull_name=Entry(dataframeleft,textvariable=self.fullname_var,font=("times new roman",12,"bold"),width=29)
        txtFull_name.grid(row=2,column=1)

        lblAddress=Label(dataframeleft,bg="powder blue",text="Address",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblAddress.grid(row=3,column=0,sticky=W)
        txtAddress=Entry(dataframeleft,textvariable=self.address_var,font=("times new roman",12,"bold"),width=29)
        txtAddress.grid(row=3,column=1)

        lblPostcode=Label(dataframeleft,bg="powder blue",text="Post Code",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblPostcode.grid(row=4,column=0,sticky=W)
        txtPostcode=Entry(dataframeleft,textvariable=self.postid_var,font=("times new roman",12,"bold"),width=29)
        txtPostcode.grid(row=4,column=1)

        lblPhn_no=Label(dataframeleft,bg="powder blue",text="Phone No",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblPhn_no.grid(row=5,column=0,sticky=W)
        txtPhn_no=Entry(dataframeleft,textvariable=self.phoneno_var,font=("times new roman",12,"bold"),width=29)
        txtPhn_no.grid(row=5,column=1)

        lblBookid=Label(dataframeleft,bg="powder blue",text="Book ID",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblBookid.grid(row=0,column=2,sticky=W)
        txtBookid=Entry(dataframeleft,textvariable=self.bookid_var,font=("times new roman",12,"bold"),width=29)
        txtBookid.grid(row=0,column=3)

        lblBook_title=Label(dataframeleft,bg="powder blue",text="Book Title",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblBook_title.grid(row=1,column=2,sticky=W)
        txtBook_title=Entry(dataframeleft,textvariable=self.booktitle_var,font=("times new roman",12,"bold"),width=29)
        txtBook_title.grid(row=1,column=3)

        lblauthorname=Label(dataframeleft,bg="powder blue",text="Author Nmae",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblauthorname.grid(row=2,column=2,sticky=W)
        txtauthorname=Entry(dataframeleft,textvariable=self.authorname_var,font=("times new roman",12,"bold"),width=29)
        txtauthorname.grid(row=2,column=3)

        lbldateofborrow=Label(dataframeleft,bg="powder blue",text="Member type",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbldateofborrow.grid(row=0,column=0,sticky=W)
        comdateofborrow=ttk.Combobox(dataframeleft,font=("times new roman",12,"bold"),textvariable=self.dateofborrow_var,width=27,state="readonly")
        comdateofborrow["value"]=("Auto")
        comdateofborrow.grid(row=0,column=1)

        lbldatedue=Label(dataframeleft,bg="powder blue",text="Member type",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbldatedue.grid(row=0,column=0,sticky=W)
        comdatedue=ttk.Combobox(dataframeleft,font=("times new roman",12,"bold"),textvariable=self.dateofdue_var,width=27,state="readonly")
        comdatedue["value"]=("Auto")
        comdatedue.grid(row=0,column=1)

        lbldaysonbook=Label(dataframeleft,bg="powder blue",text="Days on Book",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbldaysonbook.grid(row=5,column=2,sticky=W)
        txtdaysonbook=Entry(dataframeleft,textvariable=self.dateonbook_var,font=("times new roman",12,"bold"),width=29)
        txtdaysonbook.grid(row=5,column=3)

        

        lbllatereturn=Label(dataframeleft,bg="powder blue",text="Late Return Fine",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbllatereturn.grid(row=6,column=2,sticky=W)
        txtlatereturn=Entry(dataframeleft,textvariable=self.latereturnbook_var,font=("times new roman",12,"bold"),width=29)
        txtlatereturn.grid(row=6,column=3)



       

        dataframeright=LabelFrame(frame,text="Book Details",bg="powder Blue",fg="green",bd=12,relief=RIDGE,font=("times new roman",12,"bold"))
        dataframeright.place(x=910,y=5,width=500,height=350)

        lblnewbookdetail=Label(dataframeright,bg="powder blue",text="NEW BOOK DETAIL",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblnewbookdetail.grid(row=2,column=0,sticky=W)

        lblnewbookname=Label(dataframeright,bg="powder blue",text="Full Name",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblnewbookname.grid(row=3,column=0,sticky=W)
        txtnewbookname=Entry(dataframeright,textvariable=self.newbookname_var,font=("times new roman",12,"bold"),width=29)
        txtnewbookname.grid(row=3,column=0)
        lblnewbookid=Label(dataframeright,bg="powder blue",text="Book ID",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblnewbookid.grid(row=4,column=0,sticky=W)
        txtnewbookid=Entry(dataframeright,textvariable=self.newbookId_var,font=("times new roman",12,"bold"),width=29)
        txtnewbookid.grid(row=4,column=0)
        lblnewbookauthor=Label(dataframeright,bg="powder blue",text="Book Auhtor",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblnewbookauthor.grid(row=5,column=0,sticky=W)
        txtnewbookauthor=Entry(dataframeright,textvariable=self.newbookauthor_var,font=("times new roman",12,"bold"),width=29)
        txtnewbookauthor.grid(row=5,column=0)
        
        
        


        listScrollbar=Scrollbar(dataframeright)
        listScrollbar.grid(row=1,column=2,sticky="ns")
        

                

        listofbooks=self.fatchbook_data()

        listBox=Listbox(dataframeright,font=("arial",12,"bold"),width=50,height=7)
       # Listbox.bind("<<listboxselect>>",selectbook)
        listBox.grid(row=1,column=0,padx=0)
        listScrollbar.config(command=Listbox.yview)

        for  item in listofbooks:
            listBox.insert(END,item) 

        buttonframe=Frame(self.value,bd=12,relief=RIDGE,padx=2,bg="powder blue")
        buttonframe.place(x=0,y=530,width=1440,height=70)
        
        btnadddata=Button(buttonframe,command=self.add_data(),text="Add Data",font=("arial",12,"bold"),width=22,bg="red",fg="white")
        btnadddata.grid(row=0,column=0)

        btnadddata=Button(buttonframe,command=self.add_Book(),text="Add Book",font=("arial",12,"bold"),width=22,bg="red",fg="white")
        btnadddata.grid(row=0,column=1)

        btnadddata=Button(buttonframe,command=self.checkbook(),text="Check Book",font=("arial",12,"bold"),width=22,bg="red",fg="white")
        btnadddata.grid(row=0,column=2)

        btnadddata=Button(buttonframe,commond=self.delete(),text="Delete",font=("arial",12,"bold"),width=22,bg="red",fg="white")
        btnadddata.grid(row=0,column=3)

        btnadddata=Button(buttonframe,command=self.reset(),text="Reset",font=("arial",12,"bold"),width=22,bg="red",fg="white")
        btnadddata.grid(row=0,column=4)

        btnadddata=Button(buttonframe,command=self.Iexit(),text="Exit",font=("arial",12,"bold"),width=22,bg="red",fg="white")
        btnadddata.grid(row=0,column=5)

        framedetail=Frame(self.value,bd=12,relief=RIDGE,padx=2,bg="powder blue") 
        framedetail.place(x=0,y=600,width=1440,height=200)

        table_frame=Frame(framedetail,bd=12,relief=RIDGE,padx=2,bg="powder blue")
        table_frame.place(x=0,y=2,width=1400,height=175)
        xscroll=Scrollbar(table_frame,orient=HORIZONTAL)
        yscroll=Scrollbar(table_frame,orient=VERTICAL)
    

        self.library_table=ttk.Treeview(table_frame,columns=("membertype","prnno","fullname","adress","postid","mobile","bookid",
        "booktitle","authorname","date of borrow","datedue","days on book","late return fine"),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)
        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=X)
        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)
        self.library_table.heading("membertype",text="Member Type")
        self.library_table.heading("prnno",text="PRN No")
        self.library_table.heading("fullname",text="Full Name")
        self.library_table.heading("adress",text="Address")
        self.library_table.heading("postid",text="Post ID")
        self.library_table.heading("mobile",text="Phone No")
        self.library_table.heading("bookid",text="Book ID")
        self.library_table.heading("booktitle",text="Book Title")
        self.library_table.heading("authorname",text="Author Name")
        self.library_table.heading("date of borrow",text="Date of Borrow")
        self.library_table.heading("datedue",text="Date Due")
        self.library_table.heading("days on book",text="Days of Book")
        self.library_table.heading("late return fine",text="Late Return Fine")
        self.library_table["show"]="headings"
        self.library_table.pack(fill=BOTH,expand=1)

        self.library_table["show"]="headings"
        self.library_table.pack(fill=BOTH,expand=1)
        self.fatch_data
        self.library_table.bind("<<>buttonRelease>",self.get_cursor)
        
    def add_data(self):
        self.auto()
    
        conn=mysql.connector.connect(host="localhost",username="root",password="test@123",database="librarymanagementsystem")
        my_coursor=conn.cursor() 
        my_coursor.execute("insert into library values(&s,&s,&s,&s,&s,&s,&s,&s,&s,&s,&s,&s,&s)",(     
        self.member_var.get(),
        self.pnrno_var.get(),
        self.fullname_var.get(),
        self.address_var.get(),
        self.postid_var.get(),
        self.phoneno_var.get(),
        self.bookid_var.get(),
        self.booktitle_var.get(),
        self.authorname_var.get(),
        self.dateofborrow_var.get(),
        self.dateonbook_var.get(),
        self.latereturnbook_var.get()
        ))
        
        conn.commit()
        self.fatch_data()
        conn.close()

        messagebox.showinfo("success","member has been inserted successfully")

    def add_Book(self):
        
        conn=mysql.connector.connect(host="localhost",username="root",password="test@123",database="librarymanagementsyste")
        my_coursor=conn.cursor()  
        my_coursor.execute("insert into library_book values(&s,&s,&s)",(
            self.newbookname_var.get(),
            self.newbookId_var.get(),
            self.newbookauthor_var.get()

        ))
        conn.commit()
        self.fatchbook_data()
        conn.close()  

    def fatch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="test@123",database="librarymanagementsystem")
        my_coursor=conn.cursor() 
        my_coursor.execute("select * from library")
        rows=my_coursor.fetchall()
        if len(rows)!=0:
            self.library_table.delete(*self.library_table.get_children())
            for i in rows:
                self.library_table.insert("",END,values=i)
            conn.commit()
        conn.close() 

    def fatchbook_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="test@123",database="librarymanagementsystem")
        my_coursor=conn.cursor() 
        my_coursor.execute("select * from library_book")
        rows=my_coursor.fetchall()
        for x in rows:
            print(x)
        conn.commit()
        conn.close()    



    def get_cursor(self,evevt=""):
        cursor_row=self.library_table.focus()
        content=self.library_table.item(cursor_row)
        row=content["value"]
        self.member_var.set(row[0])    
        self.pnrno_var.set(row[2])
        self.fullname_var.set(row[3])  
        self.address_var.set(row[4])  
        self.postid_var.set(row[5])   
        self.phoneno_var.set(row[6])  
        self.bookid_var.set(row[7])  
        self.booktitle_var.set(row[8])  
        self.authorname_var.set(row[9])  
        self.dateofborrow_var.set(row[10])  
        self.dateofdue_var.set(row[11])  
        self.dateonbook_var.set(row[12])  
        self.latereturnbook_var.set(row[13])                     

    def auto(self):
        d1=datetime.datetime.today()
        d2=datetime.timedelta(days=15)
        d3=d1=d2
        self.dateofborrow_var.set(d1)
        self.dateofdue_var.set(d3)
        self.dateonbook_var.set(15)    
    def check(self):
        a=self.newbookname_var.get()

        conn=mysql.connector.connect(host="localhost",username="root",password="test@123",database="librarymanagementsystem")
        my_coursor=conn.cursor() 
        q=("SELECT EXISTS(SELECT * from library_book WHERE Book Name=%s")
        my_coursor.execute(q,a)
        conn.commit
        self.fatchbook_data()
        conn.close
        
    def  checkbook(self):
        
        if self.check is True:  
            messagebox.showinfo("the book is available")
        else:
            messagebox.showinfo("0")    
        
    def reset(self):
        self.member_var.set("")  
        self.pnrno_var.set("")
        self.fullname_var.set("")  
        self.address_var.set("")  
        self.postid_var.set("")   
        self.phoneno_var.set("")  
        self.bookid_var.set("")  
        self.booktitle_var.set("")  
        self.authorname_var.set("")  
        self.dateofborrow_var.set("")  
        self.dateofdue_var.set("")  
        self.dateonbook_var.set("")  
        self.latereturnbook_var.set("")
        
    def Iexit(self):
        Iexit=tkinter.Messagebox.askyesno("Library management system","Do you want to exit")
        if Iexit>0:
            self.value.destroy()
            return

    def delete(self):
        if self.phoneno_var.get=="" or self.fullname_var.get=="":
            messagebox.showerror("Error","first select the member")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="test@123",database="librarymanagementsystem")
            my_coursor=conn.cursor()
            query="delete from library where PRN_No=%s"
            value=(self.phoneno_var.get())
            my_coursor.execute(query,value)
            conn.commit()
            self.fatch_data()
            self.reset()
            conn.close()
            messagebox.showinfo("Success","member has been Deleted")



        
        
if __name__=="__main__":
    value=Tk()
    obj=library_management_system(value)
    value.mainloop()


