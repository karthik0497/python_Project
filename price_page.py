from tkinter import*
from tkinter import ttk
import requests
from datetime import datetime

def portfolio_page():
    suru.destroy()
    import portfolio_page

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



suru=Tk()
h=suru.winfo_screenheight()
w=suru.winfo_screenwidth()
suru.configure(height=h,width=w,bg='#010100')
suru.title('Crypto price page')
suru.iconbitmap('favicon bit.ico')


pic1=PhotoImage(file='e crypto.png')
bg_pic1=Label(suru,image=pic1,bd=0)
bg_pic1.place(x=720,y=200)

crypto_heading =Label(suru, text='Cryptocurrency Market',bg='#010100',
                    font=('Microsoft YaHei UI Light',30,'bold'),fg='#499ab3')
crypto_heading.place(x=450,y=30)

frame=Frame(suru,width=450,height=550,bg='#010100')
frame.place(x=200,y=140)

#---------------------------------------BTC-------------------------------------------------

btc_l=Label(frame,text='BTC',bg='#499ab3',font=('Microsoft YaHei UI Light',15,
                                                                  'bold'),fg='#010100')
btc_l.place(x=10,y=0)

usd_l=Label(frame,text='$000',bg='#010100',font=('Microsoft YaHei UI Light',15,
                                                                  'bold'),fg='#70278b')
usd_l.place(x=150,y=0)

btc_i=Label(frame,text='Indian price:',bg='#010100',font=('Microsoft YaHei UI Light',15,
                                                                  'bold'),fg='#499ab3')
btc_i.place(x=10,y=50)

inr_l=Label(frame,text='$000',bg='#010100',font=('Microsoft YaHei UI Light',15,
                                                                  'bold'),fg='#980f62')
inr_l.place(x=150,y=50)

#---------------------------------------ETH-------------------------------------------------

eth_l=Label(frame,text='ETH',bg='#499ab3',font=('Microsoft YaHei UI Light',15,
                                                                  'bold'),fg='#010100')
eth_l.place(x=10,y=100)

e_usd_l=Label(frame,text='$000',bg='#010100',font=('Microsoft YaHei UI Light',15,
                                                                  'bold'),fg='#70278b')
e_usd_l.place(x=150,y=100)

eth_i=Label(frame,text='Indian price:',bg='#010100',font=('Microsoft YaHei UI Light',15,
                                                                  'bold'),fg='#499ab3')
eth_i.place(x=10,y=150)

e_inr_l=Label(frame,text='$000',bg='#010100',font=('Microsoft YaHei UI Light',15,
                                                                  'bold'),fg='#980f62')
e_inr_l.place(x=150,y=150)

#---------------------------------------ADA-------------------------------------------------

ada_l=Label(frame,text='ADA',bg='#499ab3',font=('Microsoft YaHei UI Light',15,
                                                                  'bold'),fg='#010100')
ada_l.place(x=10,y=200)

a_usd_l=Label(frame,text='$000',bg='#010100',font=('Microsoft YaHei UI Light',15,
                                                                  'bold'),fg='#70278b')
a_usd_l.place(x=150,y=200)

ada_i=Label(frame,text='Indian price:',bg='#010100',font=('Microsoft YaHei UI Light',15,
                                                                  'bold'),fg='#499ab3')
ada_i.place(x=10,y=250)

a_inr_l=Label(frame,text='$000',bg='#010100',font=('Microsoft YaHei UI Light',15,
                                                                  'bold'),fg='#980f62')
a_inr_l.place(x=150,y=250)

#---------------------------------------DOT-------------------------------------------------

dot_l=Label(frame,text='DOT',bg='#499ab3',font=('Microsoft YaHei UI Light',15,
                                                                  'bold'),fg='#010100')
dot_l.place(x=10,y=300)

d_usd_l=Label(frame,text='$000',bg='#010100',font=('Microsoft YaHei UI Light',15,
                                                                  'bold'),fg='#70278b')
d_usd_l.place(x=150,y=300)

dot_i=Label(frame,text='Indian price:',bg='#010100',font=('Microsoft YaHei UI Light',15,
                                                                  'bold'),fg='#499ab3')
dot_i.place(x=10,y=350)

d_inr_l=Label(frame,text='$000',bg='#010100',font=('Microsoft YaHei UI Light',15,
                                                                  'bold'),fg='#980f62')
d_inr_l.place(x=150,y=350)

#---------------------------------------BNB-------------------------------------------------

bnb_l=Label(frame,text='BNB',bg='#499ab3',font=('Microsoft YaHei UI Light',15,
                                                                  'bold'),fg='#010100')
bnb_l.place(x=10,y=400)

b_usd_l=Label(frame,text='$000',bg='#010100',font=('Microsoft YaHei UI Light',15,
                                                                  'bold'),fg='#70278b')
b_usd_l.place(x=150,y=400)

bnb_i=Label(frame,text='Indian price:',bg='#010100',font=('Microsoft YaHei UI Light',15,
                                                                  'bold'),fg='#499ab3')
bnb_i.place(x=10,y=450)

b_inr_l=Label(frame,text='$000',bg='#010100',font=('Microsoft YaHei UI Light',15,
                                                                  'bold'),fg='#980f62')
b_inr_l.place(x=150,y=450)

#---------------------------------------SOL-------------------------------------------------

sol_l=Label(frame,text='SOL',bg='#499ab3',font=('Microsoft YaHei UI Light',15,
                                                                  'bold'),fg='#010100')
sol_l.place(x=10,y=500)

s_usd_l=Label(frame,text='$000',bg='#010100',font=('Microsoft YaHei UI Light',15,
                                                                  'bold'),fg='#70278b')
s_usd_l.place(x=150,y=500)

sol_i=Label(frame,text='Indian price:',bg='#010100',font=('Microsoft YaHei UI Light',15,
                                                                  'bold'),fg='#499ab3')
sol_i.place(x=10,y=550)

s_inr_l=Label(frame,text='$000',bg='#010100',font=('Microsoft YaHei UI Light',15,
                                                                  'bold'),fg='#980f62')
s_inr_l.place(x=150,y=550)






time_l=Label(suru,text='time',bg='#010100',font=('Microsoft YaHei UI Light',12,
                                                                  'bold'),fg='white')
time_l.place(x=900,y=100)




info()


back_l=Label(suru,text='Track your Portfolio',bg='#010100',font=('Microsoft YaHei UI Light',12,
                                                                  'bold'),fg='#499ab3')
back_l.place(x=800,y=620)

back_button = Button(suru, text="Click here",bd=0,bg='black',
                     font=('Microsoft YaHei UI Light',12,'bold','underline'),activeforeground='#980f62',
                     fg='#980f62',activebackground='black',cursor='hand2',
                      command=portfolio_page)
back_button.place(x=975,y=617)

suru.mainloop()
