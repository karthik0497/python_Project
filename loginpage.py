from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector


def forget_page():
    
    def change_password():
        password = frame4.get()
        if frame3.get()=='' or frame4.get()=='' or frame5.get()=='':
            messagebox.showerror("error","All fields are required",parent=window)
        elif frame4.get()!= frame5.get():
            messagebox.showerror("error","password mismatched",parent=window)
        elif len(password) < 8 :
            messagebox.showerror("Error", "Invalid password must have more than 8 char and numeric")
        else:
             con = mysql.connector.connect(host="localhost",user="root",
                                        password="@K4r7h1k0497",database="userdata")
             mycursor=con.cursor() 
             query='select * from data where username=%s'
             mycursor.execute(query,(frame3.get(),))
             row=mycursor.fetchone()                                   # after executing a select query with the help of cursor object using execute() method. The fetchone() method is used to fetch the first row of data returned by the select query and storing it into the variable "row".
             if row ==None:
                  messagebox.showerror("error","incorrect username",parent=window)
             else:                                                     #These two resulting strings are then stored in a tuple values, separated
                query='update data set password=%s where username=%s'  # Construct the SQL query with placeholders.
                values=str(frame4.get()),str(frame3.get())             # Prepare parameters to substitute into the query string.
                mycursor.execute(query,values)                         # Execute the query with given parameters.
                con.commit()                                           # Commit changes to the database.
                con.close()                                            # Close the database connection.
                messagebox.showinfo("success","password reset login with new password",parent=window)  # Display a success message.
                window.destroy()                                       # Close the window where the password was reset.
                                
                 
    window=Toplevel()
    window.title('change password')
    window.geometry("500x500")
    window.configure(bg="white")
   
    
    heading1=Label(window,text="Reset password",font=("Helvetica", 25, "bold"),bg="white",
              fg="#5AE4A8")
    heading1.pack(pady=10)

    username1=Label(window,text="Username",font=("Helvetica", 15, "bold"),fg="#5AE4A8",bg="white")
    username1.pack(pady=10)
    frame3=Entry(window,width=27,bg="#5AE4A8",bd=0,fg="black",
             font=("Helvetica", 15, "bold"))
    frame3.pack(pady=2)
    
    password1=Label(window,text="new Password",font=("Helvetica", 15, "bold"),fg="#5AE4A8",bg="white")
    password1.pack(pady=5)
    frame4=Entry(window,width=27,bg="#5AE4A8",bd=0,fg="black",
             font=("Helvetica", 15, "bold"))
    frame4.pack(pady=5)
    
    cnfm_password=Label(window,text="Confirm password",font=("Helvetica", 15, "bold"),fg="#5AE4A8",bg="white")
    cnfm_password.pack(pady=5)
    frame5=Entry(window,width=27,bg="#5AE4A8",bd=0,fg="black",
                font=("Helvetica", 15, "bold"))
    frame5.pack(pady=10)
    
    signupbutton=Button(window,text="Submit",font=("Helvetica", 15, "bold"),bd=0,
                   activeforeground="white",activebackground="#5AE4A8",width=25,
              fg="white",bg="#5AE4A8",command=change_password)
    signupbutton.pack(pady=25)
    
    window.mainloop()


def menuwindow():
    login_window.destroy()
    import menuwindow

def login_user():
    if username.get()=="" or password.get()=="":
        messagebox.showerror("error","All fields are required")
        
    else:
        try:
            con = mysql.connector.connect(host="localhost",user="root",
                                        password="@K4r7h1k0497",database="userdata")
            mycursor=con.cursor() 
        except:
           messagebox.showerror('error','connection is not established try again')
           return #there is no point in continuing if a database connection cannot be established.
        query = 'select * from data where username=(%s) and password=%s'   #The (%) syntax indicates that these parameters will be provided separately when the query is executed.
        values=str(username.get()),str(password.get())
        mycursor.execute(query,values)  # line executes the SQL query with the provided values using the cursor's execute() method
        row=mycursor.fetchone()
        if row==None:  # retrieves the first row of the query result using the cursor's fetchone() method. If no rows were returned (i.e., row is None), an error message is displayed 
            messagebox.showerror('error','invalid username and password')
        else:
            messagebox.showinfo('success','login success')
            menuwindow()


def sign_up_page():
    login_window.destroy()
    import signuppage

def userclick(event):
    if username.get()=="Username":
        username.delete(0,END)

def passwordclick(event):
    if password.get()=="Password":
        password.delete(0,END)
    
def hide():
    openeye.config(file="closeeye1.png")      
    password.config(show='*')
    eyebutton.config(command=show)
    
def show():
    openeye.config(file="openeye1.png") 
    password.config(show='')
    eyebutton.config(command=hide)
    

login_window = Tk()
login_window.geometry("1366x768")
login_window.resizable(0,0)
login_window.title("LOGIN PAGE")
bg =PhotoImage(file="untitled.png")
bgpic=Label(login_window,image=bg)
bgpic.place(x=0,y=0)

"""TITLE RUNNING LOOP  ------   For example, if the original string is "Hello World!",
the update_label_text function will generate a new string "ello World!H" 
and set it as the label's text.
The function then schedules itself to run again after 100 milliseconds
using the after method of the window object,
creating a looping effect that continuously updates the label text.. """

Title_Frame = Frame(login_window, width=1100, height=150, bg='white',
                     relief='ridge')
Title_Frame.pack(side=TOP, pady=5)
label = Label(Title_Frame, 
              text="Experience   our   platform   to   the   fullest   by   becoming   a   registered   user .   Log   in   or   sign   up   now   !!!!!!  ",
              font=("Helvetica", 18, "bold"), bg='white',fg="black", padx=300)
label.pack()

def update_label_text():
    new_text = label['text'][1:] + label['text'][0]
    label.config(text=new_text)
    
    login_window.after(100, update_label_text)   
# Schedule the first update of the label text
update_label_text()



heading=Label(login_window,text="User Login",font=("Helvetica", 25, "bold"),bd=0,
              fg="#5AE4A8",bg="white")
heading.place(x=930,y=150)


#the bind method is used to attach the userclick function to the FocusIn event. 
username=Entry(login_window,width=25,font=("Helvetica", 12, "bold"),bd=0,fg="#1F3334")
username.place(x=900,y=240)
username.insert(0,"Username")
username.bind('<FocusIn>',userclick)
frame1=Frame(login_window,width=250,height=2,bg="#5AE4A8").place(x=900,y=262)



password=Entry(login_window,width=25,font=("Helvetica", 12, "bold"),bd=0,fg="#1F3334")
password.place(x=900,y=310)
password.insert(0,"Password")
password.bind('<FocusIn>',passwordclick)
frame2=Frame(login_window,width=250,height=2,bg="#5AE4A8").place(x=900,y=332)

openeye=PhotoImage(file="openeye1.png")
eyebutton=Button(login_window,image=openeye,bd=0,bg='white',cursor='hand2',command=hide)
eyebutton.place(x=1128,y=308)

forgetbutton=Button(login_window,text="Forget Password?",font=("Helvetica", 10, "bold"),bd=0,bg='white',
                    cursor='hand2',fg="#1F3334", activeforeground="#5AE4A8",activebackground='white',command=forget_page)
forgetbutton.place(x=1040,y=350)

loginbutton=Button(login_window,text="Log In",font=("Helvetica", 15, "bold"),bd=0,
                   activeforeground="white",activebackground="#5AE4A8",width=21,command=login_user,
              fg="white",bg="#5AE4A8").place(x=900,y=420)

orlabel=Label(login_window,text="---------------OR----------------",  fg="#5AE4A8",
              font=("Helvetica", 15, "bold"),bg="white")
orlabel.place(x=900,y=500)


fb=PhotoImage(file="facebook.png")
fbbutton=Button(login_window,image=fb,bd=0,bg='white',cursor='hand2')
fbbutton.place(x=960,y=560)

google=PhotoImage(file="google.png")
fbbutton=Button(login_window,image=google,bd=0,bg='white',cursor='hand2')
fbbutton.place(x=1020,y=560)

twitter=PhotoImage(file="twitter.png")
fbbutton=Button(login_window,image=twitter,bd=0,bg='white',cursor='hand2')
fbbutton.place(x=1080,y=560)


signup_page=Label(login_window,text="Dont have an account?", fg="#5AE4A8",
              font=("Helvetica", 12, "bold"),bg="white")
signup_page.place(x=900,y=610)


new_account_button=Button(login_window,text="Create New One",font=("Helvetica", 8, "bold underline"),bd=0,
                   activeforeground="blue",cursor="hand2",
              fg="blue",bg="white",command=sign_up_page).place(x=1080,y=613)

login_window.mainloop()