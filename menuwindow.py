from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime
import requests


# Create the Tkinter window
window =Tk()
window.title("menu page")
window .geometry("1366x768")
window .resizable(0,0)
bg1 =PhotoImage(file="menu pic.png")
bgpic=Label(window ,image=bg1)
bgpic.place(x=0,y=0)

def notify():
    window.destroy()
    import telegramtrack
    
    
def portfolio():
    window.destroy()
    import project
    
notification_button=Button(window,text="PRICE TRACKING", 
                           font=("Helvetica", 13, "bold"),bg="#04012C",fg="white",command=notify)
notification_button.place(x=100,y=250)

portfolio_button=Button(window,text="PORTFOLIO TRACKING", 
                        font=("Helvetica", 13, "bold"),bg="#04012C",fg="white",command=portfolio)
portfolio_button.place(x=100,y=320)

 
    
    
Title = Label(window, 
              text="Click Your Way to Success with Our Game-Changing Service!",
              font=("Helvetica", 18, "bold"), bg='#04012C',fg="#B50B3A")
Title.place(x=20,y=150)  


def info():
    api_link="https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,INR"
    req=requests.get(api_link)
    dic=req.json()

    usd_value=float(dic["USD"])
    usd_formatted_value="${:,.3f}".format(usd_value)
    usd_l["text"]=usd_formatted_value

    inr_value=float(dic["INR"])
    inr_formatted_value="{:,.3f}".format(inr_value)
    inr_l["text"]="₹"+inr_formatted_value
    
#-----------------------------------------ETH----------------------------------------------------
    e_api_link="https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD,INR"
    e_req=requests.get(e_api_link)
    e_dic=e_req.json()

    e_usd_value=float(e_dic["USD"])
    e_usd_formatted_value="${:,.3f}".format(e_usd_value)
    e_usd_l["text"]=e_usd_formatted_value

    e_inr_value=float(e_dic["INR"])
    e_inr_formatted_value="{:,.3f}".format(e_inr_value)
    e_inr_l["text"]="₹"+e_inr_formatted_value
#-----------------------------------------ADA----------------------------------------------------

    a_api_link="https://min-api.cryptocompare.com/data/price?fsym=ADA&tsyms=USD,INR"
    a_req=requests.get(a_api_link)
    a_dic=a_req.json()

    a_usd_value=float(a_dic["USD"])
    a_usd_formatted_value="${:,.3f}".format(a_usd_value)
    a_usd_l["text"]=a_usd_formatted_value

    a_inr_value=float(a_dic["INR"])
    a_inr_formatted_value="{:,.3f}".format(a_inr_value)
    a_inr_l["text"]="₹"+a_inr_formatted_value

#-----------------------------------------DOT----------------------------------------------------
    d_api_link="https://min-api.cryptocompare.com/data/price?fsym=DOT&tsyms=USD,INR"
    d_req=requests.get(d_api_link)
    d_dic=d_req.json()

    d_usd_value=float(d_dic["USD"])
    d_usd_formatted_value="${:,.3f}".format(d_usd_value)
    d_usd_l["text"]=d_usd_formatted_value

    d_inr_value=float(d_dic["INR"])
    d_inr_formatted_value="{:,.3f}".format(d_inr_value)
    d_inr_l["text"]="₹"+d_inr_formatted_value

#-----------------------------------------BNB----------------------------------------------------
    b_api_link="https://min-api.cryptocompare.com/data/price?fsym=BNB&tsyms=USD,INR"
    b_req=requests.get(b_api_link)
    b_dic=b_req.json()

    b_usd_value=float(b_dic["USD"])
    b_usd_formatted_value="${:,.3f}".format(b_usd_value)
    b_usd_l["text"]=b_usd_formatted_value

    b_inr_value=float(b_dic["INR"])
    b_inr_formatted_value="{:,.3f}".format(b_inr_value)
    b_inr_l["text"]="₹"+b_inr_formatted_value

#-----------------------------------------SOL----------------------------------------------------
    s_api_link="https://min-api.cryptocompare.com/data/price?fsym=SOL&tsyms=USD,INR"
    s_req=requests.get(s_api_link)
    s_dic=s_req.json()

    s_usd_value=float(s_dic["USD"])
    s_usd_formatted_value="${:,.3f}".format(s_usd_value)
    s_usd_l["text"]=s_usd_formatted_value

    s_inr_value=float(s_dic["INR"])
    s_inr_formatted_value="{:,.3f}".format(s_inr_value)
    s_inr_l["text"]="₹"+s_inr_formatted_value

    time=datetime.now().strftime("%H:%M:%S")
    time_l.config(text="Updated at : "+time)
    frame.after(500,info)





frame=Frame(window,width=450,height=550,bg='#04012C')
frame.place(x=750,y=140)

#---------------------------------------BTC-------------------------------------------------

btc_l=Label(frame,text='BTC',bg='#499ab3',font=('Microsoft YaHei UI Light',15,
                                                                  'bold'),fg='#04012C')
btc_l.place(x=10,y=0)

usd_l=Label(frame,text='$000',bg='#04012C',font=('Microsoft YaHei UI Light',15,
                                                                  'bold'),fg='#70278b')
usd_l.place(x=150,y=0)

btc_i=Label(frame,text='Indian price:',bg='#04012C',font=('Microsoft YaHei UI Light',15,
                                                                  'bold'),fg='#499ab3')
btc_i.place(x=10,y=50)

inr_l=Label(frame,text='$000',bg='#04012C',font=('Microsoft YaHei UI Light',15,
                                                                  'bold'),fg='#980f62')
inr_l.place(x=150,y=50)

#---------------------------------------ETH-------------------------------------------------

eth_l=Label(frame,text='ETH',bg='#499ab3',font=('Microsoft YaHei UI Light',15,
                                                                  'bold'),fg='#04012C')
eth_l.place(x=10,y=100)

e_usd_l=Label(frame,text='$000',bg='#04012C',font=('Microsoft YaHei UI Light',15,
                                                                  'bold'),fg='#70278b')
e_usd_l.place(x=150,y=100)

eth_i=Label(frame,text='Indian price:',bg='#04012C',font=('Microsoft YaHei UI Light',15,
                                                                  'bold'),fg='#499ab3')
eth_i.place(x=10,y=150)

e_inr_l=Label(frame,text='$000',bg='#04012C',font=('Microsoft YaHei UI Light',15,
                                                                  'bold'),fg='#980f62')
e_inr_l.place(x=150,y=150)

#---------------------------------------ADA-------------------------------------------------

ada_l=Label(frame,text='ADA',bg='#499ab3',font=('Microsoft YaHei UI Light',15,
                                                                  'bold'),fg='#04012C')
ada_l.place(x=10,y=200)

a_usd_l=Label(frame,text='$000',bg='#04012C',font=('Microsoft YaHei UI Light',15,
                                                                  'bold'),fg='#70278b')
a_usd_l.place(x=150,y=200)

ada_i=Label(frame,text='Indian price:',bg='#04012C',font=('Microsoft YaHei UI Light',15,
                                                                  'bold'),fg='#499ab3')
ada_i.place(x=10,y=250)

a_inr_l=Label(frame,text='$000',bg='#04012C',font=('Microsoft YaHei UI Light',15,
                                                                  'bold'),fg='#980f62')
a_inr_l.place(x=150,y=250)

#---------------------------------------DOT-------------------------------------------------

dot_l=Label(frame,text='DOT',bg='#499ab3',font=('Microsoft YaHei UI Light',15,
                                                                  'bold'),fg='#04012C')
dot_l.place(x=10,y=300)

d_usd_l=Label(frame,text='$000',bg='#04012C',font=('Microsoft YaHei UI Light',15,
                                                                  'bold'),fg='#70278b')
d_usd_l.place(x=150,y=300)

dot_i=Label(frame,text='Indian price:',bg='#04012C',font=('Microsoft YaHei UI Light',15,
                                                                  'bold'),fg='#499ab3')
dot_i.place(x=10,y=350)

d_inr_l=Label(frame,text='$000',bg='#04012C',font=('Microsoft YaHei UI Light',15,
                                                                  'bold'),fg='#980f62')
d_inr_l.place(x=150,y=350)

#---------------------------------------BNB-------------------------------------------------

bnb_l=Label(frame,text='BNB',bg='#499ab3',font=('Microsoft YaHei UI Light',15,
                                                                  'bold'),fg='#04012C')
bnb_l.place(x=10,y=400)

b_usd_l=Label(frame,text='$000',bg='#04012C',font=('Microsoft YaHei UI Light',15,
                                                                  'bold'),fg='#70278b')
b_usd_l.place(x=150,y=400)

bnb_i=Label(frame,text='Indian price:',bg='#04012C',font=('Microsoft YaHei UI Light',15,
                                                                  'bold'),fg='#499ab3')
bnb_i.place(x=10,y=450)

b_inr_l=Label(frame,text='$000',bg='#04012C',font=('Microsoft YaHei UI Light',15,
                                                                  'bold'),fg='#980f62')
b_inr_l.place(x=150,y=450)

#---------------------------------------SOL-------------------------------------------------

sol_l=Label(frame,text='SOL',bg='#499ab3',font=('Microsoft YaHei UI Light',15,
                                                                  'bold'),fg='#04012C')
sol_l.place(x=10,y=500)

s_usd_l=Label(frame,text='$000',bg='#04012C',font=('Microsoft YaHei UI Light',15,
                                                                  'bold'),fg='#70278b')
s_usd_l.place(x=150,y=500)

sol_i=Label(frame,text='Indian price:',bg='#04012C',font=('Microsoft YaHei UI Light',15,
                                                                  'bold'),fg='#499ab3')
sol_i.place(x=10,y=550)

s_inr_l=Label(frame,text='$000',bg='#04012C',font=('Microsoft YaHei UI Light',15,
                                                                  'bold'),fg='#980f62')
s_inr_l.place(x=150,y=550)






time_l=Label(window,text='time',bg='#04012C',font=('Microsoft YaHei UI Light',12,
                                                                  'bold'),fg='white')
time_l.place(x=900,y=100)




info()



window.mainloop()