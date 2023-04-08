from tkinter import *
from tkinter import ttk
import requests
import json
from telegram import Bot
import asyncio
import webbrowser
from datetime import datetime

window=Tk()
window.geometry("1366x768")
window.title('telegran tracking')
bg1 =PhotoImage(file="telegrampic.png")
bgpic1=Label(window,image=bg1)
bgpic1.place(x=0,y=0)

# CoinMarketCap API endpoint
url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"

"""
 When making an HTTP request, including headers or parameters is essential for communicating with the server
So passing these headers and params is necessary to make proper API request which can 
 interact with the API server via Python code..
The response object returned from the GET request is then accessed using the .text attribute,
which contains the response body as a string in JSON format. 
The json.loads() method is then used to convert the JSON string into a Python dictionary object 
stored in the data variable.
"""

def get_crypto_data(crypto):
    headers = {'X-CMC_PRO_API_KEY': "5c0c6dea-e42d-4fef-83f3-07edcdc832e1"}
    parameters = {'symbol': crypto}
    
    response = requests.get(url, headers=headers, params=parameters)
    data = json.loads(response.text)  # the json module provides an easy way to encode and decode data in JSON format. 
                                      # The json.loads method is used to load data in JSON 
                                      # format from a string type data.deserializing the JSON string.

    # Extract relevant data from response
    crypto_name = data['data'][crypto]['name']
    crypto_price = data['data'][crypto]['quote']['USD']['price']
    crypto_percent_change_24h = data['data'][crypto]['quote']['USD']['percent_change_24h']
    crypto_volume_24h = data['data'][crypto]['quote']['USD']['volume_24h']

    return crypto_name, crypto_price, crypto_percent_change_24h, crypto_volume_24h

 #async coroutine send_message that takes in four arguments  

async def send_message(crypto_name, crypto_price, crypto_percent_change_24h, crypto_volume_24h):          
    message = f'{crypto_name}\nPrice: ${crypto_price}\nChange: {crypto_percent_change_24h}%\nVolume: ${crypto_volume_24h}'
    bot = Bot(token=bot_token)
    await bot.send_message(chat_id=chat_id, text=message)

"""The await keyword is used before calling bot.send_message() to ensure the 
code waits for the message to be sent before proceeding further in execution.
 Using asynchronous code in Tkinter allows for concurrent execution with other
 threads and that makes the program more responsive
 The await keyword is used here to ensure that the coroutine waits for the specified
 time interval before continuing with the loop."""

async def track_crypto(crypto_list):
    time_interval = int(time_entry.get())
    while True:
        for crypto in crypto_list:
            crypto_name, crypto_price, crypto_percent_change_24h, crypto_volume_24h = get_crypto_data(crypto)
            await send_message(crypto_name, crypto_price, crypto_percent_change_24h, crypto_volume_24h)
        await asyncio.sleep(time_interval) # it wait for the time interval to send message 
                                           # asyncio.sleep() function, which suspends the coroutine for the specified
                                           # amount of time. 
                                           # The await keyword is used here to ensure that the coroutine waits for 
                                           # the specifiedtime interval before continuing with the loop.




def start_tracking():
    global bot_token, chat_id              # becauesit will ask new bot id,token for every event loop ,so we use global
    bot_token = bot_token_entry.get()
    chat_id = chat_id_entry.get()
    
    # Split values using comma as delimiter
    input_string = crypto_entry.get().upper()
    crypto_list = input_string.split(",")
    asyncio.run(track_crypto(crypto_list))
    
    """
    The track_crypto() function runs indefinitely (until the program is manually stoppe), 
    periodically fetching the latest cryptocurrency data for each cryptocurrency in the crypto_list
    and sending a message to the user's Telegram chat using the send_message() function.
    The time interval between each data fetch is determined by the time_interval 
    """    
# Create the Tkinter window

window.title("Crypto Tracker")

label = Label(window,
              text="Ready to Ride the Crypto Bull? Let Our Telegram Bot Keep You Informed!",
              font=("Helvetica", 18, "bold"), bg='#FEB81C',fg="#FEFFFE")
label.place(x=10,y=40)
# Create the label and entry widgets

bot_token_label = Label(window, text="Enter your Telegram bot token:",font=('Arial',12,'bold'),bg="#FEB81C")
bot_token_label.place(x=50,y=100)
bot_token_entry = Entry(window)
bot_token_entry.place(x=50,y=150)

chat_id_label = Label(window, text="Enter your Telegram chat ID:",font=('Arial',12,'bold'),bg="#FEB81C")
chat_id_label.place(x=50,y=200)
chat_id_entry = Entry(window)
chat_id_entry.place(x=50,y=250)

crypto_label = Label(window, text="Enter crypto symbol:",font=('Arial',12,'bold'),bg="#FEB81C")
crypto_label.place(x=50,y=300)
crypto_entry = Entry(window)
crypto_entry.place(x=50,y=350)

time_label = Label(window, text="Select time interval (in seconds):",font=('Arial',12,'bold'),bg="#FEB81C")
time_label.place(x=50,y=400)
time_entry = Entry(window)
time_entry.place(x=50,y=450)    
    
    
# Create the button widget
button = Button(window, text="Start Tracking", command=start_tracking)
button.place(x=250,y=450)

def callback(url):
    webbrowser.open_new_tab(url)

link=Label(window,text="Get your telegram chat id using your bot token",font=('Helveticabold', 10, 'bold'),
                            fg='blue', bg='#FEB81C',cursor="hand2")
link.place(x=50,y=650)
link.bind("<Button-1>",lambda d:callback("https://ungineer.github.io/chatid.html"))

link1=Label(window,text="How to create telegram bot?",font=('Helveticabold', 10, 'bold'),
                            fg='blue', bg='#FEB81C',cursor="hand2")
link1.place(x=50,y=625)
link1.bind("<Button-1>",lambda d:callback("https://www.teleme.io/articles/create_your_own_telegram_bot?hl=en"))


def log_in_page():
    window.destroy()
    import loginpage
    
def portfoliotracking_page():
    window.destroy()
    import project
    
tracking_page_button=Button(window,text="portfolio tracking page",font=("Helvetica", 8, "bold underline"),bd=0,
                   activeforeground="blue",cursor="hand2",
              fg='blue', bg='#FEB81C',command=portfoliotracking_page).place(x=1100,y=650)

login_page_button=Button(window,text="Log out",font=("Helvetica", 8, "bold underline"),bd=0,
                   activeforeground="blue",cursor="hand2",
              fg='blue', bg='#FEB81C',command=log_in_page).place(x=1100,y=680)

window.mainloop()