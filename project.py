from tkinter import *
from tkinter import ttk
import mysql.connector
from datetime import datetime  
import webbrowser


# MySQL connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="@K4r7h1k0497",
    database="userdata"
)

#Tkinter 
app = Tk()
app.title("Crypto Portfolio Tracker")
app.title("menu page")
app .geometry("1366x768")
app .resizable(0,0)
bg1 =PhotoImage(file="tele.png")
bgpic=Label(app,image=bg1)
bgpic.place(x=0,y=0)

#functions for adding and showing portfolio
def add_to_portfolio():
    # Get data from input fields
    name = name_input.get()
    symbol = symbol_input.get()
    amount = float(amount_input.get())
    price = float(price_input.get())
    value = amount * price
    buy= buy_var.get()
    sell=sell_var.get()
     # Get selected option from checkbuttons
    if buy_var.get() == 1:
        option = "Buy"
    elif sell_var.get() == 1:
        option = "Sell"
    else:
        option = ""
    

    # Get current date and time
    now =datetime.now()
    dt_string = now.strftime("%Y-%m-%d %H:%M:%S")

   # Insert data into MySQL database
    mycursor = mydb.cursor()
    sql = "INSERT INTO portfolio (name, symbol, Amount, price, value, date, options) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    val = (name, symbol, amount, price, value, dt_string, option)
    mycursor.execute(sql, val)
    mydb.commit()

    # Clear input fields
    name_input.delete(0, END)
    symbol_input.delete(0, END)
    amount_input.delete(0, END)
    price_input.delete(0, END)
    buy_var.set(0)
    sell_var.set(0)


def show_portfolio():
    # Get data from MySQL database
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM portfolio")
    portfolio_data = mycursor.fetchall()  #retrieves all the rows

    # Create new window for displaying portfolio
    portfolio_window = Toplevel()
    portfolio_window.title("Portfolio")

    # Create table for displaying portfolio data
    table = Frame(portfolio_window)
    table.pack()

    # Create headers for table
    headers = ["id", "Name", "Symbol", "Amount", "Price", "Value", "Date/Time", "Options", "Action"]
                                                                    #   Each header label is placed in the table 
                                                                    # frame at the Respective column index.
    for i in range(len(headers)):
        header_label = Label(table, text=headers[i])
        header_label.grid(row=0, column=i)
    
                                                                    # corresponding to the seven columns in the first row of portfolio_data.
                                                                    # Add portfolio data to table
    total_value = 0
    for i in range(len(portfolio_data)):                            #first iteration of the outer loop (when i is 0)
        for j in range(len(portfolio_data[i])):                     #the length of portfolio_data[i] is 7,
            cell_label = Label(table, text=portfolio_data[i][j])    #inner loop will iterate over j values of 0, 1, 2, 3, 4, 5, and 6, 
            cell_label.grid(row=i+1, column=j)                      #Add portfolio data to table
            cell_label = Label(table, text=portfolio_data[i][j]) 
            if j == 6: # column index for date/time
                # format date and time
                dt_string = datetime.strptime(portfolio_data[i][j], "%Y-%m-%d %H:%M:%S") #i is row=0 and j column=6
                formatted_dt = dt_string.strftime("%m/%d/%Y %I:%M %p")   #converting datetime formate to our date  string
                cell_label.config(text=formatted_dt)
                cell_label.grid(row=i+1, column=j)

                                                          
        delete_button = Button(table, text="Delete", command=lambda row=i: delete_row(row))
        delete_button.grid(row=i+1, column=len(headers)-1)    #  lambda function that takes one argument (row) 
                                                              # and calls the delete_row function with that argument.        
                                                              # if row = 0 column = 9-1=8 so button will place the 8 column
                                                              #column parameter is set to len(headers)-1 so that the buttons
                                                              # will be placed in the right of column of the table.
        total_value += portfolio_data[i][4] * portfolio_data[i][3] 
   
                                        # multiplying the "Price" (portfolio_data[i][4]) 
                                        # and "Amount" (portfolio_data[i][3]) columns together.
                                        #every iterate it will add the value one by one it displayed in totall value label

    #  displaying total value of portfolio
    total_value_label = Label(portfolio_window, text="Total Value: $" + "{:.2f}".format(total_value))
    total_value_label.pack()            #"{:.2f}" string formatting syntax.

    # label for displaying current date and time
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")  # format date and time
    date_label = Label(portfolio_window, text="Last updated: " + dt_string)
    date_label.pack(side=BOTTOM)

def delete_row(row):
    # Get ID of row to be deleted
    mycursor = mydb.cursor()   #creating a database cursor using the mydb.cursor() method.
    mycursor.execute("SELECT id FROM portfolio") #SQL SELECT statement using the cursor to retrieve all the IDs from the "portfolio" table.
    id_list = mycursor.fetchall()         #The result of the query is stored in the id_list variable using the fetchall() method, 
                                          # which retrieves all the rows returned by the query as a list of tuple
                                          
    id_to_delete = id_list[row][0]        #The ID is stored in the id_to_delete variable.
                                          #  entire row will store in variable id_to_delete
                                          # Extracts the ID of the row to be deleted from the id_list variable.
    mycursor.execute("DELETE FROM portfolio WHERE id = %s", (id_to_delete,))
    mydb.commit()
   # Destroy Toplevel window
    # table.destroy()
    # Refresh portfolio display
    show_portfolio()

# Create labels and input fields for adding coins to portfolio

name_label = Label(app, text=" Name",font=("Helvetica", 15, "bold"),bg="#49A2D8",fg="black")
name_label.place(x=100,y=150)
name_input = Entry(app)
name_input.place(x=190,y=150)

symbol_label = Label(app, text=" Symbol",font=("Helvetica", 15, "bold"),bg="#49A2D8",fg="black")
symbol_label.place(x=100,y=200)
symbol_input = Entry(app)
symbol_input.place(x=190,y=200)

amount_label = Label(app, text=" amount",font=("Helvetica", 15, "bold"),bg="#49A2D8",fg="black")
amount_label.place(x=100,y=250)
amount_input = Entry(app)
amount_input.place(x=190,y=250)

price_label = Label(app, text=" Price",font=("Helvetica", 15, "bold"),bg="#49A2D8",fg="black")
price_label.place(x=100,y=300)
price_input = Entry(app)
price_input.place(x=190,y=300)

add_button = Button(app, text="Add to Portfolio", command=add_to_portfolio,
                    font=("Helvetica", 13, "bold"),bg="#49A2D8",fg="black")
add_button.place(x=200,y=360)


show_button = Button(app, text="Show Portfolio", command=show_portfolio,
                     font=("Helvetica", 13, "bold"),bg="#49A2D8",fg="black")
show_button.place(x=200,y=400)

Title = Label(app, 
              text="Maximize Your Investments: Monitor Your Portfolio with Ease",
              font=("Helvetica", 18, "bold"), bg='#49A2D8',fg="black")
Title.place(x=20,y=80)  

buy_var = IntVar()
sell_var = IntVar()
buy_checkbutton = Checkbutton(app, text="Buy", variable=buy_var,
                              font=("Helvetica", 13, "bold"),bg="#49A2D8",fg="black")
buy_checkbutton.place(x=105,y=360)

sell_checkbutton = Checkbutton(app, text="Sell", variable=sell_var,
                               font=("Helvetica", 13, "bold"),bg="#49A2D8",fg="black")
sell_checkbutton.place(x=105,y=400)

def callback(url):
    webbrowser.open_new_tab(url)

link=Label(app,text="crypto calender ?click here",font=('Helveticabold', 10, 'bold'),
                            bg='#49A2D8',fg="black",cursor="hand2")
link.place(x=50,y=500)
link.bind("<Button-1>",lambda d:callback("https://cryptomarketcal.com"))

link1=Label(app,text="Technical analysis? click here",font=('Helveticabold', 10, 'bold'),
                            bg='#49A2D8',fg="black",cursor="hand2")
link1.place(x=50,y=530)
link1.bind("<Button-1>",lambda d:callback("https://www.tradingview.com"))

link3=Label(app,text="check active projects? click here",font=('Helveticabold', 10, 'bold'),
                            bg='#49A2D8',fg="black",cursor="hand2")
link3.place(x=50,y=560)
link3.bind("<Button-1>",lambda d:callback("https://www.cryptomiso.com"))

link4=Label(app,text="check transaction status? click here",font=('Helveticabold', 10, 'bold'),
                          bg='#49A2D8',fg="black",cursor="hand2")
link4.place(x=50,y=590)
link4.bind("<Button-1>",lambda d:callback("https://www.blockchair.com"))

link1=Label(app,text="check market sentiment? click here",font=('Helveticabold', 10, 'bold'),
                             bg='#49A2D8',fg="black",cursor="hand2")
link1.place(x=50,y=620)
link1.bind("<Button-1>",lambda d:callback("https://www.cryptopanic.com"))


def log_in_page():
    app.destroy()
    import loginpage
    
def pricetracking_page():
    app.destroy()
    import telegramtrack
    
tracking_page_button=Button(app,text="price tracking page",font=("Helvetica", 8, "bold underline"),bd=0,
                   activeforeground="blue",cursor="hand2",
              bg="#49A2D8",fg="black",command=pricetracking_page).place(x=1050,y=650)

login_page_button=Button(app,text="Log out",font=("Helvetica", 8, "bold underline"),bd=0,
                   activeforeground="blue",cursor="hand2",
              bg="#49A2D8",fg="black",command=log_in_page).place(x=1050,y=680)

# Run Tkinter application
app.mainloop()