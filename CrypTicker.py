# Python 2.7.6. WBN Calling exchange APIs.
import time, json, requests
import statistics
from Tkinter import *



#Variables
MyBTC = 10.78
MyBLK = 14361
MyLTC = 20.78844
MyDRK = 45
MyFAIR = 0

bitstampUSDexchangeURL = 'https://www.bitstamp.net/api/ticker/'
btceUSDexchangeURL = 'https://btc-e.com/api/2/btc_usd/ticker'
coinbaseUSDexchangeURL = 'https://coinbase.com/api/v1/prices/buy'
krakenUSDexchangeURL = 'https://api.kraken.com/0/public/Ticker'
bitfinexUSDexchangeURL = "https://api.bitfinex.com/v1/ticker/btcusd"
cryptsyUSDexchangeURL = 'http://pubapi.cryptsy.com/api.php?method=singlemarketdata&marketid=2'
BLKexchangeURL = 'http://pubapi.cryptsy.com/api.php?method=singlemarketdata&marketid=179'
LTCexchangeURL = 'http://pubapi.cryptsy.com/api.php?method=singlemarketdata&marketid=3'
DRKexchangeURL = 'http://pubapi.cryptsy.com/api.php?method=singlemarketdata&marketid=155'
FAIRexchangeURL = 'https://api.vaultex.io/v1/market/stats/FAIR/BTC'

exchangeNametext = " Exchange Name "
BTCexchangeNametext = " Price Average "
BLKexchangeNametext = " Cryptsy "
LTCexchangeNametext = " Cryptsy "
DRKexchangeNametext = " Cryptsy "
FAIRexchangeNametext = " Vaultex "

TextFontType = "Georgia"
DataFontType = "Comic Sans MS"
TextFontSize = 12
DataFontSize = 14

PriceAveragetext = str(" Price Average ")
bitstampUSDtext = str(" Bitstamp ")
btceUSDtext = str(" Btc-e ")
coinbaseUSDtext = str(" Coinbase ")
krakenUSDtext = str(" Kraken ")
bitfinexUSDtext = str(" Bitfinex ")
cryptsyUSDtext = str(" Cryptsy ")
MyBTCtext = " My BTC "
MyBLKtext = " My BLK "
MyLTCtext = " My LTC "
MyDRKtext = " My DRK "
MyFAIRtext = " My FAIR "
BLKpriceBTCtext = str(" BLK Price in BTC ")
BLKpriceUSDtext = str(" BLK Price in USD ")
LTCpriceBTCtext = str(" LTC Price in BTC ")
LTCpriceUSDtext = str(" LTC Price in USD ")
DRKpriceBTCtext = str(" DRK Price in BTC ")
DRKpriceUSDtext = str(" DRK Price in USD ")
FAIRpriceBTCtext = str(" FAIR Price in BTC ")
FAIRpriceUSDtext = str(" FAIR Price in USD ")
MyBTCValuetext = str(" My Bitcoins Value in USD ")
MyBLKValueUSDtext = str(" My BLK Value in USD ")
MyBLKValueBTCtext = str(" My BLK Value in BTC ")
MyLTCValueUSDtext = str(" My LTC Value in USD ")
MyLTCValueBTCtext = str(" My LTC Value in BTC ")
MyDRKValueUSDtext = str(" My DRK Value in USD ")
MyDRKValueBTCtext = str(" My DRK Value in BTC ")
MyFAIRValueUSDtext = str(" My FAIR Value in USD ")
MyFAIRValueBTCtext = str(" My FAIR Value in BTC ")
MyTotalValueUSDtext = str(" My Total Value in USD ")
MyTotalValueBTCtext = str(" My Total Value in BTC ")

UpdateIntervalSec = 12
UpdateInterval = UpdateIntervalSec * 1000
UpdateIntervalSectext = str(" Update Interval (s) ")





#BITCOIN
# Import and Update API DATA for Bitcoin
def bitstampUSD():
    bitstampUSDtick = requests.get(bitstampUSDexchangeURL)
    return bitstampUSDtick.json()['last']

def bitstampUSDupdate():
    global bitstampUSDvardata
    bitstampUSDvardata.set(str.format("{0:.2f}", (float(bitstampUSD()))))
    root.after(UpdateInterval, bitstampUSDupdate)


def btceUSD():
    btceUSDtick = requests.get(btceUSDexchangeURL)
    return btceUSDtick.json()['ticker']['last']

def btceUSDupdate():
    global btceUSDvardata
    btceUSDvardata.set(str.format("{0:.2f}", (float(btceUSD()))))
    root.after(UpdateInterval, btceUSDupdate)


def coinbaseUSD():
    coinbaseUSDTick = requests.get(coinbaseUSDexchangeURL)
    return coinbaseUSDTick.json()['amount']

def coinbaseUSDupdate():
    global coinbaseUSDvardata
    coinbaseUSDvardata.set(str.format("{0:.2f}", (float(coinbaseUSD()))))
    root.after(UpdateInterval, coinbaseUSDupdate)


def krakenUSD():
    krakenUSDTick = requests.post(krakenUSDexchangeURL,data=json.dumps({"pair":"XXBTZUSD"}),
        headers={"content-type":"application/json"})
    return krakenUSDTick.json()['result']['XXBTZUSD']['c'][0]

def krakenUSDupdate():
    global krakenUSDvardata
    krakenUSDvardata.set(str.format("{0:.2f}", (float(krakenUSD()))))
    root.after(UpdateInterval, krakenUSDupdate)


def bitfinexUSD():
    bitfinexUSDTick = requests.get(bitfinexUSDexchangeURL)
    return bitfinexUSDTick.json()['last_price']

def bitfinexUSDupdate():
    global bitfinexUSDvardata
    bitfinexUSDvardata.set(str.format("{0:.2f}", (float(bitfinexUSD()))))
    root.after(UpdateInterval, bitfinexUSDupdate)


def cryptsyUSD():
    cryptsyBTCTick = requests.get(cryptsyUSDexchangeURL)
    return cryptsyBTCTick.json()["return"]["markets"]["BTC"]['lasttradeprice']

def cryptsyUSDupdate():
    global cryptsyUSDvardata
    cryptsyUSDvardata.set(str.format("{0:.2f}", (float(cryptsyUSD()))))
    root.after(UpdateInterval, cryptsyUSDupdate)


def CalculatePriceAverage():
    global PriceAverageUSDvardatalist
    PriceAverageUSDvardatalist = [float(bitstampUSDvardata.get()), float(btceUSDvardata.get()), float(coinbaseUSDvardata.get()), float(krakenUSDvardata.get()), float(bitfinexUSDvardata.get()), float(cryptsyUSDvardata.get())]

    global PriceAverageUSDvardata
    PriceAverageUSDvardata.set(str.format("{0:.2f}", (statistics.mean(PriceAverageUSDvardatalist))))

    print PriceAverageUSDvardatalist
    print PriceAverageUSDvardata.get()
    root.after(UpdateInterval, CalculatePriceAverage)


# Calculate and Update my Bitcoin Value
def MyBTCValue():
    MyBTCValue = float(PriceAverageUSDvardata.get()) * MyBTC
    print MyBTCValue
    return MyBTCValue

def MyBTCValueupdate():
    global MyBTCValuevardata
    MyBTCValuevardata.set(str.format("{0:.2f}", (float(MyBTCValue()))))
    root.after(UpdateInterval, MyBTCValueupdate)


#BLACKCOIN
# Import and Update API DATA for Cryptsy - Blackcoin price in BTC
def BLKpriceBTC():
    Tick = requests.get(BLKexchangeURL)
    return Tick.json()["return"]["markets"]["BC"]['lasttradeprice']

def BLKpriceBTCupdate():
    global BLKpriceBTCvardata
    BLKpriceBTCvardata.set(str.format("{0:.8f}", (float(BLKpriceBTC()))))
    print BLKpriceBTCvardata.get()
    root.after(UpdateInterval, BLKpriceBTCupdate)


# Calculate and Update with Price Average DATA for Cryptsy - Blackcoin price in USD
def BLKpriceUSD():
    BLKpriceUSD = float(BLKpriceBTCvardata.get()) * float(PriceAverageUSDvardata.get())
    return BLKpriceUSD

def BLKpriceUSDupdate():
    global BLKpriceBTCvardata
    global BLKpriceUSDvardata
    BLKpriceUSDvardata.set(str.format("{0:.2f}", (float(BLKpriceUSD()))))
    print BLKpriceUSDvardata.get()
    root.after(UpdateInterval, BLKpriceUSDupdate)


# Calculate and Update my Blackcoin Value in USD
def MyBLKValueUSD():
    global BLKpriceBTCvardata
    global BLKpriceUSDvardata
    MyBLKValueUSD = float(BLKpriceUSDvardata.get()) * MyBLK
    return MyBLKValueUSD

def MyBLKValueUSDupdate():
    global MyBLKValueUSDvardata
    MyBLKValueUSDvardata.set(str.format("{0:.2f}", (float(MyBLKValueUSD()))))
    root.after(UpdateInterval, MyBLKValueUSDupdate)


# Calculate and Update my Blackcoin Value in BTC
def MyBLKValueBTC():
    MyBLKValueBTC = float(BLKpriceBTCvardata.get()) * MyBLK
    return MyBLKValueBTC

def MyBLKValueBTCupdate():
    global MyBLKValueBTCvardata
    MyBLKValueBTCvardata.set(str.format("{0:.8f}", (float(MyBLKValueBTC()))))
    root.after(UpdateInterval, MyBLKValueBTCupdate)



#LITECOIN
# Import and Update API DATA for Cryptsy - Litecoin price in BTC
def LTCpriceBTC():
    Tick = requests.get(LTCexchangeURL)
    return Tick.json()["return"]["markets"]["LTC"]['lasttradeprice']

def LTCpriceBTCupdate():
    global LTCpriceBTCvardata
    LTCpriceBTCvardata.set(str.format("{0:.8f}", (float(LTCpriceBTC()))))
    print LTCpriceBTCvardata.get()
    root.after(UpdateInterval, LTCpriceBTCupdate)


# Calculate and Update with Price Average DATA for Cryptsy - Litecoin price in USD
def LTCpriceUSD():
    LTCpriceUSD = float(LTCpriceBTCvardata.get()) * float(PriceAverageUSDvardata.get())
    return LTCpriceUSD

def LTCpriceUSDupdate():
    global LTCpriceBTCvardata
    global LTCpriceUSDvardata
    LTCpriceUSDvardata.set(str.format("{0:.2f}", (float(LTCpriceUSD()))))
    print LTCpriceUSDvardata.get()
    root.after(UpdateInterval, LTCpriceUSDupdate)


# Calculate and Update my Litecoin Value in USD
def MyLTCValueUSD():
    global LTCpriceBTCvardata
    global LTCpriceUSDvardata
    MyLTCValueUSD = float(LTCpriceUSDvardata.get()) * MyLTC
    return MyLTCValueUSD

def MyLTCValueUSDupdate():
    global MyLTCValueUSDvardata
    MyLTCValueUSDvardata.set(str.format("{0:.2f}", (float(MyLTCValueUSD()))))
    root.after(UpdateInterval, MyLTCValueUSDupdate)


# Calculate and Update my Litecoin Value in BTC
def MyLTCValueBTC():
    MyLTCValueBTC = float(LTCpriceBTCvardata.get()) * MyLTC
    return MyLTCValueBTC

def MyLTCValueBTCupdate():
    global MyLTCValueBTCvardata
    MyLTCValueBTCvardata.set(str.format("{0:.8f}", (float(MyLTCValueBTC()))))
    root.after(UpdateInterval, MyLTCValueBTCupdate)



#DARKCOIN
# Import and Update API DATA for Cryptsy - Darkcoin price in BTC
def DRKpriceBTC():
    Tick = requests.get(DRKexchangeURL)
    return Tick.json()["return"]["markets"]["DRK"]['lasttradeprice']

def DRKpriceBTCupdate():
    global DRKpriceBTCvardata
    DRKpriceBTCvardata.set(str.format("{0:.8f}", (float(DRKpriceBTC()))))
    print DRKpriceBTCvardata.get()
    root.after(UpdateInterval, DRKpriceBTCupdate)


# Calculate and Update with Price Average DATA for Cryptsy - Darkcoin price in USD
def DRKpriceUSD():
    DRKpriceUSD = float(DRKpriceBTCvardata.get()) * float(PriceAverageUSDvardata.get())
    return DRKpriceUSD

def DRKpriceUSDupdate():
    global DRKpriceBTCvardata
    global DRKpriceUSDvardata
    DRKpriceUSDvardata.set(str.format("{0:.2f}", (float(DRKpriceUSD()))))
    print DRKpriceUSDvardata.get()
    root.after(UpdateInterval, DRKpriceUSDupdate)


# Calculate and Update my Darkcoin Value in USD
def MyDRKValueUSD():
    global DRKpriceBTCvardata
    global DRKpriceUSDvardata
    MyDRKValueUSD = float(DRKpriceUSDvardata.get()) * MyDRK
    return MyDRKValueUSD

def MyDRKValueUSDupdate():
    global MyDRKValueUSDvardata
    MyDRKValueUSDvardata.set(str.format("{0:.2f}", (float(MyDRKValueUSD()))))
    root.after(UpdateInterval, MyDRKValueUSDupdate)


# Calculate and Update my Darkcoin Value in BTC
def MyDRKValueBTC():
    MyDRKValueBTC = float(DRKpriceBTCvardata.get()) * MyDRK
    return MyDRKValueBTC

def MyDRKValueBTCupdate():
    global MyDRKValueBTCvardata
    MyDRKValueBTCvardata.set(str.format("{0:.8f}", (float(MyDRKValueBTC()))))
    root.after(UpdateInterval, MyDRKValueBTCupdate)


#FAIRCOIN
# Import and Update API DATA for Cryptsy - Faircoin price in BTC
def FAIRpriceBTC():
    Tick = requests.get(FAIRexchangeURL)
    return 0 #float(Tick.json()["last_price"])

def FAIRpriceBTCupdate():
    global FAIRpriceBTCvardata
    FAIRpriceBTCvardata.set(str.format("{0:.8f}", (float(FAIRpriceBTC()))))
    print FAIRpriceBTCvardata.get()
    root.after(UpdateInterval, FAIRpriceBTCupdate)


# Calculate and Update with Price Average DATA for Cryptsy - Faircoin price in USD
def FAIRpriceUSD():
    FAIRpriceUSD = float(FAIRpriceBTCvardata.get()) * float(PriceAverageUSDvardata.get())
    return FAIRpriceUSD

def FAIRpriceUSDupdate():
    global FAIRpriceBTCvardata
    global FAIRpriceUSDvardata
    FAIRpriceUSDvardata.set(str.format("{0:.2f}", (float(FAIRpriceUSD()))))
    print FAIRpriceUSDvardata.get()
    root.after(UpdateInterval, FAIRpriceUSDupdate)


# Calculate and Update my Faircoin Value in USD
def MyFAIRValueUSD():
    global FAIRpriceBTCvardata
    global FAIRpriceUSDvardata
    MyFAIRValueUSD = float(FAIRpriceUSDvardata.get()) * MyFAIR
    return MyFAIRValueUSD

def MyFAIRValueUSDupdate():
    global MyFAIRValueUSDvardata
    MyFAIRValueUSDvardata.set(str.format("{0:.2f}", (float(MyFAIRValueUSD()))))
    root.after(UpdateInterval, MyFAIRValueUSDupdate)


# Calculate and Update my Faircoin Value in BTC
def MyFAIRValueBTC():
    MyFAIRValueBTC = float(FAIRpriceBTCvardata.get()) * MyFAIR
    return MyFAIRValueBTC

def MyFAIRValueBTCupdate():
    global MyFAIRValueBTCvardata
    MyFAIRValueBTCvardata.set(str.format("{0:.8f}", (float(MyFAIRValueBTC()))))
    root.after(UpdateInterval, MyFAIRValueBTCupdate)



#TOTAL
# Calculate and Update my Total Value in USD
def MyTotalValueUSD():
    MyTotalValueUSD = float(MyBTCValuevardata.get()) + float(MyBLKValueUSDvardata.get()) + float(MyLTCValueUSDvardata.get()) + float(MyDRKValueUSDvardata.get()) + float(MyFAIRValueUSDvardata.get())
    return MyTotalValueUSD

def MyTotalValueUSDupdate():
    global MyTotalValueUSDvardata
    MyTotalValueUSDvardata.set(str.format("{0:.2f}", (float(MyTotalValueUSD()))))
    root.after(UpdateInterval, MyTotalValueUSDupdate)


# Calculate and Update my Total Value in BTC
def MyTotalValueBTC():
    MyTotalValueBTC = MyBTC + float(MyBLKValueBTCvardata.get()) + float(MyLTCValueBTCvardata.get()) + float(MyDRKValueBTCvardata.get()) + float(MyFAIRValueBTCvardata.get())
    return MyTotalValueBTC

def MyTotalValueBTCupdate():
    global MyTotalValueBTCvardata
    MyTotalValueBTCvardata.set(str.format("{0:.8}", (float(MyTotalValueBTC()))))
    root.after(UpdateInterval, MyTotalValueBTCupdate)



# Window Start
class Window(Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("Crypto")
        self.pack(fill=BOTH, expand=1)
        # Quit Button
        quitButton = Button(self, text="Quit", command=self.client_exit)
        quitButton.grid(row=0, column=0)
        #
        menu = Menu(self.master)
        self.master.config(menu=menu)
        file = Menu(menu)
        file.add_command(label="Exit", command=self.client_exit)
        menu.add_cascade(label="File", menu=file)
        edit = Menu(menu)
        #edit.add_command(label="Show Image", command=self.showImg)
        edit.add_command(label="Print DATA", command=self.showTxt)
        menu.add_cascade(label="Edit", menu=edit)


    #def showImg(self):
    #    load = Image.open("./images/blackcoin_500_small.gif")
    #    render = ImageTk.PhotoImage(load)
    #    img = Label(self, image=render)
    #    img.image = render
    #    img.place(x=2, y=1)


    def showTxt(self):
        PriceAverageUSDvardataFixed = float(PriceAverageUSDvardata.get())
        text = Label(self, text=PriceAverageUSDvardataFixed)
        text2 = Label(self, text=PriceAverageUSDvardatalist)
        text.grid(column=0)
        text2.grid(column=0)


    def client_exit(self):
        exit()


# Window Loop Start
root = Tk()
#root.geometry("1400x600")
app = Window(root)
root.title("CryptTicker")
root.config (bg = "red")

#Coin Images
BTCimage = Text(app, height=3.1, width=6)
BitcoinImage = PhotoImage(file='./images/BitcoinImage.gif')
BTCimage.image_create(END, image=BitcoinImage)
BTCimage.grid(row=1, column=2, rowspan=2)

BLKimage = Text(app, height=3.1, width=6)
BlackcoinImage = PhotoImage(file='./images/BlackcoinImage.gif')
BLKimage.image_create(END, image=BlackcoinImage)
BLKimage.grid(row=3, column=2, rowspan=2)

LTCimage = Text(app, height=3.1, width=6)
LitecoinImage = PhotoImage(file='./images/LitecoinImage.gif')
LTCimage.image_create(END, image=LitecoinImage)
LTCimage.grid(row=5, column=2, rowspan=2)

DRKimage = Text(app, height=3.1, width=6)
DarkcoinImage = PhotoImage(file='./images/DarkcoinImage.gif')
DRKimage.image_create(END, image=DarkcoinImage)
DRKimage.grid(row=7, column=2, rowspan=2)

FAIRimage = Text(app, height=3.1, width=6)
FaircoinImage = PhotoImage(file='./images/FaircoinImage.gif')
FAIRimage.image_create(END, image=FaircoinImage)
FAIRimage.grid(row=9, column=2, rowspan=2)


#root = Tk.Tk()
#root.config (bg = "red")
#label = Tk.Label(root, text = "test")
#label.configure(background = "#50A42D")
#label.pack()


# Data and Text Labels
'''
text2 = Text(root, height=30, width=60)
scroll = Scrollbar(root, command=text2.yview)
text2.configure(yscrollcommand=scroll.set)
scroll.pack(side=RIGHT, fill=Y)
'''



#Update Interval Rate Entry with Button
UpdateIntervalSecvartext = StringVar()
UpdateIntervalSeclabeltext = Label(app, textvariable=UpdateIntervalSecvartext, relief=FLAT, font=(TextFontType, TextFontSize))
UpdateIntervalSecvartext.set(UpdateIntervalSectext)
UpdateIntervalSeclabeltext.grid(row=1, column=0)

UpdateIntervalSecEntry = Entry(app)
UpdateIntervalSecEntry.grid(row=2, column=0)
UpdateIntervalSecEntry.focus_set()


def callback():
    global UpdateIntervalSec
    global UpdateInterval
    UpdateIntervalSec = int(UpdateIntervalSecEntry.get())
    print UpdateIntervalSecEntry.get()
    UpdateIntervalSecvardata = StringVar()
    UpdateIntervalSeclabeldata = Label(app, textvariable=UpdateIntervalSecvardata, relief=FLAT, font=(TextFontType, TextFontSize))
    UpdateIntervalSecvardata.set(UpdateIntervalSec)
    UpdateIntervalSeclabeldata.grid(row=4, column=0)
    UpdateInterval = UpdateIntervalSec * 1000
    return UpdateIntervalSec

b = Button(app, text="Update", width=10, command=callback).grid(row=3, column=0)

#UpdateIntervalSecvardata = StringVar()
UpdateIntervalSeclabeldata = Label(app, text=UpdateIntervalSec, relief=FLAT, font=(TextFontType, TextFontSize))
#UpdateIntervalSecvardata.set(UpdateIntervalSec.get())
UpdateIntervalSeclabeldata.grid(row=4, column=0)



#Exchange Name
exchangeNamevartext = StringVar()
exchangeNamelabeltext = Label(app, textvariable=exchangeNamevartext, relief=FLAT, font=(TextFontType, TextFontSize))
exchangeNamevartext.set(exchangeNametext)
exchangeNamelabeltext.grid(row=0, column=13)

#Bitcoin Exchange Name
BTCexchangeNamevartext = StringVar()
BTCexchangeNamelabeltext = Label(app, textvariable=BTCexchangeNamevartext, relief=FLAT, font=(TextFontType, TextFontSize))
BTCexchangeNamevartext.set(BTCexchangeNametext)
BTCexchangeNamelabeltext.grid(row=2, column=13)

#Blackcoin Exchange Name
BLKexchangeNamevartext = StringVar()
BLKexchangeNamelabeltext = Label(app, textvariable=BLKexchangeNamevartext, relief=FLAT, font=(TextFontType, TextFontSize))
BLKexchangeNamevartext.set(BLKexchangeNametext)
BLKexchangeNamelabeltext.grid(row=4, column=13)

#Litecoin Exchange Name
LTCexchangeNamevartext = StringVar()
LTCexchangeNamelabeltext = Label(app, textvariable=LTCexchangeNamevartext, relief=FLAT, font=(TextFontType, TextFontSize))
LTCexchangeNamevartext.set(LTCexchangeNametext)
LTCexchangeNamelabeltext.grid(row=6, column=13)

#Darkcoin Exchange Name
DRKexchangeNamevartext = StringVar()
DRKexchangeNamelabeltext = Label(app, textvariable=DRKexchangeNamevartext, relief=FLAT, font=(TextFontType, TextFontSize))
DRKexchangeNamevartext.set(DRKexchangeNametext)
DRKexchangeNamelabeltext.grid(row=8, column=13)

#Faircoin Exchange Name
FAIRexchangeNamevartext = StringVar()
FAIRexchangeNamelabeltext = Label(app, textvariable=FAIRexchangeNamevartext, relief=FLAT, font=(TextFontType, TextFontSize))
FAIRexchangeNamevartext.set(FAIRexchangeNametext)
FAIRexchangeNamelabeltext.grid(row=10, column=13)



#BITCOIN
# Display Data and Text for Bitcoin
bitstampUSDvartext = StringVar()
bitstampUSDlabeltext = Label(app, textvariable=bitstampUSDvartext, relief=FLAT, font=(TextFontType, TextFontSize))
bitstampUSDvartext.set(bitstampUSDtext)
bitstampUSDlabeltext.grid(row=3, column=1)
bitstampUSDvardata = StringVar()
bitstampUSDlabeldata = Label(app, textvariable=bitstampUSDvardata, relief=RAISED, font=(DataFontType, DataFontSize))
bitstampUSDupdate()
bitstampUSDlabeldata.grid(row=4, column=1)


btceUSDvartext = StringVar()
btceUSDlabeltext = Label(app, textvariable=btceUSDvartext, relief=FLAT, font=(TextFontType, TextFontSize))
btceUSDvartext.set(btceUSDtext)
btceUSDlabeltext.grid(row=5, column=1)
btceUSDvardata = StringVar()
btceUSDlabeldata = Label(app, textvariable=btceUSDvardata, relief=RAISED, font=(DataFontType, DataFontSize))
btceUSDupdate()
btceUSDlabeldata.grid(row=6, column=1)


coinbaseUSDvartext = StringVar()
coinbaseUSDlabeltext = Label(app, textvariable=coinbaseUSDvartext, relief=FLAT, font=(TextFontType, TextFontSize))
coinbaseUSDvartext.set(coinbaseUSDtext)
coinbaseUSDlabeltext.grid(row=7, column=1)
coinbaseUSDvardata = StringVar()
coinbaseUSDlabeldata = Label(app, textvariable=coinbaseUSDvardata, relief=RAISED, font=(DataFontType, DataFontSize))
coinbaseUSDupdate()
coinbaseUSDlabeldata.grid(row=8, column=1)

krakenUSDvartext = StringVar()
krakenUSDlabeltext = Label(app, textvariable=krakenUSDvartext, relief=FLAT, font=(TextFontType, TextFontSize))
krakenUSDvartext.set(krakenUSDtext)
krakenUSDlabeltext.grid(row=9, column=1)
krakenUSDvardata = StringVar()
krakenUSDlabeldata = Label(app, textvariable=krakenUSDvardata, relief=RAISED, font=(DataFontType, DataFontSize))
krakenUSDupdate()
krakenUSDlabeldata.grid(row=10, column=1)

bitfinexUSDvartext = StringVar()
bitfinexUSDlabeltext = Label(app, textvariable=bitfinexUSDvartext, relief=FLAT, font=(TextFontType, TextFontSize))
bitfinexUSDvartext.set(bitfinexUSDtext)
bitfinexUSDlabeltext.grid(row=11, column=1)
bitfinexUSDvardata = StringVar()
bitfinexUSDlabeldata = Label(app, textvariable=bitfinexUSDvardata, relief=RAISED, font=(DataFontType, DataFontSize))
bitfinexUSDupdate()
bitfinexUSDlabeldata.grid(row=12, column=1)

cryptsyUSDvartext = StringVar()
cryptsyUSDlabeltext = Label(app, textvariable=cryptsyUSDvartext, relief=FLAT, font=(TextFontType, TextFontSize))
cryptsyUSDvartext.set(cryptsyUSDtext)
cryptsyUSDlabeltext.grid(row=13, column=1)
cryptsyUSDvardata = StringVar()
cryptsyUSDlabeldata = Label(app, textvariable=cryptsyUSDvardata, relief=RAISED, font=(DataFontType, DataFontSize))
cryptsyUSDupdate()
cryptsyUSDlabeldata.grid(row=14, column=1)


PriceAverageUSDvartext = StringVar()
PriceAverageUSDlabeltext = Label(app, textvariable=PriceAverageUSDvartext, relief=FLAT, font=(TextFontType, TextFontSize))
PriceAverageUSDvartext.set(PriceAveragetext)
PriceAverageUSDlabeltext.grid(row=1, column=1)

PriceAverageUSDvardata = StringVar()
CalculatePriceAverage()
PriceAverageUSDlabeldata = Label(app, textvariable=PriceAverageUSDvardata, relief=RAISED, font=(DataFontType, DataFontSize))
PriceAverageUSDlabeldata.grid(row=2, column=1)


#MyBTC
MyBTCvartext = StringVar()
MyBTClabeltext = Label(app, textvariable=MyBTCvartext, relief=FLAT, font=(TextFontType, TextFontSize))
MyBTCvartext.set(MyBTCtext)
MyBTClabeltext.grid(row=1, column=3)

#MyBTCentry
#MyBTCentry = Entry(app)
#def MyBTCentryModify():
#    global MyBTC
#    MyBTCentry.delete(0,Tk.END)


#MyBTCentry.grid(row=5, column=0)
#MyBTCentry.focus_set()
#MyBTC = MyBTCentry.get()
#MyBTC = 22
'''
def callback():
    UpdateIntervalSec = int(UpdateIntervalSecEntry.get())
    print UpdateIntervalSecEntry.get()
    UpdateIntervalSecvardata = StringVar()
    UpdateIntervalSeclabeldata = Label(app, textvariable=UpdateIntervalSecvardata, relief=FLAT, font=(TextFontType, TextFontSize))
    UpdateIntervalSecvardata.set(UpdateIntervalSec)
    UpdateIntervalSeclabeldata.grid(row=4, column=0)
    UpdateInterval = UpdateIntervalSec * 1000
    return UpdateIntervalSec

b = Button(app, text="Update", width=10, command=callback).grid(row=3, column=0)
'''
#MyBTCvardata = StringVar()
MyBTClabeldata = Label(app, text=MyBTC, relief=RAISED, font=(DataFontType, DataFontSize))
MyBTClabeldata.grid(row=2, column=3)


#My BTC Value in USD
MyBTCValuevartext = StringVar()
MyBTCValuelabeltext = Label(app, textvariable=MyBTCValuevartext, relief=FLAT, font=(TextFontType, TextFontSize))
MyBTCValuevartext.set(MyBTCValuetext)
MyBTCValuelabeltext.grid(row=1, column=11)

MyBTCValuevardata = StringVar()
MyBTCValuelabeldata = Label(app, textvariable=MyBTCValuevardata, relief=RAISED, font=(DataFontType, DataFontSize))
MyBTCValueupdate()
MyBTCValuelabeldata.grid(row=2, column=11)


#BLACKCOIN
#MyBLK
MyBLKvartext = StringVar()
MyBLKlabeltext = Label(app, textvariable=MyBLKvartext, relief=FLAT, font=(TextFontType, TextFontSize))
MyBLKvartext.set(MyBLKtext)
MyBLKlabeltext.grid(row=3, column=3)
#MyBLKvardata = StringVar()
MyBLKlabeldata = Label(app, text=MyBLK, relief=RAISED, font=(DataFontType, DataFontSize))
MyBLKlabeldata.grid(row=4, column=3)


# Display Data and Text for Cryptsy - Blackcoin price in BTC
BLKpriceBTCvartext = StringVar()
BLKpriceBTClabeltext = Label(app, textvariable=BLKpriceBTCvartext, relief=FLAT, font=(TextFontType, TextFontSize))
BLKpriceBTCvartext.set(BLKpriceBTCtext)
BLKpriceBTClabeltext.grid(row=3, column=5)
BLKpriceBTCvardata = StringVar()
BLKpriceBTClabeldata = Label(app, textvariable=BLKpriceBTCvardata, relief=RAISED, font=(DataFontType, DataFontSize))
BLKpriceBTCupdate()
BLKpriceBTClabeldata.grid(row=4, column=5)


# Display Data and Text for Cryptsy - Blackcoin price in USD
BLKpriceUSDvartext = StringVar()
BLKpriceUSDlabeltext = Label(app, textvariable=BLKpriceUSDvartext, relief=FLAT, font=(TextFontType, TextFontSize))
BLKpriceUSDvartext.set(BLKpriceUSDtext)
BLKpriceUSDlabeltext.grid(row=3, column=7)
BLKpriceUSDvardata = StringVar()
BLKpriceUSDlabeldata = Label(app, textvariable=BLKpriceUSDvardata, relief=RAISED, font=(DataFontType, DataFontSize))
BLKpriceUSDupdate()
BLKpriceUSDlabeldata.grid(row=4, column=7)


#My BLK Value in USD
MyBLKValueUSDvartext = StringVar()
MyBLKValueUSDlabeltext = Label(app, textvariable=MyBLKValueUSDvartext, relief=FLAT, font=(TextFontType, TextFontSize))
MyBLKValueUSDvartext.set(MyBLKValueUSDtext)
MyBLKValueUSDlabeltext.grid(row=3, column=11)

MyBLKValueUSDvardata = StringVar()
MyBLKValueUSDlabeldata = Label(app, textvariable=MyBLKValueUSDvardata, relief=RAISED, font=(DataFontType, DataFontSize))
MyBLKValueUSDupdate()
MyBLKValueUSDlabeldata.grid(row=4, column=11)


#My BLK Value in BTC
MyBLKValueBTCvartext = StringVar()
MyBLKValueBTClabeltext = Label(app, textvariable=MyBLKValueBTCvartext, relief=FLAT, font=(TextFontType, TextFontSize))
MyBLKValueBTCvartext.set(MyBLKValueBTCtext)
MyBLKValueBTClabeltext.grid(row=3, column=9)

MyBLKValueBTCvardata = StringVar()
MyBLKValueBTClabeldata = Label(app, textvariable=MyBLKValueBTCvardata, relief=RAISED, font=(DataFontType, DataFontSize))
MyBLKValueBTCupdate()
MyBLKValueBTClabeldata.grid(row=4, column=9)



#LITECOIN
#MyLTC
MyLTCvartext = StringVar()
MyLTClabeltext = Label(app, textvariable=MyLTCvartext, relief=FLAT, font=(TextFontType, TextFontSize))
MyLTCvartext.set(MyLTCtext)
MyLTClabeltext.grid(row=5, column=3)
#MyLTCvardata = StringVar()
MyLTClabeldata = Label(app, text=MyLTC, relief=RAISED, font=(DataFontType, DataFontSize))
MyLTClabeldata.grid(row=6, column=3)


# Display Data and Text for Cryptsy - Litecoin price in BTC
LTCpriceBTCvartext = StringVar()
LTCpriceBTClabeltext = Label(app, textvariable=LTCpriceBTCvartext, relief=FLAT, font=(TextFontType, TextFontSize))
LTCpriceBTCvartext.set(LTCpriceBTCtext)
LTCpriceBTClabeltext.grid(row=5, column=5)
LTCpriceBTCvardata = StringVar()
LTCpriceBTClabeldata = Label(app, textvariable=LTCpriceBTCvardata, relief=RAISED, font=(DataFontType, DataFontSize))
LTCpriceBTCupdate()
LTCpriceBTClabeldata.grid(row=6, column=5)


# Display Data and Text for Cryptsy - Litecoin price in USD
LTCpriceUSDvartext = StringVar()
LTCpriceUSDlabeltext = Label(app, textvariable=LTCpriceUSDvartext, relief=FLAT, font=(TextFontType, TextFontSize))
LTCpriceUSDvartext.set(LTCpriceUSDtext)
LTCpriceUSDlabeltext.grid(row=5, column=7)
LTCpriceUSDvardata = StringVar()
LTCpriceUSDlabeldata = Label(app, textvariable=LTCpriceUSDvardata, relief=RAISED, font=(DataFontType, DataFontSize))
LTCpriceUSDupdate()
LTCpriceUSDlabeldata.grid(row=6, column=7)


#My LTC Value in USD
MyLTCValueUSDvartext = StringVar()
MyLTCValueUSDlabeltext = Label(app, textvariable=MyLTCValueUSDvartext, relief=FLAT, font=(TextFontType, TextFontSize))
MyLTCValueUSDvartext.set(MyLTCValueUSDtext)
MyLTCValueUSDlabeltext.grid(row=5, column=11)

MyLTCValueUSDvardata = StringVar()
MyLTCValueUSDlabeldata = Label(app, textvariable=MyLTCValueUSDvardata, relief=RAISED, font=(DataFontType, DataFontSize))
MyLTCValueUSDupdate()
MyLTCValueUSDlabeldata.grid(row=6, column=11)


#My LTC Value in BTC
MyLTCValueBTCvartext = StringVar()
MyLTCValueBTClabeltext = Label(app, textvariable=MyLTCValueBTCvartext, relief=FLAT, font=(TextFontType, TextFontSize))
MyLTCValueBTCvartext.set(MyLTCValueBTCtext)
MyLTCValueBTClabeltext.grid(row=5, column=9)

MyLTCValueBTCvardata = StringVar()
MyLTCValueBTClabeldata = Label(app, textvariable=MyLTCValueBTCvardata, relief=RAISED, font=(DataFontType, DataFontSize))
MyLTCValueBTCupdate()
MyLTCValueBTClabeldata.grid(row=6, column=9)



#DARKCOIN
#MyDRK
MyDRKvartext = StringVar()
MyDRKlabeltext = Label(app, textvariable=MyDRKvartext, relief=FLAT, font=(TextFontType, TextFontSize))
MyDRKvartext.set(MyDRKtext)
MyDRKlabeltext.grid(row=7, column=3)
#MyDRKvardata = StringVar()
MyDRKlabeldata = Label(app, text=MyDRK, relief=RAISED, font=(DataFontType, DataFontSize))
MyDRKlabeldata.grid(row=8, column=3)


# Display Data and Text for Cryptsy - Darkcoin price in BTC
DRKpriceBTCvartext = StringVar()
DRKpriceBTClabeltext = Label(app, textvariable=DRKpriceBTCvartext, relief=FLAT, font=(TextFontType, TextFontSize))
DRKpriceBTCvartext.set(DRKpriceBTCtext)
DRKpriceBTClabeltext.grid(row=7, column=5)
DRKpriceBTCvardata = StringVar()
DRKpriceBTClabeldata = Label(app, textvariable=DRKpriceBTCvardata, relief=RAISED, font=(DataFontType, DataFontSize))
DRKpriceBTCupdate()
DRKpriceBTClabeldata.grid(row=8, column=5)


# Display Data and Text for Cryptsy - Darkcoin price in USD
DRKpriceUSDvartext = StringVar()
DRKpriceUSDlabeltext = Label(app, textvariable=DRKpriceUSDvartext, relief=FLAT, font=(TextFontType, TextFontSize))
DRKpriceUSDvartext.set(DRKpriceUSDtext)
DRKpriceUSDlabeltext.grid(row=7, column=7)
DRKpriceUSDvardata = StringVar()
DRKpriceUSDlabeldata = Label(app, textvariable=DRKpriceUSDvardata, relief=RAISED, font=(DataFontType, DataFontSize))
DRKpriceUSDupdate()
DRKpriceUSDlabeldata.grid(row=8, column=7)


#My DRK Value in USD
MyDRKValueUSDvartext = StringVar()
MyDRKValueUSDlabeltext = Label(app, textvariable=MyDRKValueUSDvartext, relief=FLAT, font=(TextFontType, TextFontSize))
MyDRKValueUSDvartext.set(MyDRKValueUSDtext)
MyDRKValueUSDlabeltext.grid(row=7, column=11)

MyDRKValueUSDvardata = StringVar()
MyDRKValueUSDlabeldata = Label(app, textvariable=MyDRKValueUSDvardata, relief=RAISED, font=(DataFontType, DataFontSize))
MyDRKValueUSDupdate()
MyDRKValueUSDlabeldata.grid(row=8, column=11)


#My DRK Value in BTC
MyDRKValueBTCvartext = StringVar()
MyDRKValueBTClabeltext = Label(app, textvariable=MyDRKValueBTCvartext, relief=FLAT, font=(TextFontType, TextFontSize))
MyDRKValueBTCvartext.set(MyDRKValueBTCtext)
MyDRKValueBTClabeltext.grid(row=7, column=9)

MyDRKValueBTCvardata = StringVar()
MyDRKValueBTClabeldata = Label(app, textvariable=MyDRKValueBTCvardata, relief=RAISED, font=(DataFontType, DataFontSize))
MyDRKValueBTCupdate()
MyDRKValueBTClabeldata.grid(row=8, column=9)



#FAIRCOIN
#MyFAIR
MyFAIRvartext = StringVar()
MyFAIRlabeltext = Label(app, textvariable=MyFAIRvartext, relief=FLAT, font=(TextFontType, TextFontSize))
MyFAIRvartext.set(MyFAIRtext)
MyFAIRlabeltext.grid(row=9, column=3)
#MyFAIRvardata = StringVar()
MyFAIRlabeldata = Label(app, text=MyFAIR, relief=RAISED, font=(DataFontType, DataFontSize))
MyFAIRlabeldata.grid(row=10, column=3)


# Display Data and Text for Cryptsy - Faircoin price in BTC
FAIRpriceBTCvartext = StringVar()
FAIRpriceBTClabeltext = Label(app, textvariable=FAIRpriceBTCvartext, relief=FLAT, font=(TextFontType, TextFontSize))
FAIRpriceBTCvartext.set(FAIRpriceBTCtext)
FAIRpriceBTClabeltext.grid(row=9, column=5)
FAIRpriceBTCvardata = StringVar()
FAIRpriceBTClabeldata = Label(app, textvariable=FAIRpriceBTCvardata, relief=RAISED, font=(DataFontType, DataFontSize))
FAIRpriceBTCupdate()
FAIRpriceBTClabeldata.grid(row=10, column=5)


# Display Data and Text for Cryptsy - Faircoin price in USD
FAIRpriceUSDvartext = StringVar()
FAIRpriceUSDlabeltext = Label(app, textvariable=FAIRpriceUSDvartext, relief=FLAT, font=(TextFontType, TextFontSize))
FAIRpriceUSDvartext.set(FAIRpriceUSDtext)
FAIRpriceUSDlabeltext.grid(row=9, column=7)
FAIRpriceUSDvardata = StringVar()
FAIRpriceUSDlabeldata = Label(app, textvariable=FAIRpriceUSDvardata, relief=RAISED, font=(DataFontType, DataFontSize))
FAIRpriceUSDupdate()
FAIRpriceUSDlabeldata.grid(row=10, column=7)


#My FAIR Value in USD
MyFAIRValueUSDvartext = StringVar()
MyFAIRValueUSDlabeltext = Label(app, textvariable=MyFAIRValueUSDvartext, relief=FLAT, font=(TextFontType, TextFontSize))
MyFAIRValueUSDvartext.set(MyFAIRValueUSDtext)
MyFAIRValueUSDlabeltext.grid(row=9, column=11)

MyFAIRValueUSDvardata = StringVar()
MyFAIRValueUSDlabeldata = Label(app, textvariable=MyFAIRValueUSDvardata, relief=RAISED, font=(DataFontType, DataFontSize))
MyFAIRValueUSDupdate()
MyFAIRValueUSDlabeldata.grid(row=10, column=11)


#My FAIR Value in BTC
MyFAIRValueBTCvartext = StringVar()
MyFAIRValueBTClabeltext = Label(app, textvariable=MyFAIRValueBTCvartext, relief=FLAT, font=(TextFontType, TextFontSize))
MyFAIRValueBTCvartext.set(MyFAIRValueBTCtext)
MyFAIRValueBTClabeltext.grid(row=9, column=9)

MyFAIRValueBTCvardata = StringVar()
MyFAIRValueBTClabeldata = Label(app, textvariable=MyFAIRValueBTCvardata, relief=RAISED, font=(DataFontType, DataFontSize))
MyFAIRValueBTCupdate()
MyFAIRValueBTClabeldata.grid(row=10, column=9)




#TOTAL
#My Total Value in USD
MyTotalValueUSDvartext = StringVar()
MyTotalValueUSDlabeltext = Label(app, textvariable=MyTotalValueUSDvartext, relief=FLAT, font=(TextFontType, TextFontSize))
MyTotalValueUSDvartext.set(MyTotalValueUSDtext)
MyTotalValueUSDlabeltext.grid(row=100, column=11)

MyTotalValueUSDvardata = StringVar()
MyTotalValueUSDlabeldata = Label(app, textvariable=MyTotalValueUSDvardata, relief=RAISED, font=(DataFontType, DataFontSize))
MyTotalValueUSDupdate()
MyTotalValueUSDlabeldata.grid(row=101, column=11)


#My Total Value in BTC
MyTotalValueBTCvartext = StringVar()
MyTotalValueBTClabeltext = Label(app, textvariable=MyTotalValueBTCvartext, relief=FLAT, font=(TextFontType, TextFontSize))
MyTotalValueBTCvartext.set(MyTotalValueBTCtext)
MyTotalValueBTClabeltext.grid(row=100, column=9)

MyTotalValueBTCvardata = StringVar()
MyTotalValueBTClabeldata = Label(app, textvariable=MyTotalValueBTCvardata, relief=RAISED, font=(DataFontType, DataFontSize))
MyTotalValueBTCupdate()
MyTotalValueBTClabeldata.grid(row=101, column=9)



'''
EEE = Entry(app, bd =5,)
ShowEEE = Entry(app, show = EEE)
EEE.pack(side = RIGHT)
'''

root.mainloop()