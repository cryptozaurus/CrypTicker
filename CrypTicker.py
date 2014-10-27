# Python 2.7.6. WBN Calling exchange APIs.
import time, json, requests
import statistics
from Tkinter import *



#Variables
MyBTC = 10.78
MyBLK = 14361
MyLTC = 20.78844
MyDOGE = 113356
MyDRK = 45
MyPPC = 12.89
MyFAIR = 10

bitstampUSDexchangeURL = 'https://www.bitstamp.net/api/ticker/'
btceUSDexchangeURL = 'https://btc-e.com/api/2/btc_usd/ticker'
coinbaseUSDexchangeURL = 'https://coinbase.com/api/v1/prices/buy'
krakenUSDexchangeURL = 'https://api.kraken.com/0/public/Ticker'
bitfinexUSDexchangeURL = "https://api.bitfinex.com/v1/ticker/btcusd"
cryptsyUSDexchangeURL = 'http://pubapi.cryptsy.com/api.php?method=singlemarketdata&marketid=2'
BLKexchangeURL = 'http://pubapi.cryptsy.com/api.php?method=singlemarketdata&marketid=179'
LTCexchangeURL = 'http://pubapi.cryptsy.com/api.php?method=singlemarketdata&marketid=3'
DOGEexchangeURL = 'http://pubapi.cryptsy.com/api.php?method=singlemarketdata&marketid=132'
DRKexchangeURL = 'http://pubapi.cryptsy.com/api.php?method=singlemarketdata&marketid=155'
PPCexchangeURL = 'http://pubapi.cryptsy.com/api.php?method=singlemarketdata&marketid=28'
FAIRexchangeURL = 'https://api.vaultex.io/v1/market/stats/FAIR/BTC'

exchangeNametext = " Exchange Name "
BTCexchangeNametext = " Price Average "
BLKexchangeNametext = " Cryptsy "
LTCexchangeNametext = " Cryptsy "
DOGEexchangeNametext = " Cryptsy "
DRKexchangeNametext = " Cryptsy "
PPCexchangeNametext = " Cryptsy "
FAIRexchangeNametext = " Vaultex "

TextFontType = "Georgia"
DataFontType = "Comic Sans MS"
TextFontSize = 12
DataFontSize = 14

PriceAverageUSDtext = str(" Price Average ")
bitstampUSDtext = str(" Bitstamp ")
btceUSDtext = str(" Btc-e ")
coinbaseUSDtext = str(" Coinbase ")
krakenUSDtext = str(" Kraken ")
bitfinexUSDtext = str(" Bitfinex ")
cryptsyUSDtext = str(" Cryptsy ")
MyBTCtext = " My BTC "
MyBLKtext = " My BLK "
MyLTCtext = " My LTC "
MyDOGEtext = " My DOGE "
MyDRKtext = " My DRK "
MyPPCtext = " My PPC "
MyFAIRtext = " My FAIR "
BTCpriceUSDtext = str(" BTC Price in USD ")
BLKpriceBTCtext = str(" BLK Price in BTC ")
BLKpriceUSDtext = str(" BLK Price in USD ")
LTCpriceBTCtext = str(" LTC Price in BTC ")
LTCpriceUSDtext = str(" LTC Price in USD ")
DOGEpriceBTCtext = str(" DOGE Price in BTC ")
DOGEpriceUSDtext = str(" DOGE Price in USD ")
DRKpriceBTCtext = str(" DRK Price in BTC ")
DRKpriceUSDtext = str(" DRK Price in USD ")
PPCpriceBTCtext = str(" PPC Price in BTC ")
PPCpriceUSDtext = str(" PPC Price in USD ")
FAIRpriceBTCtext = str(" FAIR Price in BTC ")
FAIRpriceUSDtext = str(" FAIR Price in USD ")
MyBTCValuetext = str(" My Bitcoins Value in USD ")
MyBLKValueUSDtext = str(" My BLK Value in USD ")
MyBLKValueBTCtext = str(" My BLK Value in BTC ")
MyLTCValueUSDtext = str(" My LTC Value in USD ")
MyLTCValueBTCtext = str(" My LTC Value in BTC ")
MyDOGEValueUSDtext = str(" My DOGE Value in USD ")
MyDOGEValueBTCtext = str(" My DOGE Value in BTC ")
MyDRKValueUSDtext = str(" My DRK Value in USD ")
MyDRKValueBTCtext = str(" My DRK Value in BTC ")
MyPPCValueUSDtext = str(" My PPC Value in USD ")
MyPPCValueBTCtext = str(" My PPC Value in BTC ")
MyFAIRValueUSDtext = str(" My FAIR Value in USD ")
MyFAIRValueBTCtext = str(" My FAIR Value in BTC ")
MyTotalValueUSDtext = str(" My Total Value in USD ")
MyTotalValueBTCtext = str(" My Total Value in BTC ")

UpdateIntervalSec = 12
UpdateInterval = UpdateIntervalSec * 1000
UpdateIntervalSectext = str(" Update Interval (s) ")

exchangeNamerowtext = 0
BTCrowtext = 1
BTCrowdata = 2
BLKrowtext = 3
BLKrowdata = 4
LTCrowtext = 5
LTCrowdata = 6
DOGErowtext = 7
DOGErowdata = 8
DRKrowtext = 9
DRKrowdata = 10
PPCrowtext = 11
PPCrowdata = 12
FAIRrowtext = 13
FAIRrowdata = 14

BTCUSDcol = 0
updateMyCOINScol = 2
COINSimagecol = 3
MyCOINScol = 5
PriceBTCcol = 7
PriceUSDcol = 9
ValueBTCcol = 11
ValueUSDcol = 13
exchangeNamecol = 15







#BITCOIN
# Import and Update API DATA for Bitcoin
def bitstampUSD():
    try:
        bitstampUSDtick = requests.get(bitstampUSDexchangeURL)
        return bitstampUSDtick.json()['last']
    except Exception:
        print "Bitstamp API error"
        return 0

def bitstampUSDupdate():
    global bitstampUSDvardata
    bitstampUSDvardata.set(str.format("{0:.2f}", (float(bitstampUSD()))))
    root.after(UpdateInterval, bitstampUSDupdate)


def btceUSD():
    try:
        btceUSDtick = requests.get(btceUSDexchangeURL)
        return btceUSDtick.json()['ticker']['last']
    except Exception:
        print "Btc-e API error"
        return 0

def btceUSDupdate():
    global btceUSDvardata
    btceUSDvardata.set(str.format("{0:.2f}", (float(btceUSD()))))
    root.after(UpdateInterval, btceUSDupdate)


def coinbaseUSD():
    try:
        coinbaseUSDTick = requests.get(coinbaseUSDexchangeURL)
        return coinbaseUSDTick.json()['amount']
    except Exception:
        print "Coinbase API error"
        return 0

def coinbaseUSDupdate():
    global coinbaseUSDvardata
    coinbaseUSDvardata.set(str.format("{0:.2f}", (float(coinbaseUSD()))))
    root.after(UpdateInterval, coinbaseUSDupdate)


def krakenUSD():
    try:
        krakenUSDTick = requests.post(krakenUSDexchangeURL,data=json.dumps({"pair":"XXBTZUSD"}),headers={"content-type":"application/json"})
        return krakenUSDTick.json()['result']['XXBTZUSD']['c'][0]
    except Exception:
        print "Kraken API error"
        return 0


def krakenUSDupdate():
    global krakenUSDvardata
    krakenUSDvardata.set(str.format("{0:.2f}", (float(krakenUSD()))))
    root.after(UpdateInterval, krakenUSDupdate)


def bitfinexUSD():
    try:
        bitfinexUSDTick = requests.get(bitfinexUSDexchangeURL)
        return bitfinexUSDTick.json()['last_price']
    except Exception:
        print "Bitfinex API error"
        return 0

def bitfinexUSDupdate():
    global bitfinexUSDvardata
    bitfinexUSDvardata.set(str.format("{0:.2f}", (float(bitfinexUSD()))))
    root.after(UpdateInterval, bitfinexUSDupdate)


def cryptsyUSD():
    try:
        cryptsyBTCTick = requests.get(cryptsyUSDexchangeURL)
        return cryptsyBTCTick.json()["return"]["markets"]["BTC"]['lasttradeprice']
    except Exception:
        print "Cryptsy API error"
        return 0

def cryptsyUSDupdate():
    global cryptsyUSDvardata
    cryptsyUSDvardata.set(str.format("{0:.2f}", (float(cryptsyUSD()))))
    root.after(UpdateInterval, cryptsyUSDupdate)


def PriceAverageUSDupdate():
    global PriceAverageUSDvardatalist
    PriceAverageUSDvardatalist = [float(bitstampUSDvardata.get()), float(btceUSDvardata.get()), float(coinbaseUSDvardata.get()), float(krakenUSDvardata.get()), float(bitfinexUSDvardata.get()), float(cryptsyUSDvardata.get())]
    PriceAverageUSDvardatalist = [x for x in PriceAverageUSDvardatalist if x != 0]

    global PriceAverageUSDvardata
    PriceAverageUSDvardata.set(str.format("{0:.2f}", (statistics.mean(PriceAverageUSDvardatalist))))

    print PriceAverageUSDvardatalist
    print PriceAverageUSDvardata.get()
    root.after(UpdateInterval, PriceAverageUSDupdate)



# Calculate and Update my Bitcoin Value
def MyBTCValue():
    MyBTCValue = float(BTCpriceUSDvardata.get()) * float(MyBTCvardata.get())
    return MyBTCValue

def MyBTCValueupdate():
    global MyBTCValuevardata
    MyBTCValuevardata.set(str.format("{0:.2f}", (float(MyBTCValue()))))
    root.after(UpdateInterval, MyBTCValueupdate)


#BLACKCOIN
# Import and Update API DATA for Blackcoin price in BTC
def BLKpriceBTC():
    try:
        Tick = requests.get(BLKexchangeURL)
        return Tick.json()["return"]["markets"]["BC"]['lasttradeprice']
    except Exception:
        print "BLKpriceBTC API error"
        return 0

def BLKpriceBTCupdate():
    global BLKpriceBTCvardata
    BLKpriceBTCvardata.set(str.format("{0:.8f}", (float(BLKpriceBTC()))))
    root.after(UpdateInterval, BLKpriceBTCupdate)


# Calculate and Update with Price Average DATA for Blackcoin price in USD
def BLKpriceUSD():
    BLKpriceUSD = float(BLKpriceBTCvardata.get()) * float(PriceAverageUSDvardata.get())
    return BLKpriceUSD

def BLKpriceUSDupdate():
    global BLKpriceUSDvardata
    BLKpriceUSDvardata.set(str.format("{0:.8f}", (float(BLKpriceUSD()))))
    root.after(UpdateInterval, BLKpriceUSDupdate)


# Calculate and Update my Blackcoin Value in USD
def MyBLKValueUSD():
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
# Import and Update API DATA for Litecoin price in BTC
def LTCpriceBTC():
    try:
        Tick = requests.get(LTCexchangeURL)
        return Tick.json()["return"]["markets"]["LTC"]['lasttradeprice']
    except Exception:
        print "LTCpriceBTC API error"
        return 0

def LTCpriceBTCupdate():
    global LTCpriceBTCvardata
    LTCpriceBTCvardata.set(str.format("{0:.8f}", (float(LTCpriceBTC()))))
    root.after(UpdateInterval, LTCpriceBTCupdate)


# Calculate and Update with Price Average DATA for Litecoin price in USD
def LTCpriceUSD():
    LTCpriceUSD = float(LTCpriceBTCvardata.get()) * float(PriceAverageUSDvardata.get())
    return LTCpriceUSD

def LTCpriceUSDupdate():
    global LTCpriceUSDvardata
    LTCpriceUSDvardata.set(str.format("{0:.8f}", (float(LTCpriceUSD()))))
    root.after(UpdateInterval, LTCpriceUSDupdate)


# Calculate and Update my Litecoin Value in USD
def MyLTCValueUSD():
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



#DOGECOIN
# Import and Update API DATA for Dogecoin price in BTC
def DOGEpriceBTC():
    try:
        Tick = requests.get(DOGEexchangeURL)
        return Tick.json()["return"]["markets"]["DOGE"]['lasttradeprice']
    except Exception:
        print "DOGEpriceBTC API error"
        return 0

def DOGEpriceBTCupdate():
    global DOGEpriceBTCvardata
    DOGEpriceBTCvardata.set(str.format("{0:.8f}", (float(DOGEpriceBTC()))))
    root.after(UpdateInterval, DOGEpriceBTCupdate)


# Calculate and Update with Price Average DATA for Dogecoin price in USD
def DOGEpriceUSD():
    DOGEpriceUSD = float(DOGEpriceBTCvardata.get()) * float(PriceAverageUSDvardata.get())
    return DOGEpriceUSD

def DOGEpriceUSDupdate():
    global DOGEpriceUSDvardata
    DOGEpriceUSDvardata.set(str.format("{0:.8f}", (float(DOGEpriceUSD()))))
    root.after(UpdateInterval, DOGEpriceUSDupdate)


# Calculate and Update my Dogecoin Value in USD
def MyDOGEValueUSD():
    global DOGEpriceUSDvardata
    MyDOGEValueUSD = float(DOGEpriceUSDvardata.get()) * MyDOGE
    return MyDOGEValueUSD

def MyDOGEValueUSDupdate():
    global MyDOGEValueUSDvardata
    MyDOGEValueUSDvardata.set(str.format("{0:.2f}", (float(MyDOGEValueUSD()))))
    root.after(UpdateInterval, MyDOGEValueUSDupdate)


# Calculate and Update my Dogecoin Value in BTC
def MyDOGEValueBTC():
    MyDOGEValueBTC = float(DOGEpriceBTCvardata.get()) * MyDOGE
    return MyDOGEValueBTC

def MyDOGEValueBTCupdate():
    global MyDOGEValueBTCvardata
    MyDOGEValueBTCvardata.set(str.format("{0:.8f}", (float(MyDOGEValueBTC()))))
    root.after(UpdateInterval, MyDOGEValueBTCupdate)




#DARKCOIN
# Import and Update API DATA for Darkcoin price in BTC
def DRKpriceBTC():
    try:
        Tick = requests.get(DRKexchangeURL)
        return Tick.json()["return"]["markets"]["DRK"]['lasttradeprice']
    except Exception:
        print "DRKpriceBTC API error"
        return 0

def DRKpriceBTCupdate():
    global DRKpriceBTCvardata
    DRKpriceBTCvardata.set(str.format("{0:.8f}", (float(DRKpriceBTC()))))
    root.after(UpdateInterval, DRKpriceBTCupdate)


# Calculate and Update with Price Average DATA for Darkcoin price in USD
def DRKpriceUSD():
    DRKpriceUSD = float(DRKpriceBTCvardata.get()) * float(PriceAverageUSDvardata.get())
    return DRKpriceUSD

def DRKpriceUSDupdate():
    global DRKpriceUSDvardata
    DRKpriceUSDvardata.set(str.format("{0:.8f}", (float(DRKpriceUSD()))))
    root.after(UpdateInterval, DRKpriceUSDupdate)


# Calculate and Update my Darkcoin Value in USD
def MyDRKValueUSD():
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



#PEERCOIN
# Import and Update API DATA for Peercoin price in BTC
def PPCpriceBTC():
    try:
        Tick = requests.get(PPCexchangeURL)
        return Tick.json()["return"]["markets"]["PPC"]['lasttradeprice']
    except Exception:
        print "PPCpriceBTC API error"
        return 0

def PPCpriceBTCupdate():
    global PPCpriceBTCvardata
    PPCpriceBTCvardata.set(str.format("{0:.8f}", (float(PPCpriceBTC()))))
    root.after(UpdateInterval, PPCpriceBTCupdate)


# Calculate and Update with Price Average DATA for Peercoin price in USD
def PPCpriceUSD():
    PPCpriceUSD = float(PPCpriceBTCvardata.get()) * float(PriceAverageUSDvardata.get())
    return PPCpriceUSD

def PPCpriceUSDupdate():
    global PPCpriceUSDvardata
    PPCpriceUSDvardata.set(str.format("{0:.8f}", (float(PPCpriceUSD()))))
    root.after(UpdateInterval, PPCpriceUSDupdate)


# Calculate and Update my Peercoin Value in USD
def MyPPCValueUSD():
    global PPCpriceUSDvardata
    MyPPCValueUSD = float(PPCpriceUSDvardata.get()) * MyPPC
    return MyPPCValueUSD

def MyPPCValueUSDupdate():
    global MyPPCValueUSDvardata
    MyPPCValueUSDvardata.set(str.format("{0:.2f}", (float(MyPPCValueUSD()))))
    root.after(UpdateInterval, MyPPCValueUSDupdate)


# Calculate and Update my Peercoin Value in BTC
def MyPPCValueBTC():
    MyPPCValueBTC = float(PPCpriceBTCvardata.get()) * MyPPC
    return MyPPCValueBTC

def MyPPCValueBTCupdate():
    global MyPPCValueBTCvardata
    MyPPCValueBTCvardata.set(str.format("{0:.8f}", (float(MyPPCValueBTC()))))
    root.after(UpdateInterval, MyPPCValueBTCupdate)




#FAIRCOIN
# Import and Update API DATA for Faircoin price in BTC
def FAIRpriceBTC():
    try:
        Tick = requests.get(FAIRexchangeURL)
        return 0 #float(Tick.json()["last_price"])
    except Exception:
        print "FAIRpriceBTC API error"
        return 0

def FAIRpriceBTCupdate():
    global FAIRpriceBTCvardata
    FAIRpriceBTCvardata.set(str.format("{0:.8f}", (float(FAIRpriceBTC()))))
    root.after(UpdateInterval, FAIRpriceBTCupdate)


# Calculate and Update with Price Average DATA for Faircoin price in USD
def FAIRpriceUSD():
    FAIRpriceUSD = float(FAIRpriceBTCvardata.get()) * float(PriceAverageUSDvardata.get())
    return FAIRpriceUSD

def FAIRpriceUSDupdate():
    global FAIRpriceUSDvardata
    FAIRpriceUSDvardata.set(str.format("{0:.8f}", (float(FAIRpriceUSD()))))
    root.after(UpdateInterval, FAIRpriceUSDupdate)


# Calculate and Update my Faircoin Value in USD
def MyFAIRValueUSD():
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
    MyTotalValueUSD = float(MyBTCValuevardata.get()) + float(MyBLKValueUSDvardata.get()) + float(MyLTCValueUSDvardata.get()) + float(MyDOGEValueUSDvardata.get()) + float(MyDRKValueUSDvardata.get()) + float(MyPPCValueUSDvardata.get()) + float(MyFAIRValueUSDvardata.get())
    return MyTotalValueUSD

def MyTotalValueUSDupdate():
    global MyTotalValueUSDvardata
    MyTotalValueUSDvardata.set(str.format("{0:.2f}", (float(MyTotalValueUSD()))))
    root.after(UpdateInterval, MyTotalValueUSDupdate)


# Calculate and Update my Total Value in BTC
def MyTotalValueBTC():
    MyTotalValueBTC = MyBTC + float(MyBLKValueBTCvardata.get()) + float(MyLTCValueBTCvardata.get()) + float(MyDOGEValueBTCvardata.get()) + float(MyDRKValueBTCvardata.get()) + float(MyPPCValueBTCvardata.get()) + float(MyFAIRValueBTCvardata.get())
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
BTCimage.grid(row=1, column=COINSimagecol, rowspan=2)

BLKimage = Text(app, height=3.1, width=6)
BlackcoinImage = PhotoImage(file='./images/BlackcoinImage.gif')
BLKimage.image_create(END, image=BlackcoinImage)
BLKimage.grid(row=BLKrowtext, column=COINSimagecol, rowspan=2)

LTCimage = Text(app, height=3.1, width=6)
LitecoinImage = PhotoImage(file='./images/LitecoinImage.gif')
LTCimage.image_create(END, image=LitecoinImage)
LTCimage.grid(row=LTCrowtext, column=COINSimagecol, rowspan=2)

DOGEimage = Text(app, height=3.1, width=6)
DogecoinImage = PhotoImage(file='./images/DogecoinImage.gif')
DOGEimage.image_create(END, image=DogecoinImage)
DOGEimage.grid(row=DOGErowtext, column=COINSimagecol, rowspan=2)

DRKimage = Text(app, height=3.1, width=6)
DarkcoinImage = PhotoImage(file='./images/DarkcoinImage.gif')
DRKimage.image_create(END, image=DarkcoinImage)
DRKimage.grid(row=DRKrowtext, column=COINSimagecol, rowspan=2)

PPCimage = Text(app, height=3.1, width=6)
PeercoinImage = PhotoImage(file='./images/PeercoinImage.gif')
PPCimage.image_create(END, image=PeercoinImage)
PPCimage.grid(row=PPCrowtext, column=COINSimagecol, rowspan=2)

FAIRimage = Text(app, height=3.1, width=6)
FaircoinImage = PhotoImage(file='./images/FaircoinImage.gif')
FAIRimage.image_create(END, image=FaircoinImage)
FAIRimage.grid(row=FAIRrowtext, column=COINSimagecol, rowspan=2)


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
UpdateIntervalSeclabeltext.grid(row=100, column=exchangeNamecol)

UpdateIntervalSecEntry = Entry(app)
UpdateIntervalSecEntry.grid(row=101, column=exchangeNamecol)
UpdateIntervalSecEntry.focus_set()


def callback():
    global UpdateIntervalSec
    global UpdateInterval
    UpdateIntervalSec = int(UpdateIntervalSecEntry.get())
    print UpdateIntervalSecEntry.get()
    UpdateIntervalSecvardata = StringVar()
    UpdateIntervalSeclabeldata = Label(app, textvariable=UpdateIntervalSecvardata, relief=FLAT, font=(TextFontType, TextFontSize))
    UpdateIntervalSecvardata.set(UpdateIntervalSec)
    UpdateIntervalSeclabeldata.grid(row=103, column=exchangeNamecol)
    UpdateInterval = UpdateIntervalSec * 1000
    return UpdateIntervalSec

b = Button(app, text="Update", width=10, command=callback).grid(row=102, column=exchangeNamecol)

#UpdateIntervalSecvardata = StringVar()
UpdateIntervalSeclabeldata = Label(app, text=UpdateIntervalSec, relief=FLAT, font=(TextFontType, TextFontSize))
#UpdateIntervalSecvardata.set(UpdateIntervalSec.get())
UpdateIntervalSeclabeldata.grid(row=4, column=0)



#Exchange Name
exchangeNamevartext = StringVar()
exchangeNamelabeltext = Label(app, textvariable=exchangeNamevartext, relief=FLAT, font=(TextFontType, TextFontSize))
exchangeNamevartext.set(exchangeNametext)
exchangeNamelabeltext.grid(row=exchangeNamerowtext, column=exchangeNamecol)

#Bitcoin Exchange Name
BTCexchangeNamevartext = StringVar()
BTCexchangeNamelabeltext = Label(app, textvariable=BTCexchangeNamevartext, relief=FLAT, font=(TextFontType, TextFontSize))
BTCexchangeNamevartext.set(BTCexchangeNametext)
BTCexchangeNamelabeltext.grid(row=BTCrowdata, column=exchangeNamecol)

#Blackcoin Exchange Name
BLKexchangeNamevartext = StringVar()
BLKexchangeNamelabeltext = Label(app, textvariable=BLKexchangeNamevartext, relief=FLAT, font=(TextFontType, TextFontSize))
BLKexchangeNamevartext.set(BLKexchangeNametext)
BLKexchangeNamelabeltext.grid(row=BLKrowdata, column=exchangeNamecol)

#Litecoin Exchange Name
LTCexchangeNamevartext = StringVar()
LTCexchangeNamelabeltext = Label(app, textvariable=LTCexchangeNamevartext, relief=FLAT, font=(TextFontType, TextFontSize))
LTCexchangeNamevartext.set(LTCexchangeNametext)
LTCexchangeNamelabeltext.grid(row=LTCrowdata, column=exchangeNamecol)

#Dogecoin Exchange Name
DOGEexchangeNamevartext = StringVar()
DOGEexchangeNamelabeltext = Label(app, textvariable=DOGEexchangeNamevartext, relief=FLAT, font=(TextFontType, TextFontSize))
DOGEexchangeNamevartext.set(DOGEexchangeNametext)
DOGEexchangeNamelabeltext.grid(row=DOGErowdata, column=exchangeNamecol)

#Darkcoin Exchange Name
DRKexchangeNamevartext = StringVar()
DRKexchangeNamelabeltext = Label(app, textvariable=DRKexchangeNamevartext, relief=FLAT, font=(TextFontType, TextFontSize))
DRKexchangeNamevartext.set(DRKexchangeNametext)
DRKexchangeNamelabeltext.grid(row=DRKrowdata, column=exchangeNamecol)

#Peercoin Exchange Name
PPCexchangeNamevartext = StringVar()
PPCexchangeNamelabeltext = Label(app, textvariable=PPCexchangeNamevartext, relief=FLAT, font=(TextFontType, TextFontSize))
PPCexchangeNamevartext.set(PPCexchangeNametext)
PPCexchangeNamelabeltext.grid(row=PPCrowdata, column=exchangeNamecol)

#Faircoin Exchange Name
FAIRexchangeNamevartext = StringVar()
FAIRexchangeNamelabeltext = Label(app, textvariable=FAIRexchangeNamevartext, relief=FLAT, font=(TextFontType, TextFontSize))
FAIRexchangeNamevartext.set(FAIRexchangeNametext)
FAIRexchangeNamelabeltext.grid(row=FAIRrowdata, column=exchangeNamecol)



#BITCOIN
# Display Data and Text for Bitcoin in USD
bitstampUSDvartext = StringVar()
bitstampUSDlabeltext = Label(app, textvariable=bitstampUSDvartext, relief=FLAT, font=(TextFontType, TextFontSize))
bitstampUSDvartext.set(bitstampUSDtext)
bitstampUSDlabeltext.grid(row=3, column=BTCUSDcol)
bitstampUSDvardata = StringVar()
bitstampUSDlabeldata = Label(app, textvariable=bitstampUSDvardata, relief=RAISED, font=(DataFontType, DataFontSize))
bitstampUSDupdate()
bitstampUSDlabeldata.grid(row=4, column=BTCUSDcol)


btceUSDvartext = StringVar()
btceUSDlabeltext = Label(app, textvariable=btceUSDvartext, relief=FLAT, font=(TextFontType, TextFontSize))
btceUSDvartext.set(btceUSDtext)
btceUSDlabeltext.grid(row=5, column=BTCUSDcol)
btceUSDvardata = StringVar()
btceUSDlabeldata = Label(app, textvariable=btceUSDvardata, relief=RAISED, font=(DataFontType, DataFontSize))
btceUSDupdate()
btceUSDlabeldata.grid(row=6, column=BTCUSDcol)


coinbaseUSDvartext = StringVar()
coinbaseUSDlabeltext = Label(app, textvariable=coinbaseUSDvartext, relief=FLAT, font=(TextFontType, TextFontSize))
coinbaseUSDvartext.set(coinbaseUSDtext)
coinbaseUSDlabeltext.grid(row=7, column=BTCUSDcol)
coinbaseUSDvardata = StringVar()
coinbaseUSDlabeldata = Label(app, textvariable=coinbaseUSDvardata, relief=RAISED, font=(DataFontType, DataFontSize))
coinbaseUSDupdate()
coinbaseUSDlabeldata.grid(row=8, column=BTCUSDcol)

krakenUSDvartext = StringVar()
krakenUSDlabeltext = Label(app, textvariable=krakenUSDvartext, relief=FLAT, font=(TextFontType, TextFontSize))
krakenUSDvartext.set(krakenUSDtext)
krakenUSDlabeltext.grid(row=9, column=BTCUSDcol)
krakenUSDvardata = StringVar()
krakenUSDlabeldata = Label(app, textvariable=krakenUSDvardata, relief=RAISED, font=(DataFontType, DataFontSize))
krakenUSDupdate()
krakenUSDlabeldata.grid(row=10, column=BTCUSDcol)

bitfinexUSDvartext = StringVar()
bitfinexUSDlabeltext = Label(app, textvariable=bitfinexUSDvartext, relief=FLAT, font=(TextFontType, TextFontSize))
bitfinexUSDvartext.set(bitfinexUSDtext)
bitfinexUSDlabeltext.grid(row=11, column=BTCUSDcol)
bitfinexUSDvardata = StringVar()
bitfinexUSDlabeldata = Label(app, textvariable=bitfinexUSDvardata, relief=RAISED, font=(DataFontType, DataFontSize))
bitfinexUSDupdate()
bitfinexUSDlabeldata.grid(row=12, column=BTCUSDcol)

cryptsyUSDvartext = StringVar()
cryptsyUSDlabeltext = Label(app, textvariable=cryptsyUSDvartext, relief=FLAT, font=(TextFontType, TextFontSize))
cryptsyUSDvartext.set(cryptsyUSDtext)
cryptsyUSDlabeltext.grid(row=13, column=BTCUSDcol)
cryptsyUSDvardata = StringVar()
cryptsyUSDlabeldata = Label(app, textvariable=cryptsyUSDvardata, relief=RAISED, font=(DataFontType, DataFontSize))
cryptsyUSDupdate()
cryptsyUSDlabeldata.grid(row=14, column=BTCUSDcol)


PriceAverageUSDvartext = StringVar()
PriceAverageUSDlabeltext = Label(app, textvariable=PriceAverageUSDvartext, relief=FLAT, font=(TextFontType, TextFontSize))
PriceAverageUSDvartext.set(PriceAverageUSDtext)
PriceAverageUSDlabeltext.grid(row=1, column=BTCUSDcol)
PriceAverageUSDvardata = StringVar()
PriceAverageUSDupdate()
PriceAverageUSDlabeldata = Label(app, textvariable=PriceAverageUSDvardata, relief=RAISED, font=(DataFontType, DataFontSize))
PriceAverageUSDlabeldata.grid(row=2, column=BTCUSDcol)



#BITCOIN
#MyBTC
MyBTCvartext = StringVar()
MyBTClabeltext = Label(app, textvariable=MyBTCvartext, relief=FLAT, font=(TextFontType, TextFontSize))
MyBTCvartext.set(MyBTCtext)
MyBTClabeltext.grid(row=BTCrowtext, column=MyCOINScol)




def Calculer():
    global MyBTC
    MyBTC = float(MyBTCvardata.get())
    MyBTCValueupdate()
    print MyBTC
    return MyBTC

MyBTCvardata = StringVar()
MyBTCvardata.set(MyBTC)
MyBTCentry = Entry(app, textvariable=MyBTCvardata, relief=RAISED, font=(DataFontType, DataFontSize), width=9, borderwidth=3, justify=CENTER)

MyBTCentry.grid(row=BTCrowdata, column=MyCOINScol)



MyBTCupdatebutton = Button(app, text='Update NOW', command=Calculer).grid(row=0, column=MyCOINScol)



#MyBTCvardata = StringVar()
#MyBTClabeldata = Label(app, textvariable=MyBTCvardata, relief=RAISED, font=(DataFontType, DataFontSize))
#MyBTClabeldata.grid(row=BTCrowdata, column=MyCOINScol)



# Display Data and Text for Bitcoin price in USD
BTCpriceUSDvartext = StringVar()
BTCpriceUSDlabeltext = Label(app, textvariable=BTCpriceUSDvartext, relief=FLAT, font=(TextFontType, TextFontSize))
BTCpriceUSDvartext.set(BTCpriceUSDtext)
BTCpriceUSDlabeltext.grid(row=BTCrowtext, column=PriceUSDcol)
BTCpriceUSDvardata = PriceAverageUSDvardata
BTCpriceUSDlabeldata = Label(app, textvariable=BTCpriceUSDvardata, relief=RAISED, font=(DataFontType, DataFontSize))
BTCpriceUSDlabeldata.grid(row=BTCrowdata, column=PriceUSDcol)


#My BTC Value in USD
MyBTCValuevartext = StringVar()
MyBTCValuelabeltext = Label(app, textvariable=MyBTCValuevartext, relief=FLAT, font=(TextFontType, TextFontSize))
MyBTCValuevartext.set(MyBTCValuetext)
MyBTCValuelabeltext.grid(row=BTCrowtext, column=ValueUSDcol)

MyBTCValuevardata = StringVar()
MyBTCValuelabeldata = Label(app, textvariable=MyBTCValuevardata, relief=RAISED, font=(DataFontType, DataFontSize))
MyBTCValueupdate()
MyBTCValuelabeldata.grid(row=BTCrowdata, column=ValueUSDcol)



#BLACKCOIN
#MyBLK
MyBLKvartext = StringVar()
MyBLKlabeltext = Label(app, textvariable=MyBLKvartext, relief=FLAT, font=(TextFontType, TextFontSize))
MyBLKvartext.set(MyBLKtext)
MyBLKlabeltext.grid(row=BLKrowtext, column=MyCOINScol)
#MyBLKvardata = StringVar()
MyBLKlabeldata = Label(app, text=MyBLK, relief=RAISED, font=(DataFontType, DataFontSize))
MyBLKlabeldata.grid(row=BLKrowdata, column=MyCOINScol)


# Display Data and Text for Blackcoin price in BTC
BLKpriceBTCvartext = StringVar()
BLKpriceBTClabeltext = Label(app, textvariable=BLKpriceBTCvartext, relief=FLAT, font=(TextFontType, TextFontSize))
BLKpriceBTCvartext.set(BLKpriceBTCtext)
BLKpriceBTClabeltext.grid(row=BLKrowtext, column=PriceBTCcol)
BLKpriceBTCvardata = StringVar()
BLKpriceBTClabeldata = Label(app, textvariable=BLKpriceBTCvardata, relief=RAISED, font=(DataFontType, DataFontSize))
BLKpriceBTCupdate()
BLKpriceBTClabeldata.grid(row=BLKrowdata, column=PriceBTCcol)


# Display Data and Text for Blackcoin price in USD
BLKpriceUSDvartext = StringVar()
BLKpriceUSDlabeltext = Label(app, textvariable=BLKpriceUSDvartext, relief=FLAT, font=(TextFontType, TextFontSize))
BLKpriceUSDvartext.set(BLKpriceUSDtext)
BLKpriceUSDlabeltext.grid(row=BLKrowtext, column=PriceUSDcol)
BLKpriceUSDvardata = StringVar()
BLKpriceUSDlabeldata = Label(app, textvariable=BLKpriceUSDvardata, relief=RAISED, font=(DataFontType, DataFontSize))
BLKpriceUSDupdate()
BLKpriceUSDlabeldata.grid(row=BLKrowdata, column=PriceUSDcol)


#My BLK Value in BTC
MyBLKValueBTCvartext = StringVar()
MyBLKValueBTClabeltext = Label(app, textvariable=MyBLKValueBTCvartext, relief=FLAT, font=(TextFontType, TextFontSize))
MyBLKValueBTCvartext.set(MyBLKValueBTCtext)
MyBLKValueBTClabeltext.grid(row=BLKrowtext, column=ValueBTCcol)

MyBLKValueBTCvardata = StringVar()
MyBLKValueBTClabeldata = Label(app, textvariable=MyBLKValueBTCvardata, relief=RAISED, font=(DataFontType, DataFontSize))
MyBLKValueBTCupdate()
MyBLKValueBTClabeldata.grid(row=BLKrowdata, column=ValueBTCcol)


#My BLK Value in USD
MyBLKValueUSDvartext = StringVar()
MyBLKValueUSDlabeltext = Label(app, textvariable=MyBLKValueUSDvartext, relief=FLAT, font=(TextFontType, TextFontSize))
MyBLKValueUSDvartext.set(MyBLKValueUSDtext)
MyBLKValueUSDlabeltext.grid(row=BLKrowtext, column=ValueUSDcol)

MyBLKValueUSDvardata = StringVar()
MyBLKValueUSDlabeldata = Label(app, textvariable=MyBLKValueUSDvardata, relief=RAISED, font=(DataFontType, DataFontSize))
MyBLKValueUSDupdate()
MyBLKValueUSDlabeldata.grid(row=BLKrowdata, column=ValueUSDcol)



#LITECOIN
#MyLTC
MyLTCvartext = StringVar()
MyLTClabeltext = Label(app, textvariable=MyLTCvartext, relief=FLAT, font=(TextFontType, TextFontSize))
MyLTCvartext.set(MyLTCtext)
MyLTClabeltext.grid(row=LTCrowtext, column=MyCOINScol)
#MyLTCvardata = StringVar()
MyLTClabeldata = Label(app, text=MyLTC, relief=RAISED, font=(DataFontType, DataFontSize))
MyLTClabeldata.grid(row=LTCrowdata, column=MyCOINScol)


# Display Data and Text for Litecoin price in BTC
LTCpriceBTCvartext = StringVar()
LTCpriceBTClabeltext = Label(app, textvariable=LTCpriceBTCvartext, relief=FLAT, font=(TextFontType, TextFontSize))
LTCpriceBTCvartext.set(LTCpriceBTCtext)
LTCpriceBTClabeltext.grid(row=LTCrowtext, column=PriceBTCcol)
LTCpriceBTCvardata = StringVar()
LTCpriceBTClabeldata = Label(app, textvariable=LTCpriceBTCvardata, relief=RAISED, font=(DataFontType, DataFontSize))
LTCpriceBTCupdate()
LTCpriceBTClabeldata.grid(row=LTCrowdata, column=PriceBTCcol)


# Display Data and Text for Litecoin price in USD
LTCpriceUSDvartext = StringVar()
LTCpriceUSDlabeltext = Label(app, textvariable=LTCpriceUSDvartext, relief=FLAT, font=(TextFontType, TextFontSize))
LTCpriceUSDvartext.set(LTCpriceUSDtext)
LTCpriceUSDlabeltext.grid(row=LTCrowtext, column=PriceUSDcol)
LTCpriceUSDvardata = StringVar()
LTCpriceUSDlabeldata = Label(app, textvariable=LTCpriceUSDvardata, relief=RAISED, font=(DataFontType, DataFontSize))
LTCpriceUSDupdate()
LTCpriceUSDlabeldata.grid(row=LTCrowdata, column=PriceUSDcol)


#My LTC Value in BTC
MyLTCValueBTCvartext = StringVar()
MyLTCValueBTClabeltext = Label(app, textvariable=MyLTCValueBTCvartext, relief=FLAT, font=(TextFontType, TextFontSize))
MyLTCValueBTCvartext.set(MyLTCValueBTCtext)
MyLTCValueBTClabeltext.grid(row=LTCrowtext, column=ValueBTCcol)

MyLTCValueBTCvardata = StringVar()
MyLTCValueBTClabeldata = Label(app, textvariable=MyLTCValueBTCvardata, relief=RAISED, font=(DataFontType, DataFontSize))
MyLTCValueBTCupdate()
MyLTCValueBTClabeldata.grid(row=LTCrowdata, column=ValueBTCcol)

#My LTC Value in USD
MyLTCValueUSDvartext = StringVar()
MyLTCValueUSDlabeltext = Label(app, textvariable=MyLTCValueUSDvartext, relief=FLAT, font=(TextFontType, TextFontSize))
MyLTCValueUSDvartext.set(MyLTCValueUSDtext)
MyLTCValueUSDlabeltext.grid(row=LTCrowtext, column=ValueUSDcol)

MyLTCValueUSDvardata = StringVar()
MyLTCValueUSDlabeldata = Label(app, textvariable=MyLTCValueUSDvardata, relief=RAISED, font=(DataFontType, DataFontSize))
MyLTCValueUSDupdate()
MyLTCValueUSDlabeldata.grid(row=LTCrowdata, column=ValueUSDcol)



#DOGECOIN
#MyDOGE
MyDOGEvartext = StringVar()
MyDOGElabeltext = Label(app, textvariable=MyDOGEvartext, relief=FLAT, font=(TextFontType, TextFontSize))
MyDOGEvartext.set(MyDOGEtext)
MyDOGElabeltext.grid(row=DOGErowtext, column=MyCOINScol)
#MyDOGEvardata = StringVar()
MyDOGElabeldata = Label(app, text=MyDOGE, relief=RAISED, font=(DataFontType, DataFontSize))
MyDOGElabeldata.grid(row=DOGErowdata, column=MyCOINScol)


# Display Data and Text for Dogecoin price in BTC
DOGEpriceBTCvartext = StringVar()
DOGEpriceBTClabeltext = Label(app, textvariable=DOGEpriceBTCvartext, relief=FLAT, font=(TextFontType, TextFontSize))
DOGEpriceBTCvartext.set(DOGEpriceBTCtext)
DOGEpriceBTClabeltext.grid(row=DOGErowtext, column=PriceBTCcol)
DOGEpriceBTCvardata = StringVar()
DOGEpriceBTClabeldata = Label(app, textvariable=DOGEpriceBTCvardata, relief=RAISED, font=(DataFontType, DataFontSize))
DOGEpriceBTCupdate()
DOGEpriceBTClabeldata.grid(row=DOGErowdata, column=PriceBTCcol)


# Display Data and Text for Dogecoin price in USD
DOGEpriceUSDvartext = StringVar()
DOGEpriceUSDlabeltext = Label(app, textvariable=DOGEpriceUSDvartext, relief=FLAT, font=(TextFontType, TextFontSize))
DOGEpriceUSDvartext.set(DOGEpriceUSDtext)
DOGEpriceUSDlabeltext.grid(row=DOGErowtext, column=PriceUSDcol)
DOGEpriceUSDvardata = StringVar()
DOGEpriceUSDlabeldata = Label(app, textvariable=DOGEpriceUSDvardata, relief=RAISED, font=(DataFontType, DataFontSize))
DOGEpriceUSDupdate()
DOGEpriceUSDlabeldata.grid(row=DOGErowdata, column=PriceUSDcol)


#My DOGE Value in BTC
MyDOGEValueBTCvartext = StringVar()
MyDOGEValueBTClabeltext = Label(app, textvariable=MyDOGEValueBTCvartext, relief=FLAT, font=(TextFontType, TextFontSize))
MyDOGEValueBTCvartext.set(MyDOGEValueBTCtext)
MyDOGEValueBTClabeltext.grid(row=DOGErowtext, column=ValueBTCcol)

MyDOGEValueBTCvardata = StringVar()
MyDOGEValueBTClabeldata = Label(app, textvariable=MyDOGEValueBTCvardata, relief=RAISED, font=(DataFontType, DataFontSize))
MyDOGEValueBTCupdate()
MyDOGEValueBTClabeldata.grid(row=DOGErowdata, column=ValueBTCcol)

#My DOGE Value in USD
MyDOGEValueUSDvartext = StringVar()
MyDOGEValueUSDlabeltext = Label(app, textvariable=MyDOGEValueUSDvartext, relief=FLAT, font=(TextFontType, TextFontSize))
MyDOGEValueUSDvartext.set(MyDOGEValueUSDtext)
MyDOGEValueUSDlabeltext.grid(row=DOGErowtext, column=ValueUSDcol)

MyDOGEValueUSDvardata = StringVar()
MyDOGEValueUSDlabeldata = Label(app, textvariable=MyDOGEValueUSDvardata, relief=RAISED, font=(DataFontType, DataFontSize))
MyDOGEValueUSDupdate()
MyDOGEValueUSDlabeldata.grid(row=DOGErowdata, column=ValueUSDcol)




#DARKCOIN
#MyDRK
MyDRKvartext = StringVar()
MyDRKlabeltext = Label(app, textvariable=MyDRKvartext, relief=FLAT, font=(TextFontType, TextFontSize))
MyDRKvartext.set(MyDRKtext)
MyDRKlabeltext.grid(row=DRKrowtext, column=MyCOINScol)
#MyDRKvardata = StringVar()
MyDRKlabeldata = Label(app, text=MyDRK, relief=RAISED, font=(DataFontType, DataFontSize))
MyDRKlabeldata.grid(row=DRKrowdata, column=MyCOINScol)


# Display Data and Text for Darkcoin price in BTC
DRKpriceBTCvartext = StringVar()
DRKpriceBTClabeltext = Label(app, textvariable=DRKpriceBTCvartext, relief=FLAT, font=(TextFontType, TextFontSize))
DRKpriceBTCvartext.set(DRKpriceBTCtext)
DRKpriceBTClabeltext.grid(row=DRKrowtext, column=PriceBTCcol)
DRKpriceBTCvardata = StringVar()
DRKpriceBTClabeldata = Label(app, textvariable=DRKpriceBTCvardata, relief=RAISED, font=(DataFontType, DataFontSize))
DRKpriceBTCupdate()
DRKpriceBTClabeldata.grid(row=DRKrowdata, column=PriceBTCcol)


# Display Data and Text for Darkcoin price in USD
DRKpriceUSDvartext = StringVar()
DRKpriceUSDlabeltext = Label(app, textvariable=DRKpriceUSDvartext, relief=FLAT, font=(TextFontType, TextFontSize))
DRKpriceUSDvartext.set(DRKpriceUSDtext)
DRKpriceUSDlabeltext.grid(row=DRKrowtext, column=PriceUSDcol)
DRKpriceUSDvardata = StringVar()
DRKpriceUSDlabeldata = Label(app, textvariable=DRKpriceUSDvardata, relief=RAISED, font=(DataFontType, DataFontSize))
DRKpriceUSDupdate()
DRKpriceUSDlabeldata.grid(row=DRKrowdata, column=PriceUSDcol)


#My DRK Value in BTC
MyDRKValueBTCvartext = StringVar()
MyDRKValueBTClabeltext = Label(app, textvariable=MyDRKValueBTCvartext, relief=FLAT, font=(TextFontType, TextFontSize))
MyDRKValueBTCvartext.set(MyDRKValueBTCtext)
MyDRKValueBTClabeltext.grid(row=DRKrowtext, column=ValueBTCcol)

MyDRKValueBTCvardata = StringVar()
MyDRKValueBTClabeldata = Label(app, textvariable=MyDRKValueBTCvardata, relief=RAISED, font=(DataFontType, DataFontSize))
MyDRKValueBTCupdate()
MyDRKValueBTClabeldata.grid(row=DRKrowdata, column=ValueBTCcol)


#My DRK Value in USD
MyDRKValueUSDvartext = StringVar()
MyDRKValueUSDlabeltext = Label(app, textvariable=MyDRKValueUSDvartext, relief=FLAT, font=(TextFontType, TextFontSize))
MyDRKValueUSDvartext.set(MyDRKValueUSDtext)
MyDRKValueUSDlabeltext.grid(row=DRKrowtext, column=ValueUSDcol)

MyDRKValueUSDvardata = StringVar()
MyDRKValueUSDlabeldata = Label(app, textvariable=MyDRKValueUSDvardata, relief=RAISED, font=(DataFontType, DataFontSize))
MyDRKValueUSDupdate()
MyDRKValueUSDlabeldata.grid(row=DRKrowdata, column=ValueUSDcol)



#PEERCOIN
#MyPPC
MyPPCvartext = StringVar()
MyPPClabeltext = Label(app, textvariable=MyPPCvartext, relief=FLAT, font=(TextFontType, TextFontSize))
MyPPCvartext.set(MyPPCtext)
MyPPClabeltext.grid(row=PPCrowtext, column=MyCOINScol)
#MyPPCvardata = StringVar()
MyPPClabeldata = Label(app, text=MyPPC, relief=RAISED, font=(DataFontType, DataFontSize))
MyPPClabeldata.grid(row=PPCrowdata, column=MyCOINScol)


# Display Data and Text for Peercoin price in BTC
PPCpriceBTCvartext = StringVar()
PPCpriceBTClabeltext = Label(app, textvariable=PPCpriceBTCvartext, relief=FLAT, font=(TextFontType, TextFontSize))
PPCpriceBTCvartext.set(PPCpriceBTCtext)
PPCpriceBTClabeltext.grid(row=PPCrowtext, column=PriceBTCcol)
PPCpriceBTCvardata = StringVar()
PPCpriceBTClabeldata = Label(app, textvariable=PPCpriceBTCvardata, relief=RAISED, font=(DataFontType, DataFontSize))
PPCpriceBTCupdate()
PPCpriceBTClabeldata.grid(row=PPCrowdata, column=PriceBTCcol)


# Display Data and Text for Peercoin price in USD
PPCpriceUSDvartext = StringVar()
PPCpriceUSDlabeltext = Label(app, textvariable=PPCpriceUSDvartext, relief=FLAT, font=(TextFontType, TextFontSize))
PPCpriceUSDvartext.set(PPCpriceUSDtext)
PPCpriceUSDlabeltext.grid(row=PPCrowtext, column=PriceUSDcol)
PPCpriceUSDvardata = StringVar()
PPCpriceUSDlabeldata = Label(app, textvariable=PPCpriceUSDvardata, relief=RAISED, font=(DataFontType, DataFontSize))
PPCpriceUSDupdate()
PPCpriceUSDlabeldata.grid(row=PPCrowdata, column=PriceUSDcol)


#My PPC Value in BTC
MyPPCValueBTCvartext = StringVar()
MyPPCValueBTClabeltext = Label(app, textvariable=MyPPCValueBTCvartext, relief=FLAT, font=(TextFontType, TextFontSize))
MyPPCValueBTCvartext.set(MyPPCValueBTCtext)
MyPPCValueBTClabeltext.grid(row=PPCrowtext, column=ValueBTCcol)

MyPPCValueBTCvardata = StringVar()
MyPPCValueBTClabeldata = Label(app, textvariable=MyPPCValueBTCvardata, relief=RAISED, font=(DataFontType, DataFontSize))
MyPPCValueBTCupdate()
MyPPCValueBTClabeldata.grid(row=PPCrowdata, column=ValueBTCcol)


#My PPC Value in USD
MyPPCValueUSDvartext = StringVar()
MyPPCValueUSDlabeltext = Label(app, textvariable=MyPPCValueUSDvartext, relief=FLAT, font=(TextFontType, TextFontSize))
MyPPCValueUSDvartext.set(MyPPCValueUSDtext)
MyPPCValueUSDlabeltext.grid(row=PPCrowtext, column=ValueUSDcol)

MyPPCValueUSDvardata = StringVar()
MyPPCValueUSDlabeldata = Label(app, textvariable=MyPPCValueUSDvardata, relief=RAISED, font=(DataFontType, DataFontSize))
MyPPCValueUSDupdate()
MyPPCValueUSDlabeldata.grid(row=PPCrowdata, column=ValueUSDcol)




#FAIRCOIN
#MyFAIR
MyFAIRvartext = StringVar()
MyFAIRlabeltext = Label(app, textvariable=MyFAIRvartext, relief=FLAT, font=(TextFontType, TextFontSize))
MyFAIRvartext.set(MyFAIRtext)
MyFAIRlabeltext.grid(row=FAIRrowtext, column=MyCOINScol)
#MyFAIRvardata = StringVar()
MyFAIRlabeldata = Label(app, text=MyFAIR, relief=RAISED, font=(DataFontType, DataFontSize))
MyFAIRlabeldata.grid(row=FAIRrowdata, column=MyCOINScol)


# Display Data and Text for Faircoin price in BTC
FAIRpriceBTCvartext = StringVar()
FAIRpriceBTClabeltext = Label(app, textvariable=FAIRpriceBTCvartext, relief=FLAT, font=(TextFontType, TextFontSize))
FAIRpriceBTCvartext.set(FAIRpriceBTCtext)
FAIRpriceBTClabeltext.grid(row=FAIRrowtext, column=PriceBTCcol)
FAIRpriceBTCvardata = StringVar()
FAIRpriceBTClabeldata = Label(app, textvariable=FAIRpriceBTCvardata, relief=RAISED, font=(DataFontType, DataFontSize))
FAIRpriceBTCupdate()
FAIRpriceBTClabeldata.grid(row=FAIRrowdata, column=PriceBTCcol)


# Display Data and Text for Faircoin price in USD
FAIRpriceUSDvartext = StringVar()
FAIRpriceUSDlabeltext = Label(app, textvariable=FAIRpriceUSDvartext, relief=FLAT, font=(TextFontType, TextFontSize))
FAIRpriceUSDvartext.set(FAIRpriceUSDtext)
FAIRpriceUSDlabeltext.grid(row=FAIRrowtext, column=PriceUSDcol)
FAIRpriceUSDvardata = StringVar()
FAIRpriceUSDlabeldata = Label(app, textvariable=FAIRpriceUSDvardata, relief=RAISED, font=(DataFontType, DataFontSize))
FAIRpriceUSDupdate()
FAIRpriceUSDlabeldata.grid(row=FAIRrowdata, column=PriceUSDcol)


#My FAIR Value in BTC
MyFAIRValueBTCvartext = StringVar()
MyFAIRValueBTClabeltext = Label(app, textvariable=MyFAIRValueBTCvartext, relief=FLAT, font=(TextFontType, TextFontSize))
MyFAIRValueBTCvartext.set(MyFAIRValueBTCtext)
MyFAIRValueBTClabeltext.grid(row=FAIRrowtext, column=ValueBTCcol)

MyFAIRValueBTCvardata = StringVar()
MyFAIRValueBTClabeldata = Label(app, textvariable=MyFAIRValueBTCvardata, relief=RAISED, font=(DataFontType, DataFontSize))
MyFAIRValueBTCupdate()
MyFAIRValueBTClabeldata.grid(row=FAIRrowdata, column=ValueBTCcol)


#My FAIR Value in USD
MyFAIRValueUSDvartext = StringVar()
MyFAIRValueUSDlabeltext = Label(app, textvariable=MyFAIRValueUSDvartext, relief=FLAT, font=(TextFontType, TextFontSize))
MyFAIRValueUSDvartext.set(MyFAIRValueUSDtext)
MyFAIRValueUSDlabeltext.grid(row=FAIRrowtext, column=ValueUSDcol)

MyFAIRValueUSDvardata = StringVar()
MyFAIRValueUSDlabeldata = Label(app, textvariable=MyFAIRValueUSDvardata, relief=RAISED, font=(DataFontType, DataFontSize))
MyFAIRValueUSDupdate()
MyFAIRValueUSDlabeldata.grid(row=FAIRrowdata, column=ValueUSDcol)


#TOTAL
#My Total Value in BTC
MyTotalValueBTCvartext = StringVar()
MyTotalValueBTClabeltext = Label(app, textvariable=MyTotalValueBTCvartext, relief=FLAT, font=(TextFontType, TextFontSize))
MyTotalValueBTCvartext.set(MyTotalValueBTCtext)
MyTotalValueBTClabeltext.grid(row=100, column=ValueBTCcol)

MyTotalValueBTCvardata = StringVar()
MyTotalValueBTClabeldata = Label(app, textvariable=MyTotalValueBTCvardata, relief=RAISED, font=(DataFontType, DataFontSize))
MyTotalValueBTCupdate()
MyTotalValueBTClabeldata.grid(row=101, column=ValueBTCcol)


#TOTAL
#My Total Value in USD
MyTotalValueUSDvartext = StringVar()
MyTotalValueUSDlabeltext = Label(app, textvariable=MyTotalValueUSDvartext, relief=FLAT, font=(TextFontType, TextFontSize))
MyTotalValueUSDvartext.set(MyTotalValueUSDtext)
MyTotalValueUSDlabeltext.grid(row=100, column=ValueUSDcol)

MyTotalValueUSDvardata = StringVar()
MyTotalValueUSDlabeldata = Label(app, textvariable=MyTotalValueUSDvardata, relief=RAISED, font=(DataFontType, DataFontSize))
MyTotalValueUSDupdate()
MyTotalValueUSDlabeldata.grid(row=101, column=ValueUSDcol)




'''
EEE = Entry(app, bd =5,)
ShowEEE = Entry(app, show = EEE)
EEE.pack(side = RIGHT)
'''

root.mainloop()