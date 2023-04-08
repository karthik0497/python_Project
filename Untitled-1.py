from tkinter import *
from tkinter import ttk
import mysql.connector
from datetime import datetime
import webbrowser

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="@K4r7h1k0497",
    database="userdata"
)

app = Tk()
app.title("Crypto Portfolio Tracker")
app.geometry("1366x768")
app.resizable(0, 0)
bg1 = PhotoImage(file="tele.png")
bgpic = Label(app, image=bg1)
bgpic.place(x=0, y=0)

def add_to_portfolio():
    name, symbol, amount, price = name_input.get(), symbol_input.get(), float(amount_input.get()), float(price_input.get())
    value = amount * price
    option = "Buy" if buy_var.get() else "Sell" if sell_var.get() else ""
    now = datetime.now()
    dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
    mycursor = mydb.cursor()
    sql = "INSERT INTO portfolio (name, symbol, Amount, price, value, date, options) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    val = (name, symbol, amount, price, value, dt_string, option)
    mycursor.execute(sql, val)
    mydb.commit()
    name_input.delete(0, END)
    symbol_input.delete(0, END)
    amount_input.delete(0, END)
    price_input.delete(0, END)
    buy_var.set(0)
    sell_var.set(0)

def show_portfolio():
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM portfolio")
    portfolio_data = mycursor.fetchall()
    portfolio_window = Toplevel()
    portfolio_window.title("Portfolio")
    table = Frame(portfolio_window)
    table.pack()
    headers = ["id", "Name", "Symbol", "Amount", "Price", "Value", "Date/Time", "Options", "Action"]
    for i in range(len(headers)):
        header_label = Label(table, text=headers[i])
        header_label.grid(row=0, column=i)
    total_value = 0
    for i, data in enumerate(portfolio_data):
        for j, value in enumerate(data):
            cell_label = Label(table, text=value)
            cell_label.grid(row=i+1, column=j)
            if j == 6:
                dt_string = datetime.strptime(value, "%Y-%m-%d %H:%M:%S")
                formatted_dt = dt_string.strftime("%m/%d/%Y %I:%M %p")
                cell_label.config(text=formatted_dt)
                cell_label.grid(row=i+1, column=j)
        delete_button = Button(table, text="Delete", command=lambda row=i: delete_row(row))
        delete_button.grid(row=i+1, column=len(headers)-1)
        total_value += data[4] * data[3]
    total_value_label = Label(portfolio_window, text="Total Value: $" + "{:.2f}".format(total_value))
    total_value_label.pack()
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    date_label = Label(portfolio_window, text="Last updated: " + dt_string)
    date_label.pack(side=BOTTOM)

def delete_row(row):
# Get ID of row to be deleted
    mycursor = mydb.cursor() #creating a database cursor using the mydb.cursor() method.
    mycursor.execute("SELECT id FROM portfolio")
    ids = mycursor.fetchall()
    row_id = ids[row][0]
    # Delete row from MySQL database
    mycursor.execute("DELETE FROM portfolio WHERE id = %s", (row_id,))
    mydb.commit()   

    
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

# Create button for adding coins to portfolio
add_button = Button(app, text="Add to Portfolio", command=add_to_portfolio,font=("Helvetica", 13, "bold"),bg="#49A2D8",fg="black")
add_button.place(x=200,y=360)

# Create button for showing portfolio
show_button = Button(app, text="Show Portfolio", command=show_portfolio,font=("Helvetica", 13, "bold"),bg="#49A2D8",fg="black")
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
link1.place(x=50,y=520)
link1.bind("<Button-1>",lambda d:callback("https://www.tradingview.com"))

link3=Label(app,text="check active projects? click here",font=('Helveticabold', 10, 'bold'),
                            bg='#49A2D8',fg="black",cursor="hand2")
link3.place(x=50,y=540)
link3.bind("<Button-1>",lambda d:callback("https://www.cryptomiso.com"))

link4=Label(app,text="check transaction status? click here",font=('Helveticabold', 10, 'bold'),
                          bg='#49A2D8',fg="black",cursor="hand2")
link4.place(x=50,y=560)
link4.bind("<Button-1>",lambda d:callback("https://www.blockchair.com"))

link1=Label(app,text="check market sentiment? click here",font=('Helveticabold', 10, 'bold'),
                             bg='#49A2D8',fg="black",cursor="hand2")
link1.place(x=50,y=580)
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
              bg="#49A2D8",fg="black",command=log_in_page).place(x=1050,y=680)le.winfo_children():
        if int(widget.grid_info()["row"]) == row+1:   # "+1" because header row is not included in portfolio_data.
            widget.destroy()

# Recalculate total value of portfolio
show_portfolio()



#Start Tkinter event loop
app.mainloop()

#Close MySQL connection
mydb.close()








    
    
    
