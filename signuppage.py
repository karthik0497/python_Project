from tkinter import*
import mysql.connector
from tkinter import messagebox


#functionality part
def clear():
    frame2.delete(0,END)
    frame3.delete(0,END)
    frame4.delete(0,END)
    frame5.delete(0,END)
    check.set(0)

def connect_database():
    email = frame2.get()
    password = frame4.get()
    if frame2.get()=="" or frame3.get()=="" or frame4.get()=="" or frame5.get()=="":
        messagebox.showerror("error","All fields are required")
    elif len(email) < 8 and "@" not in email and ".com" not in email:
        messagebox.showerror("Error", "Invalid email address")
    elif frame4.get() != frame5.get():
        messagebox.showerror("error","password mismatch")
    elif len(password) < 8 :
        messagebox.showerror("Error", "Invalid password must have more than 8 char and numeric")
    elif check.get()==0:   #uncheck
        messagebox.showerror("error","please accept terms and condition")
    else:
        con = mysql.connector.connect(host="localhost",user="root",
                                        password="@K4r7h1k0497",database="userdata")
        mycursor=con.cursor()
    
    """"to check for None because if the query does not return any results, the fetchone() method returns None,
the query returns no results, the row variable will be set to None
       If row is not None, it means that the query returned at least one row, 
       which means that the username already exists in the database.
        
    """
    query = 'select * from data where username=(%s)'
    mycursor.execute(query, (frame3.get(),))  
    row=mycursor.fetchone()                #FETCH THAT ROW THER WILL BE A USERNAME 
    if row !=None:                         #row is not None,is not equal to none 
        messagebox.showerror('error','username  alrady existed') 
                                           # Displays an error message with the text 'username already existed' using a message box pop-up.
            
    else:   
        
                   
            # Prepare the query with placeholders for the values
        query = 'INSERT INTO data(email,username,password) VALUES (%s,%s,%s)'

            # Specify the values to insert as a tuple
        values = (str(frame2.get()), str(frame3.get()), str(frame4.get()))

            # Execute the query with parameterized values
        mycursor.execute(query, values)

        con.commit()
        con.close()
        messagebox.showinfo('success','registration successful') 
        clear()                                 #calling function to delete all entry
        signin_window.destroy()
        import loginpage
            
def log_in_page():
    signin_window.destroy()
    import loginpage

# GUI part
signin_window=Tk()
signin_window.geometry("1366x768")
background=PhotoImage(file="untitled.png")
bgpic1=Label(signin_window,image=background)
bgpic1.place(x=0,y=0)
signin_window.resizable(0,0)

"""TITLE RUNNING LOOP """
Title_Frame1 = Frame(signin_window, width=1100, height=150, bg='white',
                     relief='ridge')
Title_Frame1.pack(side=TOP, pady=5)
label1 = Label(Title_Frame1, 
              text="Experience   our   platform   to   the   fullest   by   becoming   a   registered   user .   Log   in   or   sign   up   now   !!!!!!  ",
              font=("Helvetica", 18, "bold"), bg='white',fg="black", padx=300)
label1.pack()

def update_label_text1():
    new_text1 = label1['text'][1:] + label1['text'][0]
    label1.config(text=new_text1)
                                                  # using the after method creating a looping effect 
    signin_window.after(100, update_label_text1)  # that continuously updates the label text along with gui
 
update_label_text1()                              # Schedule the first update of the label text

#labels and entries 
heading1=Label(signin_window,text="Create an account",font=("Helvetica", 25, "bold"),
              fg="#5AE4A8",bg="white")
heading1.place(x=850,y=150)

email=Label(signin_window,text="Email",font=("Helvetica", 15, "bold"),bg="white",fg="#5AE4A8")
email.place(x=850,y=215)
frame2=Entry(signin_window,width=27,bg="#5AE4A8",bd=0,fg="black",
             font=("Helvetica", 15, "bold"))
frame2.place(x=850,y=240)

username1=Label(signin_window,text="Username",font=("Helvetica", 15, "bold"),bg="white",fg="#5AE4A8")
username1.place(x=850,y=302)
frame3=Entry(signin_window,width=27,bg="#5AE4A8",bd=0,fg="black",
             font=("Helvetica", 15, "bold"))
frame3.place(x=850,y=326)

password1=Label(signin_window,text="Password",font=("Helvetica", 15, "bold"),bg="white",fg="#5AE4A8")
password1.place(x=850,y=385)
frame4=Entry(signin_window,width=27,bg="#5AE4A8",bd=0,fg="black",
             font=("Helvetica", 15, "bold"))
frame4.place(x=850,y=410)

cnfm_password=Label(signin_window,text="Confirm password",font=("Helvetica", 15, "bold"),bg="white",fg="#5AE4A8")
cnfm_password.place(x=850,y=468)
frame5=Entry(signin_window,width=27,bg="#5AE4A8",bd=0,fg="black",
             font=("Helvetica", 15, "bold"))
frame5.place(x=850,y=495)

check=IntVar() #creating variable for check box
termsandcondition=Checkbutton(signin_window,text="I agree to the Terms & Conditions",
                              font=("Helvetica", 8, "bold"),bg="white",bd=0,fg="black",activebackground="white",
                              activeforeground="#5AE4A8",cursor="hand2",variable=check)
termsandcondition.place(x=850,y=523)

signupbutton=Button(signin_window,text="Sign up",font=("Helvetica", 15, "bold"),bd=0,
                   activeforeground="white",activebackground="#5AE4A8",width=25,command=connect_database,
              fg="white",bg="#5AE4A8").place(x=850,y=580)

Haveanaccount=Label(signin_window,text="Already registered?", fg="#5AE4A8",
              font=("Helvetica", 12, "bold"),bg="white")
Haveanaccount.place(x=900,y=650)

login_page_button=Button(signin_window,text="Log In",font=("Helvetica", 8, "bold underline"),bd=0,
                   activeforeground="blue",cursor="hand2",
              fg="blue",bg="white",command=log_in_page).place(x=1050,y=650)

signin_window.mainloop()