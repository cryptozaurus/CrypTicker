# Python 2.7.6. WBN Calling exchange APIs.
import time, json, requests
import statistics
from Tkinter import *


#Variables
MyBTC = 11.11
MyBLK = 14361
MyLTC = 30
MyDOGE = 113356
MyDRK = 45
MyPPC = 12.89
MyNXT = 794
MyXCP = 3.4032
MyNMC = 5.4
MyXMR = 20
MyBTS = 1025
MyFAIR = 33408


#BTC - USD exchanges URL
BTCexchangeURL1 = 'https://www.bitstamp.net/api/ticker/'
BTCexchangeURL2 = 'https://btc-e.com/api/2/btc_usd/ticker'
BTCexchangeURL3 = 'https://coinbase.com/api/v1/prices/buy'
bitstampUSDexchangeURL = 'https://www.bitstamp.net/api/ticker/'
btceUSDexchangeURL = 'https://btc-e.com/api/2/btc_usd/ticker'
coinbaseUSDexchangeURL = 'https://coinbase.com/api/v1/prices/buy'
krakenUSDexchangeURL = 'https://api.kraken.com/0/public/Ticker'
bitfinexUSDexchangeURL = "https://api.bitfinex.com/v1/ticker/btcusd"
cryptsyUSDexchangeURL = 'http://pubapi.cryptsy.com/api.php?method=singlemarketdata&marketid=2'
localbitcoinsUSDexchangeURL = 'https://localbitcoins.com/bitcoinaverage/ticker-all-currencies/'
#BLK - BTC pair by market volume
# Bittrex, Cryptsy, AllCoin, Melotic, Poloniex, BTER, Crypto-Trade, Bleutrade, Vircurex, CCEDK, Coin-Swap, useCryptos, Atomic Trade
BLKexchangeURL1 = 'http://bittrex.com/api/v1.1/public/getticker?market=BTC-BC'
BLKexchangeURL2 = 'http://pubapi.cryptsy.com/api.php?method=singlemarketdata&marketid=179'
BLKexchangeURL3 = 'https://www.allcoin.com/api2/pair/BC_BTC'
#LTC - BTC pair by market volume
#BTC-E, Bitfinex, HitBTC, Cryptsy, BTC China, CEX.IO, Justcoin, UpBit, Bittrex, Kraken, AllCoin, BTER, Poloniex, Bleutrade,Exmo, mcxNOW, Vircurex, Crypto-Trade, useCryptos, Bitorado, Ask Coin, BTC38, C-CEX, Cryptonit, SwissCEX, CCEDK, Cryptex, Coinbroker, Coin-Swap, Atomic Trade, Coins-E, NXT-E, Vault of Satoshi, BX Thailand, MasterXchange
LTCexchangeURL1 = 'https://btc-e.com/api/2/ltc_btc/ticker'
LTCexchangeURL2 = 'https://api.bitfinex.com/v1/ticker/ltcbtc'
LTCexchangeURL3 = 'http://pubapi.cryptsy.com/api.php?method=singlemarketdata&marketid=3'
DOGEexchangeURL1 = 'http://pubapi.cryptsy.com/api.php?method=singlemarketdata&marketid=132'
DOGEexchangeURL2 = 'http://data.bter.com/api/1/ticker/doge_btc'
DOGEexchangeURL3 = 'http://bittrex.com/api/v1.1/public/getticker?market=BTC-DOGE'
DRKexchangeURL1 = 'http://pubapi.cryptsy.com/api.php?method=singlemarketdata&marketid=155'
DRKexchangeURL2 = 'https://bittrex.com/api/v1.1/public/getticker?market=BTC-DRK'
DRKexchangeURL3 = 'http://data.bter.com/api/1/ticker/drk_btc'
PPCexchangeURL1 = 'http://pubapi.cryptsy.com/api.php?method=singlemarketdata&marketid=28'
PPCexchangeURL2 = 'https://btc-e.com/api/2/ppc_btc/ticker'
PPCexchangeURL3 = 'http://data.bter.com/api/1/ticker/ppc_btc'
NXTexchangeURL1 = 'http://data.bter.com/api/1/ticker/nxt_btc'
NXTexchangeURL2 = 'http://pubapi.cryptsy.com/api.php?method=singlemarketdata&marketid=159'
NXTexchangeURL3 = 'https://api.hitbtc.com/api/1/public/ticker'
XCPexchangeURL1 = 'https://poloniex.com/public?command=returnTicker'
XCPexchangeURL2 = 'http://data.bter.com/api/1/ticker/XCP_btc'
XCPexchangeURL3 = 'https://www.melotic.com/api/markets'
NMCexchangeURL1 = 'https://btc-e.com/api/2/nmc_btc/ticker'
NMCexchangeURL2 = 'https://cex.io/api/ticker/NMC/BTC'
NMCexchangeURL3 = 'http://pubapi.cryptsy.com/api.php?method=singlemarketdata&marketid=29'
XMRexchangeURL1 = 'https://poloniex.com/public?command=returnTicker'
XMRexchangeURL2 = 'https://api.hitbtc.com/api/1/public/ticker'
XMRexchangeURL3 = 'http://data.bter.com/api/1/ticker/xmr_btc'
BTSexchangeURL1 = 'http://data.bter.com/api/1/ticker/BTS_btc'
BTSexchangeURL2 = 'http://api.btc38.com/v1/ticker.php?c=bts&mk_type=btc'
BTSexchangeURL3 = 'https://poloniex.com/public?command=returnTicker'
FAIRexchangeURL1 = 'https://bittrex.com/api/v1.1/public/getticker?market=BTC-FAIR'
FAIRexchangeURL2 = 'https://api.vaultex.io/v1/market/stats/FAIR/BTC'
FAIRexchangeURL3 = 'https://alcurex.org/api/market.php?pair=fair_btc&last=last'



# Change Exchange Name in Menu
exchangeNametext = " Exchange Name "
BTCexchangeName0text = " Price Average "
BTCexchangeName1text = " Bitfinex "
BTCexchangeName2text = " Bitstamp "
BTCexchangeName3text = " Btc-e "
BTCexchangeName4text = " Coinbase "
BTCexchangeName5text = " Kraken "
BTCexchangeName6text = " Cryptsy "
BTCexchangeName7text = " Local Bitcoins "

BLKexchangeName1text = " Bittrex "
BLKexchangeName2text = " Cryptsy "
BLKexchangeName3text = " Allcoin "

LTCexchangeName1text = " Btc-e "
LTCexchangeName2text = " Bitfinex "
LTCexchangeName3text = " Cryptsy "

DOGEexchangeName1text = " Cryptsy "
DOGEexchangeName2text = " Bter "
DOGEexchangeName3text = " Bittrex "

DRKexchangeName1text = " Cryptsy "
DRKexchangeName2text = " Bittrex "
DRKexchangeName3text = " Bter "

PPCexchangeName1text = " Cryptsy "
PPCexchangeName2text = " Btc-e "
PPCexchangeName3text = " Bter "

NXTexchangeName1text = " Bter "
NXTexchangeName2text = " Cryptsy "
NXTexchangeName3text = " HitBTC "

XCPexchangeName1text = " Poloniex "
XCPexchangeName2text = " Bter "
XCPexchangeName3text = " Melotic "

NMCexchangeName1text = " Btc-e "
NMCexchangeName2text = " CEX.io "
NMCexchangeName3text = " Cryptsy "

XMRexchangeName1text = " Poloniex "
XMRexchangeName2text = " HitBTC "
XMRexchangeName3text = " Bter "

BTSexchangeName1text = " Bter "
BTSexchangeName2text = " BTC38 "
BTSexchangeName3text = " Poloniex "

FAIRexchangeName1text = " Bittrex "
FAIRexchangeName2text = " Vaultex "
FAIRexchangeName3text = " Alcurex "


# Choose Default Exchange Name:
global BTCexchangeNamevardata
BTCexchangeNamevardata = "priceaverage"
global BLKexchangeNamevardata
BLKexchangeNamevardata = "one"
global LTCexchangeNamevardata
LTCexchangeNamevardata = "one"
global DOGEexchangeNamevardata
DOGEexchangeNamevardata = "one"
global DRKexchangeNamevardata
DRKexchangeNamevardata = "one"
global PPCexchangeNamevardata
PPCexchangeNamevardata = "one"
global NXTexchangeNamevardata
NXTexchangeNamevardata = "one"
global XCPexchangeNamevardata
XCPexchangeNamevardata = "one"
global NMCexchangeNamevardata
NMCexchangeNamevardata = "one"
global XMRexchangeNamevardata
XMRexchangeNamevardata = "one"
global BTSexchangeNamevardata
BTSexchangeNamevardata = "one"
global FAIRexchangeNamevardata
FAIRexchangeNamevardata = "one"


# Font Type and Size
TextFontType = "Georgia"
DataFontType = "Comic Sans MS"
TextFontSize = 12
DataFontSize = 15


# Colors
AppWindowBackgroundColor = "#181a1e"
ButtonBackGroundColor = "#aaaaaa"
ButtonForegroundColor = "black"
TextBackgroundColor = "#181a1e"
TextForegroundColor = "#8e9194"
DataBackgroundColor = "#181a1e"
DataForegroundColor = "#00cc00" #00cc00, #f89a28
EntryBackgroundColor = "#333333"
EntryForegroundColor = "white"
ExchangeNameActiveBackgroundColor = "#292c30"
COINSbackgroundColor = "#181a1e"


# Text
PriceAverageUSDtext = str(" Price Average ")
bitstampUSDtext = str(" Bitstamp ")
btceUSDtext = str(" Btc-e ")
coinbaseUSDtext = str(" Coinbase ")
krakenUSDtext = str(" Kraken ")
bitfinexUSDtext = str(" Bitfinex ")
cryptsyUSDtext = str(" Cryptsy ")
localbitcoinsUSDtext = str(" Local Bitcoins ")
MyBTCtext = " My BTC "
MyBLKtext = " My BLK "
MyLTCtext = " My LTC "
MyDOGEtext = " My DOGE "
MyDRKtext = " My DRK "
MyPPCtext = " My PPC "
MyNXTtext = " My NXT "
MyXCPtext = " My XCP "
MyNMCtext = " My NMC "
MyXMRtext = " My XMR "
MyBTStext = " My BTS "
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
NXTpriceBTCtext = str(" NXT Price in BTC ")
NXTpriceUSDtext = str(" NXT Price in USD ")
XCPpriceBTCtext = str(" XCP Price in BTC ")
XCPpriceUSDtext = str(" XCP Price in USD ")
NMCpriceBTCtext = str(" NMC Price in BTC ")
NMCpriceUSDtext = str(" NMC Price in USD ")
XMRpriceBTCtext = str(" XMR Price in BTC ")
XMRpriceUSDtext = str(" XMR Price in USD ")
BTSpriceBTCtext = str(" BTS Price in BTC ")
BTSpriceUSDtext = str(" BTS Price in USD ")
FAIRpriceBTCtext = str(" FAIR Price in BTC ")
FAIRpriceUSDtext = str(" FAIR Price in USD ")
MyBTCValuetext = str(" My BTC Value in USD ")
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
MyNXTValueUSDtext = str(" My NXT Value in USD ")
MyNXTValueBTCtext = str(" My NXT Value in BTC ")
MyXCPValueUSDtext = str(" My XCP Value in USD ")
MyXCPValueBTCtext = str(" My XCP Value in BTC ")
MyNMCValueUSDtext = str(" My NMC Value in USD ")
MyNMCValueBTCtext = str(" My NMC Value in BTC ")
MyXMRValueUSDtext = str(" My XMR Value in USD ")
MyXMRValueBTCtext = str(" My XMR Value in BTC ")
MyBTSValueUSDtext = str(" My BTS Value in USD ")
MyBTSValueBTCtext = str(" My BTS Value in BTC ")
MyFAIRValueUSDtext = str(" My FAIR Value in USD ")
MyFAIRValueBTCtext = str(" My FAIR Value in BTC ")
MyTotalValueUSDtext = str(" My Total Value in USD ")
MyTotalValueBTCtext = str(" My Total Value in BTC ")

# Update Interval
UpdateIntervalSec = 60
UpdateInterval = UpdateIntervalSec * 1000
UpdateIntervalSectext = str(" Update Interval (s) ")

# Rows
# BTC price in USD
bitfinexUSDrow = 3
bitstampUSDrow = 5
btceUSDrow = 7
coinbaseUSDrow = 9
krakenUSDrow = 11
cryptsyUSDrow = 13
localbitcoinsUSDrow = 15
# COINS
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
NXTrowtext = 13
NXTrowdata = 14
XCProwtext = 15
XCProwdata = 16
NMCrowtext = 17
NMCrowdata = 18
XMRrowtext = 19
XMRrowdata = 20
BTSrowtext = 21
BTSrowdata = 22
FAIRrowtext = 23
FAIRrowdata = 24

# Columns
BTCUSDcol = 0
COINSimagecol = 3
MyCOINScol = 5
updateMyCOINScol = 6
PriceBTCcol = 7
PriceUSDcol = 9
ValueBTCcol = 11
ValueUSDcol = 13
exchangeNamecol = 15




#BITCOIN
# Import and Update API DATA for Bitcoin
def BTCexchangeNameUpdate(BTCexchangeNameValue):
    if BTCexchangeNameValue == BTCexchangeName0text:
        print BTCexchangeName0text
        global BTCexchangeNamevardata
        global BTCpriceUSDvardata
        BTCexchangeNamevardata = "priceaverage"
        BTCpriceUSDvardata = StringVar()
        BTCpriceUSDvardata = PriceAverageUSDvardata
        print BTCexchangeNamevardata
        BTCupdateALL()
    if BTCexchangeNameValue == BTCexchangeName1text:
        print BTCexchangeName1text
        BTCexchangeNamevardata = "one"
        BTCpriceUSDvardata = bitfinexUSDvardata
        print BTCexchangeNamevardata
        BTCupdateALL()
    if BTCexchangeNameValue == BTCexchangeName2text:
        print BTCexchangeName2text
        BTCexchangeNamevardata = "two"
        BTCpriceUSDvardata = bitstampUSDvardata
        print BTCexchangeNamevardata
        BTCupdateALL()
    if BTCexchangeNameValue == BTCexchangeName3text:
        print BTCexchangeName3text
        BTCexchangeNamevardata = "three"
        BTCpriceUSDvardata = btceUSDvardata
        print BTCexchangeNamevardata
        BTCupdateALL()
    if BTCexchangeNameValue == BTCexchangeName4text:
        print BTCexchangeName4text
        BTCexchangeNamevardata = "four"
        BTCpriceUSDvardata = coinbaseUSDvardata
        print BTCexchangeNamevardata
        BTCupdateALL()
    if BTCexchangeNameValue == BTCexchangeName5text:
        print BTCexchangeName5text
        BTCexchangeNamevardata = "five"
        BTCpriceUSDvardata = krakenUSDvardata
        print BTCexchangeNamevardata
        BTCupdateALL()
    if BTCexchangeNameValue == BTCexchangeName6text:
        print BTCexchangeName6text
        BTCexchangeNamevardata = "six"
        BTCpriceUSDvardata = cryptsyUSDvardata
        print BTCexchangeNamevardata
        BTCupdateALL()
    if BTCexchangeNameValue == BTCexchangeName7text:
        print BTCexchangeName7text
        BTCexchangeNamevardata = "seven"
        BTCpriceUSDvardata = localbitcoinsUSDvardata
        print BTCexchangeNamevardata
        BTCupdateALL()


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


def localbitcoinsUSD():
    try:
        localbitcoinsBTCTick = requests.get(localbitcoinsUSDexchangeURL)
        return localbitcoinsBTCTick.json()["USD"]["avg_12h"]
    except Exception:
        print "Local Bitcoins API error"
        return 0

def localbitcoinsUSDupdate():
    global localbitcoinsUSDvardata
    localbitcoinsUSDvardata.set(str.format("{0:.2f}", (float(localbitcoinsUSD()))))
    root.after(UpdateInterval, localbitcoinsUSDupdate)


def PriceAverageUSDupdate():
    global PriceAverageUSDvardatalist
    PriceAverageUSDvardatalist = [float(bitstampUSDvardata.get()), float(btceUSDvardata.get()), float(coinbaseUSDvardata.get()), float(krakenUSDvardata.get()), float(bitfinexUSDvardata.get()), float(cryptsyUSDvardata.get()), float(localbitcoinsUSDvardata.get())]
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

def MyBTCValueUSDupdate():
    global MyBTCValuevardata
    MyBTCValuevardata.set(str.format("{0:.2f}", (float(MyBTCValue()))))
    root.after(UpdateInterval, MyBTCValueUSDupdate)


# Display Data and Text for Bitcoin price in USD
def BTCpriceUSDdataUpdate():

    BTCpriceUSDlabeldata = Label(app, textvariable=BTCpriceUSDvardata, relief=RAISED, font=(DataFontType, DataFontSize), bg=DataBackgroundColor, fg=DataForegroundColor)
    BTCpriceUSDlabeldata.grid(row=BTCrowdata, column=PriceUSDcol)





#BLACKCOIN
# Import and Update API DATA for Blackcoin price in BTC
def BLKexchangeNameUpdate(BLKexchangeNameValue):
    if BLKexchangeNameValue == BLKexchangeName1text:
        print BLKexchangeName1text
        global BLKexchangeNamevardata
        BLKexchangeNamevardata = "one"
        print BLKexchangeNamevardata
        BLKupdateALL()
    elif BLKexchangeNameValue == BLKexchangeName2text:
        print BLKexchangeName2text
        BLKexchangeNamevardata = "two"
        print BLKexchangeNamevardata
        BLKupdateALL()
    else:
        print BLKexchangeName3text
        BLKexchangeNamevardata = "three"
        print BLKexchangeNamevardata
        BLKupdateALL()

def BLKpriceBTC():
    if BLKexchangeNamevardata == "one":
        try:
            Tick = requests.get(BLKexchangeURL1)
            return Tick.json()['result']['Last']
        except Exception:
            print "BLKpriceBTC API error"
            return 0
    if BLKexchangeNamevardata == "two":
        try:
            Tick = requests.get(BLKexchangeURL2)
            return Tick.json()["return"]["markets"]["BC"]['lasttradeprice']
        except Exception:
            print "BLKpriceBTC API error"
            return 0
    if BLKexchangeNamevardata == "three":
        try:
            Tick = requests.get(BLKexchangeURL3)
            return Tick.json()['data']['trade_price']
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
    MyBLKValueUSD = float(BLKpriceUSDvardata.get()) * float(MyBLKvardata.get())
    return MyBLKValueUSD

def MyBLKValueUSDupdate():
    global MyBLKValueUSDvardata
    MyBLKValueUSDvardata.set(str.format("{0:.2f}", (float(MyBLKValueUSD()))))
    root.after(UpdateInterval, MyBLKValueUSDupdate)


# Calculate and Update my Blackcoin Value in BTC
def MyBLKValueBTC():
    MyBLKValueBTC = float(BLKpriceBTCvardata.get()) * float(MyBLKvardata.get())
    return MyBLKValueBTC

def MyBLKValueBTCupdate():
    global MyBLKValueBTCvardata
    MyBLKValueBTCvardata.set(str.format("{0:.8f}", (float(MyBLKValueBTC()))))
    root.after(UpdateInterval, MyBLKValueBTCupdate)



#LITECOIN
# Import and Update API DATA for Litecoin price in BTC
def LTCexchangeNameUpdate(LTCexchangeNameValue):
    if LTCexchangeNameValue == LTCexchangeName1text:
        print LTCexchangeName1text
        global LTCexchangeNamevardata
        LTCexchangeNamevardata = "one"
        print LTCexchangeNamevardata
        LTCupdateALL()
    elif LTCexchangeNameValue == LTCexchangeName2text:
        print LTCexchangeName2text
        LTCexchangeNamevardata = "two"
        print LTCexchangeNamevardata
        LTCupdateALL()
    else:
        print LTCexchangeName3text
        LTCexchangeNamevardata = "three"
        print LTCexchangeNamevardata
        LTCupdateALL()

def LTCpriceBTC():
    if LTCexchangeNamevardata == "one":
        try:
            Tick = requests.get(LTCexchangeURL1)
            return Tick.json()['ticker']['last']
        except Exception:
            print "LTCpriceBTC API error"
            return 0
    if LTCexchangeNamevardata == "two":
        try:
            Tick = requests.get(LTCexchangeURL2)
            return Tick.json()['last_price']
        except Exception:
            print "LTCpriceBTC API error"
            return 0
    if LTCexchangeNamevardata == "three":
        try:
            Tick = requests.get(LTCexchangeURL3)
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
    MyLTCValueUSD = float(LTCpriceUSDvardata.get()) * float(MyLTCvardata.get())
    return MyLTCValueUSD

def MyLTCValueUSDupdate():
    global MyLTCValueUSDvardata
    MyLTCValueUSDvardata.set(str.format("{0:.2f}", (float(MyLTCValueUSD()))))
    root.after(UpdateInterval, MyLTCValueUSDupdate)


# Calculate and Update my Litecoin Value in BTC
def MyLTCValueBTC():
    MyLTCValueBTC = float(LTCpriceBTCvardata.get()) * float(MyLTCvardata.get())
    return MyLTCValueBTC

def MyLTCValueBTCupdate():
    global MyLTCValueBTCvardata
    MyLTCValueBTCvardata.set(str.format("{0:.8f}", (float(MyLTCValueBTC()))))
    root.after(UpdateInterval, MyLTCValueBTCupdate)



#DOGECOIN
# Import and Update API DATA for Dogecoin price in BTC
def DOGEexchangeNameUpdate(DOGEexchangeNameValue):
    if DOGEexchangeNameValue == DOGEexchangeName1text:
        print DOGEexchangeName1text
        global DOGEexchangeNamevardata
        DOGEexchangeNamevardata = "one"
        print DOGEexchangeNamevardata
        DOGEupdateALL()
    elif DOGEexchangeNameValue == DOGEexchangeName2text:
        print DOGEexchangeName2text
        DOGEexchangeNamevardata = "two"
        print DOGEexchangeNamevardata
        DOGEupdateALL()
    else:
        print DOGEexchangeName3text
        DOGEexchangeNamevardata = "three"
        print DOGEexchangeNamevardata
        DOGEupdateALL()

def DOGEpriceBTC():
    if DOGEexchangeNamevardata == "one":
        try:
            Tick = requests.get(DOGEexchangeURL1)
            return Tick.json()["return"]["markets"]["DOGE"]['lasttradeprice']
        except Exception:
            print "DOGEpriceBTC API error"
            return 0
    if DOGEexchangeNamevardata == "two":
        try:
            Tick = requests.get(DOGEexchangeURL2)
            return Tick.json()['last']
        except Exception:
            print "DOGEpriceBTC API error"
            return 0
    if DOGEexchangeNamevardata == "three":
        try:
            Tick = requests.get(DOGEexchangeURL3)
            return Tick.json()['result']['Last']
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
    MyDOGEValueUSD = float(DOGEpriceUSDvardata.get()) * float(MyDOGEvardata.get())
    return MyDOGEValueUSD

def MyDOGEValueUSDupdate():
    global MyDOGEValueUSDvardata
    MyDOGEValueUSDvardata.set(str.format("{0:.2f}", (float(MyDOGEValueUSD()))))
    root.after(UpdateInterval, MyDOGEValueUSDupdate)


# Calculate and Update my Dogecoin Value in BTC
def MyDOGEValueBTC():
    MyDOGEValueBTC = float(DOGEpriceBTCvardata.get()) * float(MyDOGEvardata.get())
    return MyDOGEValueBTC

def MyDOGEValueBTCupdate():
    global MyDOGEValueBTCvardata
    MyDOGEValueBTCvardata.set(str.format("{0:.8f}", (float(MyDOGEValueBTC()))))
    root.after(UpdateInterval, MyDOGEValueBTCupdate)



#DARKCOIN
# Import and Update API DATA for Darkcoin price in BTC
def DRKexchangeNameUpdate(DRKexchangeNameValue):
    if DRKexchangeNameValue == DRKexchangeName1text:
        print DRKexchangeName1text
        global DRKexchangeNamevardata
        DRKexchangeNamevardata = "one"
        print DRKexchangeNamevardata
        DRKupdateALL()
    elif DRKexchangeNameValue == DRKexchangeName2text:
        print DRKexchangeName2text
        DRKexchangeNamevardata = "two"
        print DRKexchangeNamevardata
        DRKupdateALL()
    else:
        print DRKexchangeName3text
        DRKexchangeNamevardata = "three"
        print DRKexchangeNamevardata
        DRKupdateALL()

def DRKpriceBTC():
    if DRKexchangeNamevardata == "one":
        try:
            Tick = requests.get(DRKexchangeURL1)
            return Tick.json()["return"]["markets"]["DRK"]['lasttradeprice']
        except Exception:
            print "DRKpriceBTC API error"
            return 0
    if DRKexchangeNamevardata == "two":
        try:
            Tick = requests.get(DRKexchangeURL2)
            return Tick.json()['result']['Last']
        except Exception:
            print "DRKpriceBTC API error"
            return 0
    if DRKexchangeNamevardata == "three":
        try:
            Tick = requests.get(DRKexchangeURL3)
            return Tick.json()['last']
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
    MyDRKValueUSD = float(DRKpriceUSDvardata.get()) * float(MyDRKvardata.get())
    return MyDRKValueUSD

def MyDRKValueUSDupdate():
    global MyDRKValueUSDvardata
    MyDRKValueUSDvardata.set(str.format("{0:.2f}", (float(MyDRKValueUSD()))))
    root.after(UpdateInterval, MyDRKValueUSDupdate)


# Calculate and Update my Darkcoin Value in BTC
def MyDRKValueBTC():
    MyDRKValueBTC = float(DRKpriceBTCvardata.get()) * float(MyDRKvardata.get())
    return MyDRKValueBTC

def MyDRKValueBTCupdate():
    global MyDRKValueBTCvardata
    MyDRKValueBTCvardata.set(str.format("{0:.8f}", (float(MyDRKValueBTC()))))
    root.after(UpdateInterval, MyDRKValueBTCupdate)



#PEERCOIN
# Import and Update API DATA for Peercoin price in BTC
def PPCexchangeNameUpdate(PPCexchangeNameValue):
    if PPCexchangeNameValue == PPCexchangeName1text:
        print PPCexchangeName1text
        global PPCexchangeNamevardata
        PPCexchangeNamevardata = "one"
        print PPCexchangeNamevardata
        PPCupdateALL()
    elif PPCexchangeNameValue == PPCexchangeName2text:
        print PPCexchangeName2text
        PPCexchangeNamevardata = "two"
        print PPCexchangeNamevardata
        PPCupdateALL()
    else:
        print PPCexchangeName3text
        PPCexchangeNamevardata = "three"
        print PPCexchangeNamevardata
        PPCupdateALL()

def PPCpriceBTC():
    if PPCexchangeNamevardata == "one":
        try:
            Tick = requests.get(PPCexchangeURL1)
            return Tick.json()["return"]["markets"]["PPC"]['lasttradeprice']
        except Exception:
            print "PPCpriceBTC API error"
            return 0
    if PPCexchangeNamevardata == "two":
        try:
            Tick = requests.get(PPCexchangeURL2)
            return Tick.json()['ticker']['last']
        except Exception:
            print "PPCpriceBTC API error"
            return 0
    if PPCexchangeNamevardata == "three":
        try:
            Tick = requests.get(PPCexchangeURL3)
            return Tick.json()['last']
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
    MyPPCValueUSD = float(PPCpriceUSDvardata.get()) * float(MyPPCvardata.get())
    return MyPPCValueUSD

def MyPPCValueUSDupdate():
    global MyPPCValueUSDvardata
    MyPPCValueUSDvardata.set(str.format("{0:.2f}", (float(MyPPCValueUSD()))))
    root.after(UpdateInterval, MyPPCValueUSDupdate)


# Calculate and Update my Peercoin Value in BTC
def MyPPCValueBTC():
    MyPPCValueBTC = float(PPCpriceBTCvardata.get()) * float(MyPPCvardata.get())
    return MyPPCValueBTC

def MyPPCValueBTCupdate():
    global MyPPCValueBTCvardata
    MyPPCValueBTCvardata.set(str.format("{0:.8f}", (float(MyPPCValueBTC()))))
    root.after(UpdateInterval, MyPPCValueBTCupdate)



#NXTcoin
# Import and Update API DATA for NXTcoin price in BTC
def NXTexchangeNameUpdate(NXTexchangeNameValue):
    if NXTexchangeNameValue == NXTexchangeName1text:
        print NXTexchangeName1text
        global NXTexchangeNamevardata
        NXTexchangeNamevardata = "one"
        print NXTexchangeNamevardata
        NXTupdateALL()
    elif NXTexchangeNameValue == NXTexchangeName2text:
        print NXTexchangeName2text
        NXTexchangeNamevardata = "two"
        print NXTexchangeNamevardata
        NXTupdateALL()
    else:
        print NXTexchangeName3text
        NXTexchangeNamevardata = "three"
        print NXTexchangeNamevardata
        NXTupdateALL()

def NXTpriceBTC():
    if NXTexchangeNamevardata == "one":
        try:
            Tick = requests.get(NXTexchangeURL1)
            return Tick.json()['last']
        except Exception:
            print "NXTpriceBTC API error"
            return 0
    if NXTexchangeNamevardata == "two":
        try:
            Tick = requests.get(NXTexchangeURL2)
            return Tick.json()["return"]["markets"]["NXT"]['lasttradeprice']
        except Exception:
            print "NXTpriceBTC API error"
            return 0
    if NXTexchangeNamevardata == "three":
        try:
            Tick = requests.get(NXTexchangeURL3)
            return Tick.json()['NXTBTC']['last']
        except Exception:
            print "NXTpriceBTC API error"
            return 0

def NXTpriceBTCupdate():
    global NXTpriceBTCvardata
    NXTpriceBTCvardata.set(str.format("{0:.8f}", (float(NXTpriceBTC()))))
    root.after(UpdateInterval, NXTpriceBTCupdate)


# Calculate and Update with Price Average DATA for NXTcoin price in USD
def NXTpriceUSD():
    NXTpriceUSD = float(NXTpriceBTCvardata.get()) * float(PriceAverageUSDvardata.get())
    return NXTpriceUSD

def NXTpriceUSDupdate():
    global NXTpriceUSDvardata
    NXTpriceUSDvardata.set(str.format("{0:.8f}", (float(NXTpriceUSD()))))
    root.after(UpdateInterval, NXTpriceUSDupdate)


# Calculate and Update my NXTcoin Value in USD
def MyNXTValueUSD():
    global NXTpriceUSDvardata
    MyNXTValueUSD = float(NXTpriceUSDvardata.get()) * float(MyNXTvardata.get())
    return MyNXTValueUSD

def MyNXTValueUSDupdate():
    global MyNXTValueUSDvardata
    MyNXTValueUSDvardata.set(str.format("{0:.2f}", (float(MyNXTValueUSD()))))
    root.after(UpdateInterval, MyNXTValueUSDupdate)


# Calculate and Update my NXTcoin Value in BTC
def MyNXTValueBTC():
    MyNXTValueBTC = float(NXTpriceBTCvardata.get()) * float(MyNXTvardata.get())
    return MyNXTValueBTC

def MyNXTValueBTCupdate():
    global MyNXTValueBTCvardata
    MyNXTValueBTCvardata.set(str.format("{0:.8f}", (float(MyNXTValueBTC()))))
    root.after(UpdateInterval, MyNXTValueBTCupdate)



#Counterparty
# Import and Update API DATA for Counterparty price in BTC
def XCPexchangeNameUpdate(XCPexchangeNameValue):
    if XCPexchangeNameValue == XCPexchangeName1text:
        print XCPexchangeName1text
        global XCPexchangeNamevardata
        XCPexchangeNamevardata = "one"
        print XCPexchangeNamevardata
        XCPupdateALL()
    elif XCPexchangeNameValue == XCPexchangeName2text:
        print XCPexchangeName2text
        XCPexchangeNamevardata = "two"
        print XCPexchangeNamevardata
        XCPupdateALL()
    else:
        print XCPexchangeName3text
        XCPexchangeNamevardata = "three"
        print XCPexchangeNamevardata
        XCPupdateALL()

def XCPpriceBTC():
    if XCPexchangeNamevardata == "one":
        try:
            Tick = requests.get(XCPexchangeURL1)
            return Tick.json()['BTC_XCP']['last']
        except Exception:
            print "XCPpriceBTC API error"
            return 0
    if XCPexchangeNamevardata == "two":
        try:
            Tick = requests.get(XCPexchangeURL2)
            return Tick.json()['last']
        except Exception:
            print "XCPpriceBTC API error"
            return 0
    if XCPexchangeNamevardata == "three":
        try:
            Tick = requests.get(XCPexchangeURL3)
            return Tick.json()['xcp-btc']['latest_price']
        except Exception:
            print "XCPpriceBTC API error"
            return 0

def XCPpriceBTCupdate():
    global XCPpriceBTCvardata
    XCPpriceBTCvardata.set(str.format("{0:.8f}", (float(XCPpriceBTC()))))
    root.after(UpdateInterval, XCPpriceBTCupdate)


# Calculate and Update with Price Average DATA for Counterparty price in USD
def XCPpriceUSD():
    XCPpriceUSD = float(XCPpriceBTCvardata.get()) * float(PriceAverageUSDvardata.get())
    return XCPpriceUSD

def XCPpriceUSDupdate():
    global XCPpriceUSDvardata
    XCPpriceUSDvardata.set(str.format("{0:.8f}", (float(XCPpriceUSD()))))
    root.after(UpdateInterval, XCPpriceUSDupdate)


# Calculate and Update my Counterparty Value in USD
def MyXCPValueUSD():
    global XCPpriceUSDvardata
    MyXCPValueUSD = float(XCPpriceUSDvardata.get()) * float(MyXCPvardata.get())
    return MyXCPValueUSD

def MyXCPValueUSDupdate():
    global MyXCPValueUSDvardata
    MyXCPValueUSDvardata.set(str.format("{0:.2f}", (float(MyXCPValueUSD()))))
    root.after(UpdateInterval, MyXCPValueUSDupdate)


# Calculate and Update my Counterparty Value in BTC
def MyXCPValueBTC():
    MyXCPValueBTC = float(XCPpriceBTCvardata.get()) * float(MyXCPvardata.get())
    return MyXCPValueBTC

def MyXCPValueBTCupdate():
    global MyXCPValueBTCvardata
    MyXCPValueBTCvardata.set(str.format("{0:.8f}", (float(MyXCPValueBTC()))))
    root.after(UpdateInterval, MyXCPValueBTCupdate)



#Namecoin
# Import and Update API DATA for Namecoin price in BTC
def NMCexchangeNameUpdate(NMCexchangeNameValue):
    if NMCexchangeNameValue == NMCexchangeName1text:
        print NMCexchangeName1text
        global NMCexchangeNamevardata
        NMCexchangeNamevardata = "one"
        print NMCexchangeNamevardata
        NMCupdateALL()
    elif NMCexchangeNameValue == NMCexchangeName2text:
        print NMCexchangeName2text
        NMCexchangeNamevardata = "two"
        print NMCexchangeNamevardata
        NMCupdateALL()
    else:
        print NMCexchangeName3text
        NMCexchangeNamevardata = "three"
        print NMCexchangeNamevardata
        NMCupdateALL()

def NMCpriceBTC():
    if NMCexchangeNamevardata == "one":
        try:
            Tick = requests.get(NMCexchangeURL1)
            return Tick.json()['ticker']['last']
        except Exception:
            print "NMCpriceBTC API error"
            return 0
    if NMCexchangeNamevardata == "two":
        try:
            Tick = requests.get(NMCexchangeURL2)
            return Tick.json()['last']
        except Exception:
            print "NMCpriceBTC API error"
            return 0
    if NMCexchangeNamevardata == "three":
        try:
            Tick = requests.get(NMCexchangeURL3)
            return Tick.json()["return"]["markets"]["NMC"]['lasttradeprice']
        except Exception:
            print "NMCpriceBTC API error"
            return 0

def NMCpriceBTCupdate():
    global NMCpriceBTCvardata
    NMCpriceBTCvardata.set(str.format("{0:.8f}", (float(NMCpriceBTC()))))
    root.after(UpdateInterval, NMCpriceBTCupdate)


# Calculate and Update with Price Average DATA for Namecoin price in USD
def NMCpriceUSD():
    NMCpriceUSD = float(NMCpriceBTCvardata.get()) * float(PriceAverageUSDvardata.get())
    return NMCpriceUSD

def NMCpriceUSDupdate():
    global NMCpriceUSDvardata
    NMCpriceUSDvardata.set(str.format("{0:.8f}", (float(NMCpriceUSD()))))
    root.after(UpdateInterval, NMCpriceUSDupdate)


# Calculate and Update my Namecoin Value in USD
def MyNMCValueUSD():
    global NMCpriceUSDvardata
    MyNMCValueUSD = float(NMCpriceUSDvardata.get()) * float(MyNMCvardata.get())
    return MyNMCValueUSD

def MyNMCValueUSDupdate():
    global MyNMCValueUSDvardata
    MyNMCValueUSDvardata.set(str.format("{0:.2f}", (float(MyNMCValueUSD()))))
    root.after(UpdateInterval, MyNMCValueUSDupdate)


# Calculate and Update my Namecoin Value in BTC
def MyNMCValueBTC():
    MyNMCValueBTC = float(NMCpriceBTCvardata.get()) * float(MyNMCvardata.get())
    return MyNMCValueBTC

def MyNMCValueBTCupdate():
    global MyNMCValueBTCvardata
    MyNMCValueBTCvardata.set(str.format("{0:.8f}", (float(MyNMCValueBTC()))))
    root.after(UpdateInterval, MyNMCValueBTCupdate)


#Monero
# Import and Update API DATA for Monero price in BTC
def XMRexchangeNameUpdate(XMRexchangeNameValue):
    if XMRexchangeNameValue == XMRexchangeName1text:
        print XMRexchangeName1text
        global XMRexchangeNamevardata
        XMRexchangeNamevardata = "one"
        print XMRexchangeNamevardata
        XMRupdateALL()
    elif XMRexchangeNameValue == XMRexchangeName2text:
        print XMRexchangeName2text
        XMRexchangeNamevardata = "two"
        print XMRexchangeNamevardata
        XMRupdateALL()
    else:
        print XMRexchangeName3text
        XMRexchangeNamevardata = "three"
        print XMRexchangeNamevardata
        XMRupdateALL()

def XMRpriceBTC():
    if XMRexchangeNamevardata == "one":
        try:
            Tick = requests.get(XMRexchangeURL1)
            return Tick.json()['BTC_XMR']['last']
        except Exception:
            print "XMRpriceBTC API error"
            return 0
    if XMRexchangeNamevardata == "two":
        try:
            Tick = requests.get(XMRexchangeURL2)
            return Tick.json()['XMRBTC']['last']
        except Exception:
            print "XMRpriceBTC API error"
            return 0
    if XMRexchangeNamevardata == "three":
        try:
            Tick = requests.get(XMRexchangeURL3)
            return Tick.json()['last']
        except Exception:
            print "XMRpriceBTC API error"
            return 0

def XMRpriceBTCupdate():
    global XMRpriceBTCvardata
    XMRpriceBTCvardata.set(str.format("{0:.8f}", (float(XMRpriceBTC()))))
    root.after(UpdateInterval, XMRpriceBTCupdate)


# Calculate and Update with Price Average DATA for Monero price in USD
def XMRpriceUSD():
    XMRpriceUSD = float(XMRpriceBTCvardata.get()) * float(PriceAverageUSDvardata.get())
    return XMRpriceUSD

def XMRpriceUSDupdate():
    global XMRpriceUSDvardata
    XMRpriceUSDvardata.set(str.format("{0:.8f}", (float(XMRpriceUSD()))))
    root.after(UpdateInterval, XMRpriceUSDupdate)


# Calculate and Update my Monero Value in USD
def MyXMRValueUSD():
    global XMRpriceUSDvardata
    MyXMRValueUSD = float(XMRpriceUSDvardata.get()) * float(MyXMRvardata.get())
    return MyXMRValueUSD

def MyXMRValueUSDupdate():
    global MyXMRValueUSDvardata
    MyXMRValueUSDvardata.set(str.format("{0:.2f}", (float(MyXMRValueUSD()))))
    root.after(UpdateInterval, MyXMRValueUSDupdate)


# Calculate and Update my Monero Value in BTC
def MyXMRValueBTC():
    MyXMRValueBTC = float(XMRpriceBTCvardata.get()) * float(MyXMRvardata.get())
    return MyXMRValueBTC

def MyXMRValueBTCupdate():
    global MyXMRValueBTCvardata
    MyXMRValueBTCvardata.set(str.format("{0:.8f}", (float(MyXMRValueBTC()))))
    root.after(UpdateInterval, MyXMRValueBTCupdate)




#BitShares
# Import and Update API DATA for BitShares price in BTC
def BTSexchangeNameUpdate(BTSexchangeNameValue):
    if BTSexchangeNameValue == BTSexchangeName1text:
        print BTSexchangeName1text
        global BTSexchangeNamevardata
        BTSexchangeNamevardata = "one"
        print BTSexchangeNamevardata
        BTSupdateALL()
    elif BTSexchangeNameValue == BTSexchangeName2text:
        print BTSexchangeName2text
        BTSexchangeNamevardata = "two"
        print BTSexchangeNamevardata
        BTSupdateALL()
    else:
        print BTSexchangeName3text
        BTSexchangeNamevardata = "three"
        print BTSexchangeNamevardata
        BTSupdateALL()

def BTSpriceBTC():
    if BTSexchangeNamevardata == "one":
        try:
            Tick = requests.get(BTSexchangeURL1)
            return Tick.json()['last']
        except Exception:
            print "BTSpriceBTC API error"
            return 0
    if BTSexchangeNamevardata == "two":
        try:
            Tick = requests.get(BTSexchangeURL2)
            print Tick
            print BTSexchangeURL2
            print Tick.json
            return Tick.json()["ticker"]["last"]
        except Exception as Err:
            print Err
            print "BTSpriceBTC API error"
            return 0
    if BTSexchangeNamevardata == "three":
        try:
            Tick = requests.get(BTSexchangeURL3)
            return Tick.json()['BTC_BTSX']['last']
        except Exception as Err:
            print Err
            print "BTSpriceBTC API error"
            return 0

def BTSpriceBTCupdate():
    global BTSpriceBTCvardata
    BTSpriceBTCvardata.set(str.format("{0:.8f}", (float(BTSpriceBTC()))))
    root.after(UpdateInterval, BTSpriceBTCupdate)


# Calculate and Update with Price Average DATA for BitShares price in USD
def BTSpriceUSD():
    BTSpriceUSD = float(BTSpriceBTCvardata.get()) * float(PriceAverageUSDvardata.get())
    return BTSpriceUSD

def BTSpriceUSDupdate():
    global BTSpriceUSDvardata
    BTSpriceUSDvardata.set(str.format("{0:.8f}", (float(BTSpriceUSD()))))
    root.after(UpdateInterval, BTSpriceUSDupdate)


# Calculate and Update my BitShares Value in USD
def MyBTSValueUSD():
    global BTSpriceUSDvardata
    MyBTSValueUSD = float(BTSpriceUSDvardata.get()) * float(MyBTSvardata.get())
    return MyBTSValueUSD

def MyBTSValueUSDupdate():
    global MyBTSValueUSDvardata
    MyBTSValueUSDvardata.set(str.format("{0:.2f}", (float(MyBTSValueUSD()))))
    root.after(UpdateInterval, MyBTSValueUSDupdate)


# Calculate and Update my BitShares Value in BTC
def MyBTSValueBTC():
    MyBTSValueBTC = float(BTSpriceBTCvardata.get()) * float(MyBTSvardata.get())
    return MyBTSValueBTC

def MyBTSValueBTCupdate():
    global MyBTSValueBTCvardata
    MyBTSValueBTCvardata.set(str.format("{0:.8f}", (float(MyBTSValueBTC()))))
    root.after(UpdateInterval, MyBTSValueBTCupdate)




#FAIRCOIN
# Import and Update API DATA for Faircoin price in BTC
def FAIRexchangeNameUpdate(FAIRexchangeNameValue):
    if FAIRexchangeNameValue == FAIRexchangeName1text:
        print FAIRexchangeName1text
        global FAIRexchangeNamevardata
        FAIRexchangeNamevardata = "one"
        print FAIRexchangeNamevardata
        FAIRupdateALL()
    elif FAIRexchangeNameValue == FAIRexchangeName2text:
        print FAIRexchangeName2text
        FAIRexchangeNamevardata = "two"
        print FAIRexchangeNamevardata
        FAIRupdateALL()
    else:
        print FAIRexchangeName3text
        FAIRexchangeNamevardata = "three"
        print FAIRexchangeNamevardata
        FAIRupdateALL()

def FAIRpriceBTC():
    if FAIRexchangeNamevardata == "one":
        try:
            Tick = requests.get(FAIRexchangeURL1)
            print Tick
            print Tick.json()
            return Tick.json()['result']['Last']
        except Exception as Err:
            print "FAIRpriceBTC API error"
            print FAIRexchangeURL1
            print Err
            return 0
    if FAIRexchangeNamevardata == "two":
        try:
            Tick = requests.get(FAIRexchangeURL2, verify=False)
            return Tick.json()['[last_price]']
        except Exception as Err:
            print "FAIRpriceBTC API error"
            print FAIRexchangeURL2
            print Err
            return 0
    if FAIRexchangeNamevardata == "three":
        try:
            Tick = requests.get(FAIRexchangeURL3)
            print Tick
            print Tick.json()["fair_btc"[["price"]]]
            return Tick.json()["fair_btc"[["price"]]]
        except Exception as Err:
            print "FAIRpriceBTC API error"
            print Err
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
    MyFAIRValueUSD = float(FAIRpriceUSDvardata.get()) * float(MyFAIRvardata.get())
    return MyFAIRValueUSD

def MyFAIRValueUSDupdate():
    global MyFAIRValueUSDvardata
    MyFAIRValueUSDvardata.set(str.format("{0:.2f}", (float(MyFAIRValueUSD()))))
    root.after(UpdateInterval, MyFAIRValueUSDupdate)


# Calculate and Update my Faircoin Value in BTC
def MyFAIRValueBTC():
    MyFAIRValueBTC = float(FAIRpriceBTCvardata.get()) * float(MyFAIRvardata.get())
    return MyFAIRValueBTC

def MyFAIRValueBTCupdate():
    global MyFAIRValueBTCvardata
    MyFAIRValueBTCvardata.set(str.format("{0:.8f}", (float(MyFAIRValueBTC()))))
    root.after(UpdateInterval, MyFAIRValueBTCupdate)



#TOTAL
# Calculate and Update my Total Value in USD
def MyTotalValueUSD():
    MyTotalValueUSD = float(MyBTCValuevardata.get()) + float(MyBLKValueUSDvardata.get()) + float(MyLTCValueUSDvardata.get()) + float(MyDOGEValueUSDvardata.get()) + float(MyDRKValueUSDvardata.get()) + float(MyPPCValueUSDvardata.get()) + float(MyNXTValueUSDvardata.get()) + float(MyXCPValueUSDvardata.get()) + float(MyNMCValueUSDvardata.get()) + float(MyXMRValueUSDvardata.get()) + float(MyFAIRValueUSDvardata.get())
    return MyTotalValueUSD

def MyTotalValueUSDupdate():
    global MyTotalValueUSDvardata
    MyTotalValueUSDvardata.set(str.format("{0:.2f}", (float(MyTotalValueUSD()))))
    root.after(UpdateInterval, MyTotalValueUSDupdate)


# Calculate and Update my Total Value in BTC
def MyTotalValueBTC():
    MyTotalValueBTC = MyBTC + float(MyBLKValueBTCvardata.get()) + float(MyLTCValueBTCvardata.get()) + float(MyDOGEValueBTCvardata.get()) + float(MyDRKValueBTCvardata.get()) + float(MyPPCValueBTCvardata.get()) + float(MyNXTValueBTCvardata.get()) + float(MyXCPValueBTCvardata.get()) + float(MyNMCValueBTCvardata.get()) + float(MyXMRValueBTCvardata.get()) + float(MyBTSValueBTCvardata.get()) + float(MyFAIRValueBTCvardata.get())
    return MyTotalValueBTC

def MyTotalValueBTCupdate():
    global MyTotalValueBTCvardata
    MyTotalValueBTCvardata.set(str.format("{0:.8}", (float(MyTotalValueBTC()))))
    root.after(UpdateInterval, MyTotalValueBTCupdate)



# Update UpdateInterval
def UpdateIntervalSecupdate():
    global UpdateInterval
    UpdateInterval = UpdateIntervalSec * 1000


def UpdateIntervalSecCallback():
    global UpdateIntervalSec
    global UpdateIntervalSeclabeldata
    UpdateIntervalSec = int(UpdateIntervalSecvardata.get())
    UpdateIntervalSecupdate()
    print UpdateIntervalSec
    UpdateIntervalSeclabeldata = Label(app, text="                         ", relief=FLAT, font=(TextFontType, TextFontSize), bg=TextBackgroundColor, fg=TextForegroundColor).grid(row=103, column=BTCUSDcol)
    UpdateIntervalSeclabeldata = Label(app, text=str(UpdateIntervalSec) + str(" sec"), relief=FLAT, font=(TextFontType, TextFontSize), bg=TextBackgroundColor, fg=TextForegroundColor).grid(row=103, column=BTCUSDcol)
    return UpdateIntervalSec


# .......... My COINS Update ..........
# My Bitcoin Update
def MyBTCupdate():
    global MyBTC
    MyBTC = float(MyBTCvardata.get())
    MyBTCValueUSDupdate()
    MyTotalValueUSDupdate()
    print MyBTC
    return MyBTC

# My Blackcoin Update
def MyBLKupdate():
    global MyBLK
    MyBLK = float(MyBLKvardata.get())
    BLKpriceBTCupdate()
    BLKpriceUSDupdate()
    MyBLKValueUSDupdate()
    MyBLKValueBTCupdate()
    MyTotalValueUSDupdate()
    MyTotalValueBTCupdate()
    print MyBLK
    return MyBLK

# My Litecoin Update
def MyLTCupdate():
    global MyLTC
    MyLTC = float(MyLTCvardata.get())
    LTCpriceBTCupdate()
    LTCpriceUSDupdate()
    MyLTCValueUSDupdate()
    MyLTCValueBTCupdate()
    MyTotalValueUSDupdate()
    MyTotalValueBTCupdate()
    print MyLTC
    return MyLTC

# My DOGE Update
def MyDOGEupdate():
    global MyDOGE
    MyDOGE = float(MyDOGEvardata.get())
    DOGEpriceBTCupdate()
    DOGEpriceUSDupdate()
    MyDOGEValueUSDupdate()
    MyDOGEValueBTCupdate()
    MyTotalValueUSDupdate()
    MyTotalValueBTCupdate()
    print MyDOGE
    return MyDOGE

# My Darkcoin Update
def MyDRKupdate():
    global MyDRK
    MyDRK = float(MyDRKvardata.get())
    DRKpriceBTCupdate()
    DRKpriceUSDupdate()
    MyDRKValueUSDupdate()
    MyDRKValueBTCupdate()
    MyTotalValueUSDupdate()
    MyTotalValueBTCupdate()
    print MyDRK
    return MyDRK

# My Peercoin Update
def MyPPCupdate():
    global MyPPC
    MyPPC = float(MyPPCvardata.get())
    PPCpriceBTCupdate()
    PPCpriceUSDupdate()
    MyPPCValueUSDupdate()
    MyPPCValueBTCupdate()
    MyTotalValueUSDupdate()
    MyTotalValueBTCupdate()
    print MyPPC
    return MyPPC

# My NXTcoin Update
def MyNXTupdate():
    global MyNXT
    MyNXT = float(MyNXTvardata.get())
    NXTpriceBTCupdate()
    NXTpriceUSDupdate()
    MyNXTValueUSDupdate()
    MyNXTValueBTCupdate()
    MyTotalValueUSDupdate()
    MyTotalValueBTCupdate()
    print MyNXT
    return MyNXT

# My Counterparty Update
def MyXCPupdate():
    global MyXCP
    MyXCP = float(MyXCPvardata.get())
    XCPpriceBTCupdate()
    XCPpriceUSDupdate()
    MyXCPValueUSDupdate()
    MyXCPValueBTCupdate()
    MyTotalValueUSDupdate()
    MyTotalValueBTCupdate()
    print MyXCP
    return MyXCP

# My Namecoin Update
def MyNMCupdate():
    global MyNMC
    MyNMC = float(MyNMCvardata.get())
    NMCpriceBTCupdate()
    NMCpriceUSDupdate()
    MyNMCValueUSDupdate()
    MyNMCValueBTCupdate()
    MyTotalValueUSDupdate()
    MyTotalValueBTCupdate()
    print MyNMC
    return MyNMC

# My Monero Update
def MyXMRupdate():
    global MyXMR
    MyXMR = float(MyXMRvardata.get())
    XMRpriceBTCupdate()
    XMRpriceUSDupdate()
    MyXMRValueUSDupdate()
    MyXMRValueBTCupdate()
    MyTotalValueUSDupdate()
    MyTotalValueBTCupdate()
    print MyXMR
    return MyXMR

# My BitShares Update
def MyBTSupdate():
    global MyBTS
    MyBTS = float(MyBTSvardata.get())
    BTSpriceBTCupdate()
    BTSpriceUSDupdate()
    MyBTSValueUSDupdate()
    MyBTSValueBTCupdate()
    MyTotalValueUSDupdate()
    MyTotalValueBTCupdate()
    print MyBTS
    return MyBTS

# My Faircoin Update
def MyFAIRupdate():
    global MyFAIR
    MyFAIR = float(MyFAIRvardata.get())
    FAIRpriceBTCupdate()
    FAIRpriceUSDupdate()
    MyFAIRValueUSDupdate()
    MyFAIRValueBTCupdate()
    MyTotalValueUSDupdate()
    MyTotalValueBTCupdate()
    print MyFAIR
    return MyFAIR


# .......... UPDATE ALL..........
# Bitcoin Update ALL
def BTCupdateALL():
        bitstampUSDupdate()
        btceUSDupdate()
        coinbaseUSDupdate()
        krakenUSDupdate()
        bitfinexUSDupdate()
        cryptsyUSDupdate()
        localbitcoinsUSDupdate()
        MyBTCValueUSDupdate()
        BTCpriceUSDdataUpdate()
        MyTotalValueUSDupdate()

# Blackcoin Update ALL
def BLKupdateALL():
        BLKpriceBTCupdate()
        BLKpriceUSDupdate()
        MyBLKValueBTCupdate()
        MyBLKValueUSDupdate()
        MyTotalValueBTCupdate()
        MyTotalValueUSDupdate()

# Litecoin Update ALL
def LTCupdateALL():
        LTCpriceBTCupdate()
        LTCpriceUSDupdate()
        MyLTCValueBTCupdate()
        MyLTCValueUSDupdate()
        MyTotalValueBTCupdate()
        MyTotalValueUSDupdate()

# Dogecoin Update ALL
def DOGEupdateALL():
        DOGEpriceBTCupdate()
        DOGEpriceUSDupdate()
        MyDOGEValueBTCupdate()
        MyDOGEValueUSDupdate()
        MyTotalValueBTCupdate()
        MyTotalValueUSDupdate()

# Darkcoin Update ALL
def DRKupdateALL():
        DRKpriceBTCupdate()
        DRKpriceUSDupdate()
        MyDRKValueBTCupdate()
        MyDRKValueUSDupdate()
        MyTotalValueBTCupdate()
        MyTotalValueUSDupdate()

# Peercoin Update ALL
def PPCupdateALL():
        PPCpriceBTCupdate()
        PPCpriceUSDupdate()
        MyPPCValueBTCupdate()
        MyPPCValueUSDupdate()
        MyTotalValueBTCupdate()
        MyTotalValueUSDupdate()

# NXTcoin Update ALL
def NXTupdateALL():
        NXTpriceBTCupdate()
        NXTpriceUSDupdate()
        MyNXTValueBTCupdate()
        MyNXTValueUSDupdate()
        MyTotalValueBTCupdate()
        MyTotalValueUSDupdate()

# Counterparty Update ALL
def XCPupdateALL():
        XCPpriceBTCupdate()
        XCPpriceUSDupdate()
        MyXCPValueBTCupdate()
        MyXCPValueUSDupdate()
        MyTotalValueBTCupdate()
        MyTotalValueUSDupdate()

# Namecoin Update ALL
def NMCupdateALL():
        NMCpriceBTCupdate()
        NMCpriceUSDupdate()
        MyNMCValueBTCupdate()
        MyNMCValueUSDupdate()
        MyTotalValueBTCupdate()
        MyTotalValueUSDupdate()

# Monero Update ALL
def XMRupdateALL():
        XMRpriceBTCupdate()
        XMRpriceUSDupdate()
        MyXMRValueBTCupdate()
        MyXMRValueUSDupdate()
        MyTotalValueBTCupdate()
        MyTotalValueUSDupdate()

# BitShares Update ALL
def BTSupdateALL():
        BTSpriceBTCupdate()
        BTSpriceUSDupdate()
        MyBTSValueBTCupdate()
        MyBTSValueUSDupdate()
        MyTotalValueBTCupdate()
        MyTotalValueUSDupdate()

# Faircoin Update ALL
def FAIRupdateALL():
        FAIRpriceBTCupdate()
        FAIRpriceUSDupdate()
        MyFAIRValueBTCupdate()
        MyFAIRValueUSDupdate()
        MyTotalValueBTCupdate()
        MyTotalValueUSDupdate()



#Update ALL BUTTON
def updateALLvalue():
    MyBTCValueUSDupdate()
    MyBLKValueUSDupdate()
    MyBLKValueBTCupdate()
    MyLTCValueUSDupdate()
    MyLTCValueBTCupdate()
    MyDOGEValueUSDupdate()
    MyDOGEValueBTCupdate()
    MyDRKValueUSDupdate()
    MyDRKValueBTCupdate()
    MyPPCValueUSDupdate()
    MyPPCValueBTCupdate()
    MyNXTValueUSDupdate()
    MyNXTValueBTCupdate()
    MyXCPValueUSDupdate()
    MyXCPValueBTCupdate()
    MyNMCValueUSDupdate()
    MyNMCValueBTCupdate()
    MyXMRValueUSDupdate()
    MyXMRValueBTCupdate()
    MyBTSValueUSDupdate()
    MyBTSValueBTCupdate()
    MyFAIRValueUSDupdate()
    MyFAIRValueBTCupdate()
    MyTotalValueUSDupdate()
    MyTotalValueBTCupdate()




# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! WINDOW START !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
class Window(Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("Crypto")
        self.pack(fill=BOTH, expand=1)
        # Quit Button
        quitButton = Button(self, text="Quit", command=self.client_exit, bg=ButtonBackGroundColor, fg=ButtonForegroundColor)
        quitButton.grid(row=0, column=0)
        # Menu
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


# -------------------------- Window Loop Start --------------------------
root = Tk()
#root.geometry("1400x600")
app = Window(root)
root.title("CryptTicker")
app.config (bg=AppWindowBackgroundColor)


#Coin Images
BTCimage = Text(app, height=3.1, width=6, bg=COINSbackgroundColor, bd=0)
BitcoinImage = PhotoImage(file='./images/BitcoinImage.gif')
BTCimage.image_create(END, image=BitcoinImage)
BTCimage.grid(row=1, column=COINSimagecol, rowspan=2)

BLKimage = Text(app, height=3.1, width=6, bg=COINSbackgroundColor, bd=0)
BlackcoinImage = PhotoImage(file='./images/BlackcoinImage.gif')
BLKimage.image_create(END, image=BlackcoinImage)
BLKimage.grid(row=BLKrowtext, column=COINSimagecol, rowspan=2)

LTCimage = Text(app, height=3.1, width=6, bg=COINSbackgroundColor, bd=0)
LitecoinImage = PhotoImage(file='./images/LitecoinImage.gif')
LTCimage.image_create(END, image=LitecoinImage)
LTCimage.grid(row=LTCrowtext, column=COINSimagecol, rowspan=2)

DOGEimage = Text(app, height=3.1, width=6, bg=COINSbackgroundColor, bd=0)
DogecoinImage = PhotoImage(file='./images/DogecoinImage.gif')
DOGEimage.image_create(END, image=DogecoinImage)
DOGEimage.grid(row=DOGErowtext, column=COINSimagecol, rowspan=2)

DRKimage = Text(app, height=3.1, width=6, bg=COINSbackgroundColor, bd=0)
DarkcoinImage = PhotoImage(file='./images/DarkcoinImage.gif')
DRKimage.image_create(END, image=DarkcoinImage)
DRKimage.grid(row=DRKrowtext, column=COINSimagecol, rowspan=2)

PPCimage = Text(app, height=3.1, width=6, bg=COINSbackgroundColor, bd=0)
PeercoinImage = PhotoImage(file='./images/PeercoinImage.gif')
PPCimage.image_create(END, image=PeercoinImage)
PPCimage.grid(row=PPCrowtext, column=COINSimagecol, rowspan=2)

NXTimage = Text(app, height=3.1, width=6, bg=COINSbackgroundColor, bd=0)
NXTcoinImage = PhotoImage(file='./images/NXTcoinImage.gif')
NXTimage.image_create(END, image=NXTcoinImage)
NXTimage.grid(row=NXTrowtext, column=COINSimagecol, rowspan=2)

XCPimage = Text(app, height=3.1, width=6, bg=COINSbackgroundColor, bd=0)
CounterpartyImage = PhotoImage(file='./images/CounterpartyImage.gif')
XCPimage.image_create(END, image=CounterpartyImage)
XCPimage.grid(row=XCProwtext, column=COINSimagecol, rowspan=2)

NMCimage = Text(app, height=3.1, width=6, bg=COINSbackgroundColor, bd=0)
NamecoinImage = PhotoImage(file='./images/NamecoinImage.gif')
NMCimage.image_create(END, image=NamecoinImage)
NMCimage.grid(row=NMCrowtext, column=COINSimagecol, rowspan=2)

XMRimage = Text(app, height=3.1, width=6, bg=COINSbackgroundColor, bd=0)
MoneroImage = PhotoImage(file='./images/MoneroImage.gif')
XMRimage.image_create(END, image=MoneroImage)
XMRimage.grid(row=XMRrowtext, column=COINSimagecol, rowspan=2)

BTSimage = Text(app, height=3.1, width=6, bg=COINSbackgroundColor, bd=0)
BitSharesImage = PhotoImage(file='./images/BitSharesImage.gif')
BTSimage.image_create(END, image=BitSharesImage)
BTSimage.grid(row=BTSrowtext, column=COINSimagecol, rowspan=2)

FAIRimage = Text(app, height=3.1, width=6, bg=COINSbackgroundColor, bd=0)
FaircoinImage = PhotoImage(file='./images/FaircoinImage.gif')
FAIRimage.image_create(END, image=FaircoinImage)
FAIRimage.grid(row=FAIRrowtext, column=COINSimagecol, rowspan=2)


#Update Interval Rate Entry with Button
UpdateIntervalSecvartext = StringVar()
UpdateIntervalSeclabeltext = Label(app, textvariable=UpdateIntervalSecvartext, relief=FLAT, font=(TextFontType, TextFontSize), bg=TextBackgroundColor, fg=TextForegroundColor)
UpdateIntervalSecvartext.set(UpdateIntervalSectext)
UpdateIntervalSeclabeltext.grid(row=100, column=BTCUSDcol)

UpdateIntervalSecvardata = StringVar()
UpdateIntervalSecvardata.set(UpdateIntervalSec)
UpdateIntervalSecentry = Entry(app, textvariable=UpdateIntervalSecvardata, relief=RAISED, font=(DataFontType, DataFontSize), width=9, borderwidth=3, justify=CENTER, bg=EntryBackgroundColor, fg=EntryForegroundColor)
UpdateIntervalSecentry.grid(row=101, column=BTCUSDcol)

UpdateIntervalSecCallbackbutton = Button(app, text='Update', command=UpdateIntervalSecCallback, bg=ButtonBackGroundColor, fg=ButtonForegroundColor).grid(row=102, column=BTCUSDcol)

UpdateIntervalSeclabeldata = Label(app, text=str(UpdateIntervalSec) + str(" sec"), relief=FLAT, font=(TextFontType, TextFontSize), bg=TextBackgroundColor, fg=TextForegroundColor).grid(row=103, column=BTCUSDcol)


# .................... Exchange Name ....................
#Exchange Name display TITLE
exchangeNamevartext = StringVar()
exchangeNamelabeltext = Label(app, textvariable=exchangeNamevartext, relief=FLAT, font=(TextFontType, TextFontSize), bg=TextBackgroundColor, fg=TextForegroundColor)
exchangeNamevartext.set(exchangeNametext)
exchangeNamelabeltext.grid(row=exchangeNamerowtext, column=exchangeNamecol)

#Bitcoin Exchange Name
BTCexchangeNameChoices = [BTCexchangeName0text, BTCexchangeName1text, BTCexchangeName2text, BTCexchangeName3text, BTCexchangeName4text, BTCexchangeName5text, BTCexchangeName6text, BTCexchangeName7text]
BTCexchangeNamevartext = StringVar(app)
if BTCexchangeNamevardata == "priceaverage":
    BTCexchangeNamevartext.set(BTCexchangeNameChoices[0])
if BTCexchangeNamevardata == "one":
    BTCexchangeNamevartext.set(BTCexchangeNameChoices[1])
if BTCexchangeNamevardata == "two":
    BTCexchangeNamevartext.set(BTCexchangeNameChoices[2])
if BTCexchangeNamevardata == "three":
    BTCexchangeNamevartext.set(BTCexchangeNameChoices[3])
if BTCexchangeNamevardata == "four":
    BTCexchangeNamevartext.set(BTCexchangeNameChoices[4])
if BTCexchangeNamevardata == "five":
    BTCexchangeNamevartext.set(BTCexchangeNameChoices[5])
if BTCexchangeNamevardata == "six":
    BTCexchangeNamevartext.set(BTCexchangeNameChoices[6])
if BTCexchangeNamevardata == "seven":
    BTCexchangeNamevartext.set(BTCexchangeNameChoices[7])
option = OptionMenu(app, BTCexchangeNamevartext, *BTCexchangeNameChoices, command=BTCexchangeNameUpdate)
option.config(relief=FLAT, font=(TextFontType, TextFontSize), bg=TextBackgroundColor, fg=TextForegroundColor, activebackground=ExchangeNameActiveBackgroundColor, activeforeground=TextForegroundColor)
option.grid(row=BTCrowdata, column=exchangeNamecol)

#Blackcoin Exchange Name
BLKexchangeNameChoices = [BLKexchangeName1text, BLKexchangeName2text, BLKexchangeName3text]
BLKexchangeNamevartext = StringVar(app)
if BLKexchangeNamevardata == "one":
    BLKexchangeNamevartext.set(BLKexchangeNameChoices[0])
if BLKexchangeNamevardata == "two":
    BLKexchangeNamevartext.set(BLKexchangeNameChoices[1])
if BLKexchangeNamevardata == "three":
    BLKexchangeNamevartext.set(BLKexchangeNameChoices[2])
option = OptionMenu(app, BLKexchangeNamevartext, *BLKexchangeNameChoices, command=BLKexchangeNameUpdate)
option.config(relief=FLAT, font=(TextFontType, TextFontSize), bg=TextBackgroundColor, fg=TextForegroundColor, activebackground=ExchangeNameActiveBackgroundColor, activeforeground=TextForegroundColor)
option.grid(row=BLKrowdata, column=exchangeNamecol)

#Litecoin Exchange Name
LTCexchangeNameChoices = [LTCexchangeName1text, LTCexchangeName2text, LTCexchangeName3text]
LTCexchangeNamevartext = StringVar(app)
if LTCexchangeNamevardata == "one":
    LTCexchangeNamevartext.set(LTCexchangeNameChoices[0])
if LTCexchangeNamevardata == "two":
    LTCexchangeNamevartext.set(LTCexchangeNameChoices[1])
if LTCexchangeNamevardata == "three":
    LTCexchangeNamevartext.set(LTCexchangeNameChoices[2])
option = OptionMenu(app, LTCexchangeNamevartext, *LTCexchangeNameChoices, command=LTCexchangeNameUpdate)
option.config(relief=FLAT, font=(TextFontType, TextFontSize), bg=TextBackgroundColor, fg=TextForegroundColor, activebackground=ExchangeNameActiveBackgroundColor, activeforeground=TextForegroundColor)
option.grid(row=LTCrowdata, column=exchangeNamecol)

#Dogecoin Exchange Name
DOGEexchangeNameChoices = [DOGEexchangeName1text, DOGEexchangeName2text, DOGEexchangeName3text]
DOGEexchangeNamevartext = StringVar(app)
if DOGEexchangeNamevardata == "one":
    DOGEexchangeNamevartext.set(DOGEexchangeNameChoices[0])
if DOGEexchangeNamevardata == "two":
    DOGEexchangeNamevartext.set(DOGEexchangeNameChoices[1])
if DOGEexchangeNamevardata == "three":
    DOGEexchangeNamevartext.set(DOGEexchangeNameChoices[2])
option = OptionMenu(app, DOGEexchangeNamevartext, *DOGEexchangeNameChoices, command=DOGEexchangeNameUpdate)
option.config(relief=FLAT, font=(TextFontType, TextFontSize), bg=TextBackgroundColor, fg=TextForegroundColor, activebackground=ExchangeNameActiveBackgroundColor, activeforeground=TextForegroundColor)
option.grid(row=DOGErowdata, column=exchangeNamecol)

#Darkcoin Exchange Name
DRKexchangeNameChoices = [DRKexchangeName1text, DRKexchangeName2text, DRKexchangeName3text]
DRKexchangeNamevartext = StringVar(app)
if DRKexchangeNamevardata == "one":
    DRKexchangeNamevartext.set(DRKexchangeNameChoices[0])
if DRKexchangeNamevardata == "two":
    DRKexchangeNamevartext.set(DRKexchangeNameChoices[1])
if DRKexchangeNamevardata == "three":
    DRKexchangeNamevartext.set(DRKexchangeNameChoices[2])
option = OptionMenu(app, DRKexchangeNamevartext, *DRKexchangeNameChoices, command=DRKexchangeNameUpdate)
option.config(relief=FLAT, font=(TextFontType, TextFontSize), bg=TextBackgroundColor, fg=TextForegroundColor, activebackground=ExchangeNameActiveBackgroundColor, activeforeground=TextForegroundColor)
option.grid(row=DRKrowdata, column=exchangeNamecol)

#Peercoin Exchange Name
PPCexchangeNameChoices = [PPCexchangeName1text, PPCexchangeName2text, PPCexchangeName3text]
PPCexchangeNamevartext = StringVar(app)
if PPCexchangeNamevardata == "one":
    PPCexchangeNamevartext.set(PPCexchangeNameChoices[0])
if PPCexchangeNamevardata == "two":
    PPCexchangeNamevartext.set(PPCexchangeNameChoices[1])
if PPCexchangeNamevardata == "three":
    PPCexchangeNamevartext.set(PPCexchangeNameChoices[2])
option = OptionMenu(app, PPCexchangeNamevartext, *PPCexchangeNameChoices, command=PPCexchangeNameUpdate)
option.config(relief=FLAT, font=(TextFontType, TextFontSize), bg=TextBackgroundColor, fg=TextForegroundColor, activebackground=ExchangeNameActiveBackgroundColor, activeforeground=TextForegroundColor)
option.grid(row=PPCrowdata, column=exchangeNamecol)

#NXTcoin Exchange Name
NXTexchangeNameChoices = [NXTexchangeName1text, NXTexchangeName2text, NXTexchangeName3text]
NXTexchangeNamevartext = StringVar(app)
if NXTexchangeNamevardata == "one":
    NXTexchangeNamevartext.set(NXTexchangeNameChoices[0])
if NXTexchangeNamevardata == "two":
    NXTexchangeNamevartext.set(NXTexchangeNameChoices[1])
if NXTexchangeNamevardata == "three":
    NXTexchangeNamevartext.set(NXTexchangeNameChoices[2])
option = OptionMenu(app, NXTexchangeNamevartext, *NXTexchangeNameChoices, command=NXTexchangeNameUpdate)
option.config(relief=FLAT, font=(TextFontType, TextFontSize), bg=TextBackgroundColor, fg=TextForegroundColor, activebackground=ExchangeNameActiveBackgroundColor, activeforeground=TextForegroundColor)
option.grid(row=NXTrowdata, column=exchangeNamecol)

#Counterparty Exchange Name
XCPexchangeNameChoices = [XCPexchangeName1text, XCPexchangeName2text, XCPexchangeName3text]
XCPexchangeNamevartext = StringVar(app)
if XCPexchangeNamevardata == "one":
    XCPexchangeNamevartext.set(XCPexchangeNameChoices[0])
if XCPexchangeNamevardata == "two":
    XCPexchangeNamevartext.set(XCPexchangeNameChoices[1])
if XCPexchangeNamevardata == "three":
    XCPexchangeNamevartext.set(XCPexchangeNameChoices[2])
option = OptionMenu(app, XCPexchangeNamevartext, *XCPexchangeNameChoices, command=XCPexchangeNameUpdate)
option.config(relief=FLAT, font=(TextFontType, TextFontSize), bg=TextBackgroundColor, fg=TextForegroundColor, activebackground=ExchangeNameActiveBackgroundColor, activeforeground=TextForegroundColor)
option.grid(row=XCProwdata, column=exchangeNamecol)

#Namecoin Exchange Name
NMCexchangeNameChoices = [NMCexchangeName1text, NMCexchangeName2text, NMCexchangeName3text]
NMCexchangeNamevartext = StringVar(app)
if NMCexchangeNamevardata == "one":
    NMCexchangeNamevartext.set(NMCexchangeNameChoices[0])
if NMCexchangeNamevardata == "two":
    NMCexchangeNamevartext.set(NMCexchangeNameChoices[1])
if NMCexchangeNamevardata == "three":
    NMCexchangeNamevartext.set(NMCexchangeNameChoices[2])
option = OptionMenu(app, NMCexchangeNamevartext, *NMCexchangeNameChoices, command=NMCexchangeNameUpdate)
option.config(relief=FLAT, font=(TextFontType, TextFontSize), bg=TextBackgroundColor, fg=TextForegroundColor, activebackground=ExchangeNameActiveBackgroundColor, activeforeground=TextForegroundColor)
option.grid(row=NMCrowdata, column=exchangeNamecol)

#Monero Exchange Name
XMRexchangeNameChoices = [XMRexchangeName1text, XMRexchangeName2text, XMRexchangeName3text]
XMRexchangeNamevartext = StringVar(app)
if XMRexchangeNamevardata == "one":
    XMRexchangeNamevartext.set(XMRexchangeNameChoices[0])
if XMRexchangeNamevardata == "two":
    XMRexchangeNamevartext.set(XMRexchangeNameChoices[1])
if XMRexchangeNamevardata == "three":
    XMRexchangeNamevartext.set(XMRexchangeNameChoices[2])
option = OptionMenu(app, XMRexchangeNamevartext, *XMRexchangeNameChoices, command=XMRexchangeNameUpdate)
option.config(relief=FLAT, font=(TextFontType, TextFontSize), bg=TextBackgroundColor, fg=TextForegroundColor, activebackground=ExchangeNameActiveBackgroundColor, activeforeground=TextForegroundColor)
option.grid(row=XMRrowdata, column=exchangeNamecol)

#BitShares Exchange Name
BTSexchangeNameChoices = [BTSexchangeName1text, BTSexchangeName2text, BTSexchangeName3text]
BTSexchangeNamevartext = StringVar(app)
if BTSexchangeNamevardata == "one":
    BTSexchangeNamevartext.set(BTSexchangeNameChoices[0])
if BTSexchangeNamevardata == "two":
    BTSexchangeNamevartext.set(BTSexchangeNameChoices[1])
if BTSexchangeNamevardata == "three":
    BTSexchangeNamevartext.set(BTSexchangeNameChoices[2])
option = OptionMenu(app, BTSexchangeNamevartext, *BTSexchangeNameChoices, command=BTSexchangeNameUpdate)
option.config(relief=FLAT, font=(TextFontType, TextFontSize), bg=TextBackgroundColor, fg=TextForegroundColor, activebackground=ExchangeNameActiveBackgroundColor, activeforeground=TextForegroundColor)
option.grid(row=BTSrowdata, column=exchangeNamecol)


#Faircoin Exchange Name
FAIRexchangeNameChoices = [FAIRexchangeName1text, FAIRexchangeName2text, FAIRexchangeName3text]
FAIRexchangeNamevartext = StringVar(app)
if FAIRexchangeNamevardata == "one":
    FAIRexchangeNamevartext.set(FAIRexchangeNameChoices[0])
if FAIRexchangeNamevardata == "two":
    FAIRexchangeNamevartext.set(FAIRexchangeNameChoices[1])
if FAIRexchangeNamevardata == "three":
    FAIRexchangeNamevartext.set(FAIRexchangeNameChoices[2])
option = OptionMenu(app, FAIRexchangeNamevartext, *FAIRexchangeNameChoices, command=FAIRexchangeNameUpdate)
option.config(relief=FLAT, font=(TextFontType, TextFontSize), bg=TextBackgroundColor, fg=TextForegroundColor, activebackground=ExchangeNameActiveBackgroundColor, activeforeground=TextForegroundColor)
option.grid(row=FAIRrowdata, column=exchangeNamecol)


# .................... DATA and TEXT ....................
#BITCOIN
# Display Data and Text for Bitcoin in USD
bitfinexUSDvartext = StringVar()
bitfinexUSDlabeltext = Label(app, textvariable=bitfinexUSDvartext, relief=FLAT, font=(TextFontType, TextFontSize), bg=TextBackgroundColor, fg=TextForegroundColor)
bitfinexUSDvartext.set(bitfinexUSDtext)
bitfinexUSDlabeltext.grid(row=bitfinexUSDrow, column=BTCUSDcol)
bitfinexUSDvardata = StringVar()
bitfinexUSDlabeldata = Label(app, textvariable=bitfinexUSDvardata, relief=RAISED, font=(DataFontType, DataFontSize), bg=DataBackgroundColor, fg=DataForegroundColor)
bitfinexUSDlabeldata.grid(row=bitfinexUSDrow + 1, column=BTCUSDcol)

bitstampUSDvartext = StringVar()
bitstampUSDlabeltext = Label(app, textvariable=bitstampUSDvartext, relief=FLAT, font=(TextFontType, TextFontSize), bg=TextBackgroundColor, fg=TextForegroundColor)
bitstampUSDvartext.set(bitstampUSDtext)
bitstampUSDlabeltext.grid(row=bitstampUSDrow, column=BTCUSDcol)
bitstampUSDvardata = StringVar()
bitstampUSDlabeldata = Label(app, textvariable=bitstampUSDvardata, relief=RAISED, font=(DataFontType, DataFontSize), bg=DataBackgroundColor, fg=DataForegroundColor)
bitstampUSDlabeldata.grid(row=bitstampUSDrow + 1, column=BTCUSDcol)

btceUSDvartext = StringVar()
btceUSDlabeltext = Label(app, textvariable=btceUSDvartext, relief=FLAT, font=(TextFontType, TextFontSize), bg=TextBackgroundColor, fg=TextForegroundColor)
btceUSDvartext.set(btceUSDtext)
btceUSDlabeltext.grid(row=btceUSDrow, column=BTCUSDcol)
btceUSDvardata = StringVar()
btceUSDlabeldata = Label(app, textvariable=btceUSDvardata, relief=RAISED, font=(DataFontType, DataFontSize), bg=DataBackgroundColor, fg=DataForegroundColor)
btceUSDlabeldata.grid(row=btceUSDrow + 1, column=BTCUSDcol)

coinbaseUSDvartext = StringVar()
coinbaseUSDlabeltext = Label(app, textvariable=coinbaseUSDvartext, relief=FLAT, font=(TextFontType, TextFontSize), bg=TextBackgroundColor, fg=TextForegroundColor)
coinbaseUSDvartext.set(coinbaseUSDtext)
coinbaseUSDlabeltext.grid(row=coinbaseUSDrow, column=BTCUSDcol)
coinbaseUSDvardata = StringVar()
coinbaseUSDlabeldata = Label(app, textvariable=coinbaseUSDvardata, relief=RAISED, font=(DataFontType, DataFontSize), bg=DataBackgroundColor, fg=DataForegroundColor)
coinbaseUSDlabeldata.grid(row=coinbaseUSDrow + 1, column=BTCUSDcol)

krakenUSDvartext = StringVar()
krakenUSDlabeltext = Label(app, textvariable=krakenUSDvartext, relief=FLAT, font=(TextFontType, TextFontSize), bg=TextBackgroundColor, fg=TextForegroundColor)
krakenUSDvartext.set(krakenUSDtext)
krakenUSDlabeltext.grid(row=krakenUSDrow, column=BTCUSDcol)
krakenUSDvardata = StringVar()
krakenUSDlabeldata = Label(app, textvariable=krakenUSDvardata, relief=RAISED, font=(DataFontType, DataFontSize), bg=DataBackgroundColor, fg=DataForegroundColor)
krakenUSDlabeldata.grid(row=krakenUSDrow + 1, column=BTCUSDcol)

cryptsyUSDvartext = StringVar()
cryptsyUSDlabeltext = Label(app, textvariable=cryptsyUSDvartext, relief=FLAT, font=(TextFontType, TextFontSize), bg=TextBackgroundColor, fg=TextForegroundColor)
cryptsyUSDvartext.set(cryptsyUSDtext)
cryptsyUSDlabeltext.grid(row=cryptsyUSDrow, column=BTCUSDcol)
cryptsyUSDvardata = StringVar()
cryptsyUSDlabeldata = Label(app, textvariable=cryptsyUSDvardata, relief=RAISED, font=(DataFontType, DataFontSize), bg=DataBackgroundColor, fg=DataForegroundColor)
cryptsyUSDlabeldata.grid(row=cryptsyUSDrow + 1, column=BTCUSDcol)

localbitcoinsUSDvartext = StringVar()
localbitcoinsUSDlabeltext = Label(app, textvariable=localbitcoinsUSDvartext, relief=FLAT, font=(TextFontType, TextFontSize), bg=TextBackgroundColor, fg=TextForegroundColor)
localbitcoinsUSDvartext.set(localbitcoinsUSDtext)
localbitcoinsUSDlabeltext.grid(row=localbitcoinsUSDrow, column=BTCUSDcol)
localbitcoinsUSDvardata = StringVar()
localbitcoinsUSDlabeldata = Label(app, textvariable=localbitcoinsUSDvardata, relief=RAISED, font=(DataFontType, DataFontSize), bg=DataBackgroundColor, fg=DataForegroundColor)
localbitcoinsUSDlabeldata.grid(row=localbitcoinsUSDrow + 1, column=BTCUSDcol)

#Price Average in USD
PriceAverageUSDvartext = StringVar()
PriceAverageUSDlabeltext = Label(app, textvariable=PriceAverageUSDvartext, relief=FLAT, font=(TextFontType, TextFontSize), bg=TextBackgroundColor, fg=TextForegroundColor)
PriceAverageUSDvartext.set(PriceAverageUSDtext)
PriceAverageUSDlabeltext.grid(row=1, column=BTCUSDcol)
PriceAverageUSDvardata = StringVar()
PriceAverageUSDlabeldata = Label(app, textvariable=PriceAverageUSDvardata, relief=RAISED, font=(DataFontType, DataFontSize), bg=DataBackgroundColor, fg=DataForegroundColor)
PriceAverageUSDlabeldata.grid(row=2, column=BTCUSDcol)


#Update ALL Bitcoin exchanges in USD and calculate Price Average
bitstampUSDupdate()
btceUSDupdate()
coinbaseUSDupdate()
krakenUSDupdate()
bitfinexUSDupdate()
cryptsyUSDupdate()
localbitcoinsUSDupdate()
PriceAverageUSDupdate()



# .................... MY COINS ....................
#BITCOIN
#MyBTC
MyBTCvartext = StringVar()
MyBTClabeltext = Label(app, textvariable=MyBTCvartext, relief=FLAT, font=(TextFontType, TextFontSize), bg=TextBackgroundColor, fg=TextForegroundColor)
MyBTCvartext.set(MyBTCtext)
MyBTClabeltext.grid(row=BTCrowtext, column=MyCOINScol)

MyBTCvardata = StringVar()
MyBTCvardata.set(MyBTC)
MyBTCentry = Entry(app, textvariable=MyBTCvardata, relief=RAISED, font=(DataFontType, DataFontSize), width=9, borderwidth=3, justify=CENTER, bg=EntryBackgroundColor, fg=EntryForegroundColor)
MyBTCentry.grid(row=BTCrowdata, column=MyCOINScol)

MyBTCupdatebutton = Button(app, text='Update NOW', command=MyBTCupdate, bg=ButtonBackGroundColor, fg=ButtonForegroundColor).grid(row=BTCrowdata, column=updateMyCOINScol)


# Display Data and Text for Bitcoin price in USD
BTCpriceUSDvartext = StringVar()
BTCpriceUSDlabeltext = Label(app, textvariable=BTCpriceUSDvartext, relief=FLAT, font=(TextFontType, TextFontSize), bg=TextBackgroundColor, fg=TextForegroundColor)
BTCpriceUSDvartext.set(BTCpriceUSDtext)
BTCpriceUSDlabeltext.grid(row=BTCrowtext, column=PriceUSDcol)
BTCpriceUSDvardata = StringVar()
BTCpriceUSDvardata = PriceAverageUSDvardata
BTCpriceUSDlabeldata = Label(app, textvariable=BTCpriceUSDvardata, relief=RAISED, font=(DataFontType, DataFontSize), bg=DataBackgroundColor, fg=DataForegroundColor)
BTCpriceUSDlabeldata.grid(row=BTCrowdata, column=PriceUSDcol)


#My BTC Value in USD
MyBTCValuevartext = StringVar()
MyBTCValuelabeltext = Label(app, textvariable=MyBTCValuevartext, relief=FLAT, font=(TextFontType, TextFontSize), bg=TextBackgroundColor, fg=TextForegroundColor)
MyBTCValuevartext.set(MyBTCValuetext)
MyBTCValuelabeltext.grid(row=BTCrowtext, column=ValueUSDcol)

MyBTCValuevardata = StringVar()
MyBTCValuelabeldata = Label(app, textvariable=MyBTCValuevardata, relief=RAISED, font=(DataFontType, DataFontSize), bg=DataBackgroundColor, fg=DataForegroundColor)
MyBTCValueUSDupdate()
MyBTCValuelabeldata.grid(row=BTCrowdata, column=ValueUSDcol)



#BLACKCOIN
#MyBLK
MyBLKvartext = StringVar()
MyBLKlabeltext = Label(app, textvariable=MyBLKvartext, relief=FLAT, font=(TextFontType, TextFontSize), bg=TextBackgroundColor, fg=TextForegroundColor)
MyBLKvartext.set(MyBLKtext)
MyBLKlabeltext.grid(row=BLKrowtext, column=MyCOINScol)

MyBLKvardata = StringVar()
MyBLKvardata.set(MyBLK)
MyBLKentry = Entry(app, textvariable=MyBLKvardata, relief=RAISED, font=(DataFontType, DataFontSize), width=9, borderwidth=3, justify=CENTER, bg=EntryBackgroundColor, fg=EntryForegroundColor)
MyBLKentry.grid(row=BLKrowdata, column=MyCOINScol)

MyBLKupdatebutton = Button(app, text='Update NOW', command=MyBLKupdate, bg=ButtonBackGroundColor, fg=ButtonForegroundColor).grid(row=BLKrowdata, column=updateMyCOINScol)


# Display Data and Text for Blackcoin price in BTC
BLKpriceBTCvartext = StringVar()
BLKpriceBTClabeltext = Label(app, textvariable=BLKpriceBTCvartext, relief=FLAT, font=(TextFontType, TextFontSize), bg=TextBackgroundColor, fg=TextForegroundColor)
BLKpriceBTCvartext.set(BLKpriceBTCtext)
BLKpriceBTClabeltext.grid(row=BLKrowtext, column=PriceBTCcol)
BLKpriceBTCvardata = StringVar()
BLKpriceBTClabeldata = Label(app, textvariable=BLKpriceBTCvardata, relief=RAISED, font=(DataFontType, DataFontSize), bg=DataBackgroundColor, fg=DataForegroundColor)
BLKpriceBTCupdate()
BLKpriceBTClabeldata.grid(row=BLKrowdata, column=PriceBTCcol)


# Display Data and Text for Blackcoin price in USD
BLKpriceUSDvartext = StringVar()
BLKpriceUSDlabeltext = Label(app, textvariable=BLKpriceUSDvartext, relief=FLAT, font=(TextFontType, TextFontSize), bg=TextBackgroundColor, fg=TextForegroundColor)
BLKpriceUSDvartext.set(BLKpriceUSDtext)
BLKpriceUSDlabeltext.grid(row=BLKrowtext, column=PriceUSDcol)
BLKpriceUSDvardata = StringVar()
BLKpriceUSDlabeldata = Label(app, textvariable=BLKpriceUSDvardata, relief=RAISED, font=(DataFontType, DataFontSize), bg=DataBackgroundColor, fg=DataForegroundColor)
BLKpriceUSDupdate()
BLKpriceUSDlabeldata.grid(row=BLKrowdata, column=PriceUSDcol)


#My BLK Value in BTC
MyBLKValueBTCvartext = StringVar()
MyBLKValueBTClabeltext = Label(app, textvariable=MyBLKValueBTCvartext, relief=FLAT, font=(TextFontType, TextFontSize), bg=TextBackgroundColor, fg=TextForegroundColor)
MyBLKValueBTCvartext.set(MyBLKValueBTCtext)
MyBLKValueBTClabeltext.grid(row=BLKrowtext, column=ValueBTCcol)

MyBLKValueBTCvardata = StringVar()
MyBLKValueBTClabeldata = Label(app, textvariable=MyBLKValueBTCvardata, relief=RAISED, font=(DataFontType, DataFontSize), bg=DataBackgroundColor, fg=DataForegroundColor)
MyBLKValueBTCupdate()
MyBLKValueBTClabeldata.grid(row=BLKrowdata, column=ValueBTCcol)


#My BLK Value in USD
MyBLKValueUSDvartext = StringVar()
MyBLKValueUSDlabeltext = Label(app, textvariable=MyBLKValueUSDvartext, relief=FLAT, font=(TextFontType, TextFontSize), bg=TextBackgroundColor, fg=TextForegroundColor)
MyBLKValueUSDvartext.set(MyBLKValueUSDtext)
MyBLKValueUSDlabeltext.grid(row=BLKrowtext, column=ValueUSDcol)

MyBLKValueUSDvardata = StringVar()
MyBLKValueUSDlabeldata = Label(app, textvariable=MyBLKValueUSDvardata, relief=RAISED, font=(DataFontType, DataFontSize), bg=DataBackgroundColor, fg=DataForegroundColor)
MyBLKValueUSDupdate()
MyBLKValueUSDlabeldata.grid(row=BLKrowdata, column=ValueUSDcol)



#LITECOIN
#MyLTC
MyLTCvartext = StringVar()
MyLTClabeltext = Label(app, textvariable=MyLTCvartext, relief=FLAT, font=(TextFontType, TextFontSize), bg=TextBackgroundColor, fg=TextForegroundColor)
MyLTCvartext.set(MyLTCtext)
MyLTClabeltext.grid(row=LTCrowtext, column=MyCOINScol)

MyLTCvardata = StringVar()
MyLTCvardata.set(MyLTC)
MyLTCentry = Entry(app, textvariable=MyLTCvardata, relief=RAISED, font=(DataFontType, DataFontSize), width=9, borderwidth=3, justify=CENTER, bg=EntryBackgroundColor, fg=EntryForegroundColor)
MyLTCentry.grid(row=LTCrowdata, column=MyCOINScol)

MyLTCupdatebutton = Button(app, text='Update NOW', command=MyLTCupdate, bg=ButtonBackGroundColor, fg=ButtonForegroundColor).grid(row=LTCrowdata, column=updateMyCOINScol)


# Display Data and Text for Litecoin price in BTC
LTCpriceBTCvartext = StringVar()
LTCpriceBTClabeltext = Label(app, textvariable=LTCpriceBTCvartext, relief=FLAT, font=(TextFontType, TextFontSize), bg=TextBackgroundColor, fg=TextForegroundColor)
LTCpriceBTCvartext.set(LTCpriceBTCtext)
LTCpriceBTClabeltext.grid(row=LTCrowtext, column=PriceBTCcol)
LTCpriceBTCvardata = StringVar()
LTCpriceBTClabeldata = Label(app, textvariable=LTCpriceBTCvardata, relief=RAISED, font=(DataFontType, DataFontSize), bg=DataBackgroundColor, fg=DataForegroundColor)
LTCpriceBTCupdate()
LTCpriceBTClabeldata.grid(row=LTCrowdata, column=PriceBTCcol)


# Display Data and Text for Litecoin price in USD
LTCpriceUSDvartext = StringVar()
LTCpriceUSDlabeltext = Label(app, textvariable=LTCpriceUSDvartext, relief=FLAT, font=(TextFontType, TextFontSize), bg=TextBackgroundColor, fg=TextForegroundColor)
LTCpriceUSDvartext.set(LTCpriceUSDtext)
LTCpriceUSDlabeltext.grid(row=LTCrowtext, column=PriceUSDcol)
LTCpriceUSDvardata = StringVar()
LTCpriceUSDlabeldata = Label(app, textvariable=LTCpriceUSDvardata, relief=RAISED, font=(DataFontType, DataFontSize), bg=DataBackgroundColor, fg=DataForegroundColor)
LTCpriceUSDupdate()
LTCpriceUSDlabeldata.grid(row=LTCrowdata, column=PriceUSDcol)


#My LTC Value in BTC
MyLTCValueBTCvartext = StringVar()
MyLTCValueBTClabeltext = Label(app, textvariable=MyLTCValueBTCvartext, relief=FLAT, font=(TextFontType, TextFontSize), bg=TextBackgroundColor, fg=TextForegroundColor)
MyLTCValueBTCvartext.set(MyLTCValueBTCtext)
MyLTCValueBTClabeltext.grid(row=LTCrowtext, column=ValueBTCcol)

MyLTCValueBTCvardata = StringVar()
MyLTCValueBTClabeldata = Label(app, textvariable=MyLTCValueBTCvardata, relief=RAISED, font=(DataFontType, DataFontSize), bg=DataBackgroundColor, fg=DataForegroundColor)
MyLTCValueBTCupdate()
MyLTCValueBTClabeldata.grid(row=LTCrowdata, column=ValueBTCcol)

#My LTC Value in USD
MyLTCValueUSDvartext = StringVar()
MyLTCValueUSDlabeltext = Label(app, textvariable=MyLTCValueUSDvartext, relief=FLAT, font=(TextFontType, TextFontSize), bg=TextBackgroundColor, fg=TextForegroundColor)
MyLTCValueUSDvartext.set(MyLTCValueUSDtext)
MyLTCValueUSDlabeltext.grid(row=LTCrowtext, column=ValueUSDcol)

MyLTCValueUSDvardata = StringVar()
MyLTCValueUSDlabeldata = Label(app, textvariable=MyLTCValueUSDvardata, relief=RAISED, font=(DataFontType, DataFontSize), bg=DataBackgroundColor, fg=DataForegroundColor)
MyLTCValueUSDupdate()
MyLTCValueUSDlabeldata.grid(row=LTCrowdata, column=ValueUSDcol)



#DOGECOIN
#MyDOGE
MyDOGEvartext = StringVar()
MyDOGElabeltext = Label(app, textvariable=MyDOGEvartext, relief=FLAT, font=(TextFontType, TextFontSize), bg=TextBackgroundColor, fg=TextForegroundColor)
MyDOGEvartext.set(MyDOGEtext)
MyDOGElabeltext.grid(row=DOGErowtext, column=MyCOINScol)

MyDOGEvardata = StringVar()
MyDOGEvardata.set(MyDOGE)
MyDOGEentry = Entry(app, textvariable=MyDOGEvardata, relief=RAISED, font=(DataFontType, DataFontSize), width=9, borderwidth=3, justify=CENTER, bg=EntryBackgroundColor, fg=EntryForegroundColor)
MyDOGEentry.grid(row=DOGErowdata, column=MyCOINScol)

MyDOGEupdatebutton = Button(app, text='Update NOW', command=MyDOGEupdate, bg=ButtonBackGroundColor, fg=ButtonForegroundColor).grid(row=DOGErowdata, column=updateMyCOINScol)


# Display Data and Text for Dogecoin price in BTC
DOGEpriceBTCvartext = StringVar()
DOGEpriceBTClabeltext = Label(app, textvariable=DOGEpriceBTCvartext, relief=FLAT, font=(TextFontType, TextFontSize), bg=TextBackgroundColor, fg=TextForegroundColor)
DOGEpriceBTCvartext.set(DOGEpriceBTCtext)
DOGEpriceBTClabeltext.grid(row=DOGErowtext, column=PriceBTCcol)
DOGEpriceBTCvardata = StringVar()
DOGEpriceBTClabeldata = Label(app, textvariable=DOGEpriceBTCvardata, relief=RAISED, font=(DataFontType, DataFontSize), bg=DataBackgroundColor, fg=DataForegroundColor)
DOGEpriceBTCupdate()
DOGEpriceBTClabeldata.grid(row=DOGErowdata, column=PriceBTCcol)


# Display Data and Text for Dogecoin price in USD
DOGEpriceUSDvartext = StringVar()
DOGEpriceUSDlabeltext = Label(app, textvariable=DOGEpriceUSDvartext, relief=FLAT, font=(TextFontType, TextFontSize), bg=TextBackgroundColor, fg=TextForegroundColor)
DOGEpriceUSDvartext.set(DOGEpriceUSDtext)
DOGEpriceUSDlabeltext.grid(row=DOGErowtext, column=PriceUSDcol)
DOGEpriceUSDvardata = StringVar()
DOGEpriceUSDlabeldata = Label(app, textvariable=DOGEpriceUSDvardata, relief=RAISED, font=(DataFontType, DataFontSize), bg=DataBackgroundColor, fg=DataForegroundColor)
DOGEpriceUSDupdate()
DOGEpriceUSDlabeldata.grid(row=DOGErowdata, column=PriceUSDcol)


#My DOGE Value in BTC
MyDOGEValueBTCvartext = StringVar()
MyDOGEValueBTClabeltext = Label(app, textvariable=MyDOGEValueBTCvartext, relief=FLAT, font=(TextFontType, TextFontSize), bg=TextBackgroundColor, fg=TextForegroundColor)
MyDOGEValueBTCvartext.set(MyDOGEValueBTCtext)
MyDOGEValueBTClabeltext.grid(row=DOGErowtext, column=ValueBTCcol)

MyDOGEValueBTCvardata = StringVar()
MyDOGEValueBTClabeldata = Label(app, textvariable=MyDOGEValueBTCvardata, relief=RAISED, font=(DataFontType, DataFontSize), bg=DataBackgroundColor, fg=DataForegroundColor)
MyDOGEValueBTCupdate()
MyDOGEValueBTClabeldata.grid(row=DOGErowdata, column=ValueBTCcol)

#My DOGE Value in USD
MyDOGEValueUSDvartext = StringVar()
MyDOGEValueUSDlabeltext = Label(app, textvariable=MyDOGEValueUSDvartext, relief=FLAT, font=(TextFontType, TextFontSize), bg=TextBackgroundColor, fg=TextForegroundColor)
MyDOGEValueUSDvartext.set(MyDOGEValueUSDtext)
MyDOGEValueUSDlabeltext.grid(row=DOGErowtext, column=ValueUSDcol)

MyDOGEValueUSDvardata = StringVar()
MyDOGEValueUSDlabeldata = Label(app, textvariable=MyDOGEValueUSDvardata, relief=RAISED, font=(DataFontType, DataFontSize), bg=DataBackgroundColor, fg=DataForegroundColor)
MyDOGEValueUSDupdate()
MyDOGEValueUSDlabeldata.grid(row=DOGErowdata, column=ValueUSDcol)




#DARKCOIN
#MyDRK
MyDRKvartext = StringVar()
MyDRKlabeltext = Label(app, textvariable=MyDRKvartext, relief=FLAT, font=(TextFontType, TextFontSize), bg=TextBackgroundColor, fg=TextForegroundColor)
MyDRKvartext.set(MyDRKtext)
MyDRKlabeltext.grid(row=DRKrowtext, column=MyCOINScol)

MyDRKvardata = StringVar()
MyDRKvardata.set(MyDRK)
MyDRKentry = Entry(app, textvariable=MyDRKvardata, relief=RAISED, font=(DataFontType, DataFontSize), width=9, borderwidth=3, justify=CENTER, bg=EntryBackgroundColor, fg=EntryForegroundColor)
MyDRKentry.grid(row=DRKrowdata, column=MyCOINScol)

MyDRKupdatebutton = Button(app, text='Update NOW', command=MyDRKupdate, bg=ButtonBackGroundColor, fg=ButtonForegroundColor).grid(row=DRKrowdata, column=updateMyCOINScol)


# Display Data and Text for Darkcoin price in BTC
DRKpriceBTCvartext = StringVar()
DRKpriceBTClabeltext = Label(app, textvariable=DRKpriceBTCvartext, relief=FLAT, font=(TextFontType, TextFontSize), bg=TextBackgroundColor, fg=TextForegroundColor)
DRKpriceBTCvartext.set(DRKpriceBTCtext)
DRKpriceBTClabeltext.grid(row=DRKrowtext, column=PriceBTCcol)
DRKpriceBTCvardata = StringVar()
DRKpriceBTClabeldata = Label(app, textvariable=DRKpriceBTCvardata, relief=RAISED, font=(DataFontType, DataFontSize), bg=DataBackgroundColor, fg=DataForegroundColor)
DRKpriceBTCupdate()
DRKpriceBTClabeldata.grid(row=DRKrowdata, column=PriceBTCcol)


# Display Data and Text for Darkcoin price in USD
DRKpriceUSDvartext = StringVar()
DRKpriceUSDlabeltext = Label(app, textvariable=DRKpriceUSDvartext, relief=FLAT, font=(TextFontType, TextFontSize), bg=TextBackgroundColor, fg=TextForegroundColor)
DRKpriceUSDvartext.set(DRKpriceUSDtext)
DRKpriceUSDlabeltext.grid(row=DRKrowtext, column=PriceUSDcol)
DRKpriceUSDvardata = StringVar()
DRKpriceUSDlabeldata = Label(app, textvariable=DRKpriceUSDvardata, relief=RAISED, font=(DataFontType, DataFontSize), bg=DataBackgroundColor, fg=DataForegroundColor)
DRKpriceUSDupdate()
DRKpriceUSDlabeldata.grid(row=DRKrowdata, column=PriceUSDcol)


#My DRK Value in BTC
MyDRKValueBTCvartext = StringVar()
MyDRKValueBTClabeltext = Label(app, textvariable=MyDRKValueBTCvartext, relief=FLAT, font=(TextFontType, TextFontSize), bg=TextBackgroundColor, fg=TextForegroundColor)
MyDRKValueBTCvartext.set(MyDRKValueBTCtext)
MyDRKValueBTClabeltext.grid(row=DRKrowtext, column=ValueBTCcol)

MyDRKValueBTCvardata = StringVar()
MyDRKValueBTClabeldata = Label(app, textvariable=MyDRKValueBTCvardata, relief=RAISED, font=(DataFontType, DataFontSize), bg=DataBackgroundColor, fg=DataForegroundColor)
MyDRKValueBTCupdate()
MyDRKValueBTClabeldata.grid(row=DRKrowdata, column=ValueBTCcol)


#My DRK Value in USD
MyDRKValueUSDvartext = StringVar()
MyDRKValueUSDlabeltext = Label(app, textvariable=MyDRKValueUSDvartext, relief=FLAT, font=(TextFontType, TextFontSize), bg=TextBackgroundColor, fg=TextForegroundColor)
MyDRKValueUSDvartext.set(MyDRKValueUSDtext)
MyDRKValueUSDlabeltext.grid(row=DRKrowtext, column=ValueUSDcol)

MyDRKValueUSDvardata = StringVar()
MyDRKValueUSDlabeldata = Label(app, textvariable=MyDRKValueUSDvardata, relief=RAISED, font=(DataFontType, DataFontSize), bg=DataBackgroundColor, fg=DataForegroundColor)
MyDRKValueUSDupdate()
MyDRKValueUSDlabeldata.grid(row=DRKrowdata, column=ValueUSDcol)



#PEERCOIN
#MyPPC
MyPPCvartext = StringVar()
MyPPClabeltext = Label(app, textvariable=MyPPCvartext, relief=FLAT, font=(TextFontType, TextFontSize), bg=TextBackgroundColor, fg=TextForegroundColor)
MyPPCvartext.set(MyPPCtext)
MyPPClabeltext.grid(row=PPCrowtext, column=MyCOINScol)

MyPPCvardata = StringVar()
MyPPCvardata.set(MyPPC)
MyPPCentry = Entry(app, textvariable=MyPPCvardata, relief=RAISED, font=(DataFontType, DataFontSize), width=9, borderwidth=3, justify=CENTER, bg=EntryBackgroundColor, fg=EntryForegroundColor)
MyPPCentry.grid(row=PPCrowdata, column=MyCOINScol)

MyPPCupdatebutton = Button(app, text='Update NOW', command=MyPPCupdate, bg=ButtonBackGroundColor, fg=ButtonForegroundColor).grid(row=PPCrowdata, column=updateMyCOINScol)


# Display Data and Text for Peercoin price in BTC
PPCpriceBTCvartext = StringVar()
PPCpriceBTClabeltext = Label(app, textvariable=PPCpriceBTCvartext, relief=FLAT, font=(TextFontType, TextFontSize), bg=TextBackgroundColor, fg=TextForegroundColor)
PPCpriceBTCvartext.set(PPCpriceBTCtext)
PPCpriceBTClabeltext.grid(row=PPCrowtext, column=PriceBTCcol)
PPCpriceBTCvardata = StringVar()
PPCpriceBTClabeldata = Label(app, textvariable=PPCpriceBTCvardata, relief=RAISED, font=(DataFontType, DataFontSize), bg=DataBackgroundColor, fg=DataForegroundColor)
PPCpriceBTCupdate()
PPCpriceBTClabeldata.grid(row=PPCrowdata, column=PriceBTCcol)


# Display Data and Text for Peercoin price in USD
PPCpriceUSDvartext = StringVar()
PPCpriceUSDlabeltext = Label(app, textvariable=PPCpriceUSDvartext, relief=FLAT, font=(TextFontType, TextFontSize), bg=TextBackgroundColor, fg=TextForegroundColor)
PPCpriceUSDvartext.set(PPCpriceUSDtext)
PPCpriceUSDlabeltext.grid(row=PPCrowtext, column=PriceUSDcol)
PPCpriceUSDvardata = StringVar()
PPCpriceUSDlabeldata = Label(app, textvariable=PPCpriceUSDvardata, relief=RAISED, font=(DataFontType, DataFontSize), bg=DataBackgroundColor, fg=DataForegroundColor)
PPCpriceUSDupdate()
PPCpriceUSDlabeldata.grid(row=PPCrowdata, column=PriceUSDcol)


#My PPC Value in BTC
MyPPCValueBTCvartext = StringVar()
MyPPCValueBTClabeltext = Label(app, textvariable=MyPPCValueBTCvartext, relief=FLAT, font=(TextFontType, TextFontSize), bg=TextBackgroundColor, fg=TextForegroundColor)
MyPPCValueBTCvartext.set(MyPPCValueBTCtext)
MyPPCValueBTClabeltext.grid(row=PPCrowtext, column=ValueBTCcol)

MyPPCValueBTCvardata = StringVar()
MyPPCValueBTClabeldata = Label(app, textvariable=MyPPCValueBTCvardata, relief=RAISED, font=(DataFontType, DataFontSize), bg=DataBackgroundColor, fg=DataForegroundColor)
MyPPCValueBTCupdate()
MyPPCValueBTClabeldata.grid(row=PPCrowdata, column=ValueBTCcol)


#My PPC Value in USD
MyPPCValueUSDvartext = StringVar()
MyPPCValueUSDlabeltext = Label(app, textvariable=MyPPCValueUSDvartext, relief=FLAT, font=(TextFontType, TextFontSize), bg=TextBackgroundColor, fg=TextForegroundColor)
MyPPCValueUSDvartext.set(MyPPCValueUSDtext)
MyPPCValueUSDlabeltext.grid(row=PPCrowtext, column=ValueUSDcol)

MyPPCValueUSDvardata = StringVar()
MyPPCValueUSDlabeldata = Label(app, textvariable=MyPPCValueUSDvardata, relief=RAISED, font=(DataFontType, DataFontSize), bg=DataBackgroundColor, fg=DataForegroundColor)
MyPPCValueUSDupdate()
MyPPCValueUSDlabeldata.grid(row=PPCrowdata, column=ValueUSDcol)



#NXTcoin
#MyNXT
MyNXTvartext = StringVar()
MyNXTlabeltext = Label(app, textvariable=MyNXTvartext, relief=FLAT, font=(TextFontType, TextFontSize), bg=TextBackgroundColor, fg=TextForegroundColor)
MyNXTvartext.set(MyNXTtext)
MyNXTlabeltext.grid(row=NXTrowtext, column=MyCOINScol)

MyNXTvardata = StringVar()
MyNXTvardata.set(MyNXT)
MyNXTentry = Entry(app, textvariable=MyNXTvardata, relief=RAISED, font=(DataFontType, DataFontSize), width=9, borderwidth=3, justify=CENTER, bg=EntryBackgroundColor, fg=EntryForegroundColor)
MyNXTentry.grid(row=NXTrowdata, column=MyCOINScol)

MyNXTupdatebutton = Button(app, text='Update NOW', command=MyNXTupdate, bg=ButtonBackGroundColor, fg=ButtonForegroundColor).grid(row=NXTrowdata, column=updateMyCOINScol)


# Display Data and Text for NXTcoin price in BTC
NXTpriceBTCvartext = StringVar()
NXTpriceBTClabeltext = Label(app, textvariable=NXTpriceBTCvartext, relief=FLAT, font=(TextFontType, TextFontSize), bg=TextBackgroundColor, fg=TextForegroundColor)
NXTpriceBTCvartext.set(NXTpriceBTCtext)
NXTpriceBTClabeltext.grid(row=NXTrowtext, column=PriceBTCcol)
NXTpriceBTCvardata = StringVar()
NXTpriceBTClabeldata = Label(app, textvariable=NXTpriceBTCvardata, relief=RAISED, font=(DataFontType, DataFontSize), bg=DataBackgroundColor, fg=DataForegroundColor)
NXTpriceBTCupdate()
NXTpriceBTClabeldata.grid(row=NXTrowdata, column=PriceBTCcol)


# Display Data and Text for NXTcoin price in USD
NXTpriceUSDvartext = StringVar()
NXTpriceUSDlabeltext = Label(app, textvariable=NXTpriceUSDvartext, relief=FLAT, font=(TextFontType, TextFontSize), bg=TextBackgroundColor, fg=TextForegroundColor)
NXTpriceUSDvartext.set(NXTpriceUSDtext)
NXTpriceUSDlabeltext.grid(row=NXTrowtext, column=PriceUSDcol)
NXTpriceUSDvardata = StringVar()
NXTpriceUSDlabeldata = Label(app, textvariable=NXTpriceUSDvardata, relief=RAISED, font=(DataFontType, DataFontSize), bg=DataBackgroundColor, fg=DataForegroundColor)
NXTpriceUSDupdate()
NXTpriceUSDlabeldata.grid(row=NXTrowdata, column=PriceUSDcol)


#My NXT Value in BTC
MyNXTValueBTCvartext = StringVar()
MyNXTValueBTClabeltext = Label(app, textvariable=MyNXTValueBTCvartext, relief=FLAT, font=(TextFontType, TextFontSize), bg=TextBackgroundColor, fg=TextForegroundColor)
MyNXTValueBTCvartext.set(MyNXTValueBTCtext)
MyNXTValueBTClabeltext.grid(row=NXTrowtext, column=ValueBTCcol)

MyNXTValueBTCvardata = StringVar()
MyNXTValueBTClabeldata = Label(app, textvariable=MyNXTValueBTCvardata, relief=RAISED, font=(DataFontType, DataFontSize), bg=DataBackgroundColor, fg=DataForegroundColor)
MyNXTValueBTCupdate()
MyNXTValueBTClabeldata.grid(row=NXTrowdata, column=ValueBTCcol)


#My NXT Value in USD
MyNXTValueUSDvartext = StringVar()
MyNXTValueUSDlabeltext = Label(app, textvariable=MyNXTValueUSDvartext, relief=FLAT, font=(TextFontType, TextFontSize), bg=TextBackgroundColor, fg=TextForegroundColor)
MyNXTValueUSDvartext.set(MyNXTValueUSDtext)
MyNXTValueUSDlabeltext.grid(row=NXTrowtext, column=ValueUSDcol)

MyNXTValueUSDvardata = StringVar()
MyNXTValueUSDlabeldata = Label(app, textvariable=MyNXTValueUSDvardata, relief=RAISED, font=(DataFontType, DataFontSize), bg=DataBackgroundColor, fg=DataForegroundColor)
MyNXTValueUSDupdate()
MyNXTValueUSDlabeldata.grid(row=NXTrowdata, column=ValueUSDcol)



#Counterparty
#MyXCP
MyXCPvartext = StringVar()
MyXCPlabeltext = Label(app, textvariable=MyXCPvartext, relief=FLAT, font=(TextFontType, TextFontSize), bg=TextBackgroundColor, fg=TextForegroundColor)
MyXCPvartext.set(MyXCPtext)
MyXCPlabeltext.grid(row=XCProwtext, column=MyCOINScol)

MyXCPvardata = StringVar()
MyXCPvardata.set(MyXCP)
MyXCPentry = Entry(app, textvariable=MyXCPvardata, relief=RAISED, font=(DataFontType, DataFontSize), width=9, borderwidth=3, justify=CENTER, bg=EntryBackgroundColor, fg=EntryForegroundColor)
MyXCPentry.grid(row=XCProwdata, column=MyCOINScol)

MyXCPupdatebutton = Button(app, text='Update NOW', command=MyXCPupdate, bg=ButtonBackGroundColor, fg=ButtonForegroundColor).grid(row=XCProwdata, column=updateMyCOINScol)


# Display Data and Text for Counterparty price in BTC
XCPpriceBTCvartext = StringVar()
XCPpriceBTClabeltext = Label(app, textvariable=XCPpriceBTCvartext, relief=FLAT, font=(TextFontType, TextFontSize), bg=TextBackgroundColor, fg=TextForegroundColor)
XCPpriceBTCvartext.set(XCPpriceBTCtext)
XCPpriceBTClabeltext.grid(row=XCProwtext, column=PriceBTCcol)
XCPpriceBTCvardata = StringVar()
XCPpriceBTClabeldata = Label(app, textvariable=XCPpriceBTCvardata, relief=RAISED, font=(DataFontType, DataFontSize), bg=DataBackgroundColor, fg=DataForegroundColor)
XCPpriceBTCupdate()
XCPpriceBTClabeldata.grid(row=XCProwdata, column=PriceBTCcol)


# Display Data and Text for Counterparty price in USD
XCPpriceUSDvartext = StringVar()
XCPpriceUSDlabeltext = Label(app, textvariable=XCPpriceUSDvartext, relief=FLAT, font=(TextFontType, TextFontSize), bg=TextBackgroundColor, fg=TextForegroundColor)
XCPpriceUSDvartext.set(XCPpriceUSDtext)
XCPpriceUSDlabeltext.grid(row=XCProwtext, column=PriceUSDcol)
XCPpriceUSDvardata = StringVar()
XCPpriceUSDlabeldata = Label(app, textvariable=XCPpriceUSDvardata, relief=RAISED, font=(DataFontType, DataFontSize), bg=DataBackgroundColor, fg=DataForegroundColor)
XCPpriceUSDupdate()
XCPpriceUSDlabeldata.grid(row=XCProwdata, column=PriceUSDcol)


#My XCP Value in BTC
MyXCPValueBTCvartext = StringVar()
MyXCPValueBTClabeltext = Label(app, textvariable=MyXCPValueBTCvartext, relief=FLAT, font=(TextFontType, TextFontSize), bg=TextBackgroundColor, fg=TextForegroundColor)
MyXCPValueBTCvartext.set(MyXCPValueBTCtext)
MyXCPValueBTClabeltext.grid(row=XCProwtext, column=ValueBTCcol)

MyXCPValueBTCvardata = StringVar()
MyXCPValueBTClabeldata = Label(app, textvariable=MyXCPValueBTCvardata, relief=RAISED, font=(DataFontType, DataFontSize), bg=DataBackgroundColor, fg=DataForegroundColor)
MyXCPValueBTCupdate()
MyXCPValueBTClabeldata.grid(row=XCProwdata, column=ValueBTCcol)


#My XCP Value in USD
MyXCPValueUSDvartext = StringVar()
MyXCPValueUSDlabeltext = Label(app, textvariable=MyXCPValueUSDvartext, relief=FLAT, font=(TextFontType, TextFontSize), bg=TextBackgroundColor, fg=TextForegroundColor)
MyXCPValueUSDvartext.set(MyXCPValueUSDtext)
MyXCPValueUSDlabeltext.grid(row=XCProwtext, column=ValueUSDcol)

MyXCPValueUSDvardata = StringVar()
MyXCPValueUSDlabeldata = Label(app, textvariable=MyXCPValueUSDvardata, relief=RAISED, font=(DataFontType, DataFontSize), bg=DataBackgroundColor, fg=DataForegroundColor)
MyXCPValueUSDupdate()
MyXCPValueUSDlabeldata.grid(row=XCProwdata, column=ValueUSDcol)



#Namecoin
#MyNMC
MyNMCvartext = StringVar()
MyNMClabeltext = Label(app, textvariable=MyNMCvartext, relief=FLAT, font=(TextFontType, TextFontSize), bg=TextBackgroundColor, fg=TextForegroundColor)
MyNMCvartext.set(MyNMCtext)
MyNMClabeltext.grid(row=NMCrowtext, column=MyCOINScol)

MyNMCvardata = StringVar()
MyNMCvardata.set(MyNMC)
MyNMCentry = Entry(app, textvariable=MyNMCvardata, relief=RAISED, font=(DataFontType, DataFontSize), width=9, borderwidth=3, justify=CENTER, bg=EntryBackgroundColor, fg=EntryForegroundColor)
MyNMCentry.grid(row=NMCrowdata, column=MyCOINScol)

MyNMCupdatebutton = Button(app, text='Update NOW', command=MyNMCupdate, bg=ButtonBackGroundColor, fg=ButtonForegroundColor).grid(row=NMCrowdata, column=updateMyCOINScol)


# Display Data and Text for Namecoin price in BTC
NMCpriceBTCvartext = StringVar()
NMCpriceBTClabeltext = Label(app, textvariable=NMCpriceBTCvartext, relief=FLAT, font=(TextFontType, TextFontSize), bg=TextBackgroundColor, fg=TextForegroundColor)
NMCpriceBTCvartext.set(NMCpriceBTCtext)
NMCpriceBTClabeltext.grid(row=NMCrowtext, column=PriceBTCcol)
NMCpriceBTCvardata = StringVar()
NMCpriceBTClabeldata = Label(app, textvariable=NMCpriceBTCvardata, relief=RAISED, font=(DataFontType, DataFontSize), bg=DataBackgroundColor, fg=DataForegroundColor)
NMCpriceBTCupdate()
NMCpriceBTClabeldata.grid(row=NMCrowdata, column=PriceBTCcol)


# Display Data and Text for Namecoin price in USD
NMCpriceUSDvartext = StringVar()
NMCpriceUSDlabeltext = Label(app, textvariable=NMCpriceUSDvartext, relief=FLAT, font=(TextFontType, TextFontSize), bg=TextBackgroundColor, fg=TextForegroundColor)
NMCpriceUSDvartext.set(NMCpriceUSDtext)
NMCpriceUSDlabeltext.grid(row=NMCrowtext, column=PriceUSDcol)
NMCpriceUSDvardata = StringVar()
NMCpriceUSDlabeldata = Label(app, textvariable=NMCpriceUSDvardata, relief=RAISED, font=(DataFontType, DataFontSize), bg=DataBackgroundColor, fg=DataForegroundColor)
NMCpriceUSDupdate()
NMCpriceUSDlabeldata.grid(row=NMCrowdata, column=PriceUSDcol)


#My NMC Value in BTC
MyNMCValueBTCvartext = StringVar()
MyNMCValueBTClabeltext = Label(app, textvariable=MyNMCValueBTCvartext, relief=FLAT, font=(TextFontType, TextFontSize), bg=TextBackgroundColor, fg=TextForegroundColor)
MyNMCValueBTCvartext.set(MyNMCValueBTCtext)
MyNMCValueBTClabeltext.grid(row=NMCrowtext, column=ValueBTCcol)

MyNMCValueBTCvardata = StringVar()
MyNMCValueBTClabeldata = Label(app, textvariable=MyNMCValueBTCvardata, relief=RAISED, font=(DataFontType, DataFontSize), bg=DataBackgroundColor, fg=DataForegroundColor)
MyNMCValueBTCupdate()
MyNMCValueBTClabeldata.grid(row=NMCrowdata, column=ValueBTCcol)


#My NMC Value in USD
MyNMCValueUSDvartext = StringVar()
MyNMCValueUSDlabeltext = Label(app, textvariable=MyNMCValueUSDvartext, relief=FLAT, font=(TextFontType, TextFontSize), bg=TextBackgroundColor, fg=TextForegroundColor)
MyNMCValueUSDvartext.set(MyNMCValueUSDtext)
MyNMCValueUSDlabeltext.grid(row=NMCrowtext, column=ValueUSDcol)

MyNMCValueUSDvardata = StringVar()
MyNMCValueUSDlabeldata = Label(app, textvariable=MyNMCValueUSDvardata, relief=RAISED, font=(DataFontType, DataFontSize), bg=DataBackgroundColor, fg=DataForegroundColor)
MyNMCValueUSDupdate()
MyNMCValueUSDlabeldata.grid(row=NMCrowdata, column=ValueUSDcol)



#Monero
#MyXMR
MyXMRvartext = StringVar()
MyXMRlabeltext = Label(app, textvariable=MyXMRvartext, relief=FLAT, font=(TextFontType, TextFontSize), bg=TextBackgroundColor, fg=TextForegroundColor)
MyXMRvartext.set(MyXMRtext)
MyXMRlabeltext.grid(row=XMRrowtext, column=MyCOINScol)

MyXMRvardata = StringVar()
MyXMRvardata.set(MyXMR)
MyXMRentry = Entry(app, textvariable=MyXMRvardata, relief=RAISED, font=(DataFontType, DataFontSize), width=9, borderwidth=3, justify=CENTER, bg=EntryBackgroundColor, fg=EntryForegroundColor)
MyXMRentry.grid(row=XMRrowdata, column=MyCOINScol)

MyXMRupdatebutton = Button(app, text='Update NOW', command=MyXMRupdate, bg=ButtonBackGroundColor, fg=ButtonForegroundColor).grid(row=XMRrowdata, column=updateMyCOINScol)


# Display Data and Text for Monero price in BTC
XMRpriceBTCvartext = StringVar()
XMRpriceBTClabeltext = Label(app, textvariable=XMRpriceBTCvartext, relief=FLAT, font=(TextFontType, TextFontSize), bg=TextBackgroundColor, fg=TextForegroundColor)
XMRpriceBTCvartext.set(XMRpriceBTCtext)
XMRpriceBTClabeltext.grid(row=XMRrowtext, column=PriceBTCcol)
XMRpriceBTCvardata = StringVar()
XMRpriceBTClabeldata = Label(app, textvariable=XMRpriceBTCvardata, relief=RAISED, font=(DataFontType, DataFontSize), bg=DataBackgroundColor, fg=DataForegroundColor)
XMRpriceBTCupdate()
XMRpriceBTClabeldata.grid(row=XMRrowdata, column=PriceBTCcol)


# Display Data and Text for Monero price in USD
XMRpriceUSDvartext = StringVar()
XMRpriceUSDlabeltext = Label(app, textvariable=XMRpriceUSDvartext, relief=FLAT, font=(TextFontType, TextFontSize), bg=TextBackgroundColor, fg=TextForegroundColor)
XMRpriceUSDvartext.set(XMRpriceUSDtext)
XMRpriceUSDlabeltext.grid(row=XMRrowtext, column=PriceUSDcol)
XMRpriceUSDvardata = StringVar()
XMRpriceUSDlabeldata = Label(app, textvariable=XMRpriceUSDvardata, relief=RAISED, font=(DataFontType, DataFontSize), bg=DataBackgroundColor, fg=DataForegroundColor)
XMRpriceUSDupdate()
XMRpriceUSDlabeldata.grid(row=XMRrowdata, column=PriceUSDcol)


#My XMR Value in BTC
MyXMRValueBTCvartext = StringVar()
MyXMRValueBTClabeltext = Label(app, textvariable=MyXMRValueBTCvartext, relief=FLAT, font=(TextFontType, TextFontSize), bg=TextBackgroundColor, fg=TextForegroundColor)
MyXMRValueBTCvartext.set(MyXMRValueBTCtext)
MyXMRValueBTClabeltext.grid(row=XMRrowtext, column=ValueBTCcol)

MyXMRValueBTCvardata = StringVar()
MyXMRValueBTClabeldata = Label(app, textvariable=MyXMRValueBTCvardata, relief=RAISED, font=(DataFontType, DataFontSize), bg=DataBackgroundColor, fg=DataForegroundColor)
MyXMRValueBTCupdate()
MyXMRValueBTClabeldata.grid(row=XMRrowdata, column=ValueBTCcol)


#My XMR Value in USD
MyXMRValueUSDvartext = StringVar()
MyXMRValueUSDlabeltext = Label(app, textvariable=MyXMRValueUSDvartext, relief=FLAT, font=(TextFontType, TextFontSize), bg=TextBackgroundColor, fg=TextForegroundColor)
MyXMRValueUSDvartext.set(MyXMRValueUSDtext)
MyXMRValueUSDlabeltext.grid(row=XMRrowtext, column=ValueUSDcol)

MyXMRValueUSDvardata = StringVar()
MyXMRValueUSDlabeldata = Label(app, textvariable=MyXMRValueUSDvardata, relief=RAISED, font=(DataFontType, DataFontSize), bg=DataBackgroundColor, fg=DataForegroundColor)
MyXMRValueUSDupdate()
MyXMRValueUSDlabeldata.grid(row=XMRrowdata, column=ValueUSDcol)



#BitShares
#MyBTS
MyBTSvartext = StringVar()
MyBTSlabeltext = Label(app, textvariable=MyBTSvartext, relief=FLAT, font=(TextFontType, TextFontSize), bg=TextBackgroundColor, fg=TextForegroundColor)
MyBTSvartext.set(MyBTStext)
MyBTSlabeltext.grid(row=BTSrowtext, column=MyCOINScol)

MyBTSvardata = StringVar()
MyBTSvardata.set(MyBTS)
MyBTSentry = Entry(app, textvariable=MyBTSvardata, relief=RAISED, font=(DataFontType, DataFontSize), width=9, borderwidth=3, justify=CENTER, bg=EntryBackgroundColor, fg=EntryForegroundColor)
MyBTSentry.grid(row=BTSrowdata, column=MyCOINScol)

MyBTSupdatebutton = Button(app, text='Update NOW', command=MyBTSupdate, bg=ButtonBackGroundColor, fg=ButtonForegroundColor).grid(row=BTSrowdata, column=updateMyCOINScol)


# Display Data and Text for BitShares price in BTC
BTSpriceBTCvartext = StringVar()
BTSpriceBTClabeltext = Label(app, textvariable=BTSpriceBTCvartext, relief=FLAT, font=(TextFontType, TextFontSize), bg=TextBackgroundColor, fg=TextForegroundColor)
BTSpriceBTCvartext.set(BTSpriceBTCtext)
BTSpriceBTClabeltext.grid(row=BTSrowtext, column=PriceBTCcol)
BTSpriceBTCvardata = StringVar()
BTSpriceBTClabeldata = Label(app, textvariable=BTSpriceBTCvardata, relief=RAISED, font=(DataFontType, DataFontSize), bg=DataBackgroundColor, fg=DataForegroundColor)
BTSpriceBTCupdate()
BTSpriceBTClabeldata.grid(row=BTSrowdata, column=PriceBTCcol)


# Display Data and Text for BitShares price in USD
BTSpriceUSDvartext = StringVar()
BTSpriceUSDlabeltext = Label(app, textvariable=BTSpriceUSDvartext, relief=FLAT, font=(TextFontType, TextFontSize), bg=TextBackgroundColor, fg=TextForegroundColor)
BTSpriceUSDvartext.set(BTSpriceUSDtext)
BTSpriceUSDlabeltext.grid(row=BTSrowtext, column=PriceUSDcol)
BTSpriceUSDvardata = StringVar()
BTSpriceUSDlabeldata = Label(app, textvariable=BTSpriceUSDvardata, relief=RAISED, font=(DataFontType, DataFontSize), bg=DataBackgroundColor, fg=DataForegroundColor)
BTSpriceUSDupdate()
BTSpriceUSDlabeldata.grid(row=BTSrowdata, column=PriceUSDcol)


#My BTS Value in BTC
MyBTSValueBTCvartext = StringVar()
MyBTSValueBTClabeltext = Label(app, textvariable=MyBTSValueBTCvartext, relief=FLAT, font=(TextFontType, TextFontSize), bg=TextBackgroundColor, fg=TextForegroundColor)
MyBTSValueBTCvartext.set(MyBTSValueBTCtext)
MyBTSValueBTClabeltext.grid(row=BTSrowtext, column=ValueBTCcol)

MyBTSValueBTCvardata = StringVar()
MyBTSValueBTClabeldata = Label(app, textvariable=MyBTSValueBTCvardata, relief=RAISED, font=(DataFontType, DataFontSize), bg=DataBackgroundColor, fg=DataForegroundColor)
MyBTSValueBTCupdate()
MyBTSValueBTClabeldata.grid(row=BTSrowdata, column=ValueBTCcol)


#My BTS Value in USD
MyBTSValueUSDvartext = StringVar()
MyBTSValueUSDlabeltext = Label(app, textvariable=MyBTSValueUSDvartext, relief=FLAT, font=(TextFontType, TextFontSize), bg=TextBackgroundColor, fg=TextForegroundColor)
MyBTSValueUSDvartext.set(MyBTSValueUSDtext)
MyBTSValueUSDlabeltext.grid(row=BTSrowtext, column=ValueUSDcol)

MyBTSValueUSDvardata = StringVar()
MyBTSValueUSDlabeldata = Label(app, textvariable=MyBTSValueUSDvardata, relief=RAISED, font=(DataFontType, DataFontSize), bg=DataBackgroundColor, fg=DataForegroundColor)
MyBTSValueUSDupdate()
MyBTSValueUSDlabeldata.grid(row=BTSrowdata, column=ValueUSDcol)



#FAIRCOIN
#MyFAIR
MyFAIRvartext = StringVar()
MyFAIRlabeltext = Label(app, textvariable=MyFAIRvartext, relief=FLAT, font=(TextFontType, TextFontSize), bg=TextBackgroundColor, fg=TextForegroundColor)
MyFAIRvartext.set(MyFAIRtext)
MyFAIRlabeltext.grid(row=FAIRrowtext, column=MyCOINScol)

MyFAIRvardata = StringVar()
MyFAIRvardata.set(MyFAIR)
MyFAIRentry = Entry(app, textvariable=MyFAIRvardata, relief=RAISED, font=(DataFontType, DataFontSize), width=9, borderwidth=3, justify=CENTER, bg=EntryBackgroundColor, fg=EntryForegroundColor)
MyFAIRentry.grid(row=FAIRrowdata, column=MyCOINScol)

MyFAIRupdatebutton = Button(app, text='Update NOW', command=MyFAIRupdate, bg=ButtonBackGroundColor, fg=ButtonForegroundColor).grid(row=FAIRrowdata, column=updateMyCOINScol)


# Display Data and Text for Faircoin price in BTC
FAIRpriceBTCvartext = StringVar()
FAIRpriceBTClabeltext = Label(app, textvariable=FAIRpriceBTCvartext, relief=FLAT, font=(TextFontType, TextFontSize), bg=TextBackgroundColor, fg=TextForegroundColor)
FAIRpriceBTCvartext.set(FAIRpriceBTCtext)
FAIRpriceBTClabeltext.grid(row=FAIRrowtext, column=PriceBTCcol)
FAIRpriceBTCvardata = StringVar()
FAIRpriceBTClabeldata = Label(app, textvariable=FAIRpriceBTCvardata, relief=RAISED, font=(DataFontType, DataFontSize), bg=DataBackgroundColor, fg=DataForegroundColor)
FAIRpriceBTCupdate()
FAIRpriceBTClabeldata.grid(row=FAIRrowdata, column=PriceBTCcol)


# Display Data and Text for Faircoin price in USD
FAIRpriceUSDvartext = StringVar()
FAIRpriceUSDlabeltext = Label(app, textvariable=FAIRpriceUSDvartext, relief=FLAT, font=(TextFontType, TextFontSize), bg=TextBackgroundColor, fg=TextForegroundColor)
FAIRpriceUSDvartext.set(FAIRpriceUSDtext)
FAIRpriceUSDlabeltext.grid(row=FAIRrowtext, column=PriceUSDcol)
FAIRpriceUSDvardata = StringVar()
FAIRpriceUSDlabeldata = Label(app, textvariable=FAIRpriceUSDvardata, relief=RAISED, font=(DataFontType, DataFontSize), bg=DataBackgroundColor, fg=DataForegroundColor)
FAIRpriceUSDupdate()
FAIRpriceUSDlabeldata.grid(row=FAIRrowdata, column=PriceUSDcol)


#My FAIR Value in BTC
MyFAIRValueBTCvartext = StringVar()
MyFAIRValueBTClabeltext = Label(app, textvariable=MyFAIRValueBTCvartext, relief=FLAT, font=(TextFontType, TextFontSize), bg=TextBackgroundColor, fg=TextForegroundColor)
MyFAIRValueBTCvartext.set(MyFAIRValueBTCtext)
MyFAIRValueBTClabeltext.grid(row=FAIRrowtext, column=ValueBTCcol)

MyFAIRValueBTCvardata = StringVar()
MyFAIRValueBTClabeldata = Label(app, textvariable=MyFAIRValueBTCvardata, relief=RAISED, font=(DataFontType, DataFontSize), bg=DataBackgroundColor, fg=DataForegroundColor)
MyFAIRValueBTCupdate()
MyFAIRValueBTClabeldata.grid(row=FAIRrowdata, column=ValueBTCcol)


#My FAIR Value in USD
MyFAIRValueUSDvartext = StringVar()
MyFAIRValueUSDlabeltext = Label(app, textvariable=MyFAIRValueUSDvartext, relief=FLAT, font=(TextFontType, TextFontSize), bg=TextBackgroundColor, fg=TextForegroundColor)
MyFAIRValueUSDvartext.set(MyFAIRValueUSDtext)
MyFAIRValueUSDlabeltext.grid(row=FAIRrowtext, column=ValueUSDcol)

MyFAIRValueUSDvardata = StringVar()
MyFAIRValueUSDlabeldata = Label(app, textvariable=MyFAIRValueUSDvardata, relief=RAISED, font=(DataFontType, DataFontSize), bg=DataBackgroundColor, fg=DataForegroundColor)
MyFAIRValueUSDupdate()
MyFAIRValueUSDlabeldata.grid(row=FAIRrowdata, column=ValueUSDcol)


#.......... TOTAL ..........
#My Total Value in BTC
MyTotalValueBTCvartext = StringVar()
MyTotalValueBTClabeltext = Label(app, textvariable=MyTotalValueBTCvartext, relief=FLAT, font=(TextFontType, TextFontSize), bg=TextBackgroundColor, fg=TextForegroundColor)
MyTotalValueBTCvartext.set(MyTotalValueBTCtext)
MyTotalValueBTClabeltext.grid(row=100, column=ValueBTCcol)

MyTotalValueBTCvardata = StringVar()
MyTotalValueBTClabeldata = Label(app, textvariable=MyTotalValueBTCvardata, relief=RAISED, font=(DataFontType, DataFontSize), bg=DataBackgroundColor, fg=DataForegroundColor)
MyTotalValueBTCupdate()
MyTotalValueBTClabeldata.grid(row=101, column=ValueBTCcol)


#My Total Value in USD
MyTotalValueUSDvartext = StringVar()
MyTotalValueUSDlabeltext = Label(app, textvariable=MyTotalValueUSDvartext, relief=FLAT, font=(TextFontType, TextFontSize), bg=TextBackgroundColor, fg=TextForegroundColor)
MyTotalValueUSDvartext.set(MyTotalValueUSDtext)
MyTotalValueUSDlabeltext.grid(row=100, column=ValueUSDcol)

MyTotalValueUSDvardata = StringVar()
MyTotalValueUSDlabeldata = Label(app, textvariable=MyTotalValueUSDvardata, relief=RAISED, font=(DataFontType, DataFontSize), bg=DataBackgroundColor, fg=DataForegroundColor)
MyTotalValueUSDupdate()
MyTotalValueUSDlabeldata.grid(row=101, column=ValueUSDcol)



# Update ALL Button
updateALLbutton = Button(app, text='Update ALL', command=updateALLvalue, bg=ButtonBackGroundColor, fg=ButtonForegroundColor).grid(row=0, column=MyCOINScol, columnspan=2)



root.mainloop()