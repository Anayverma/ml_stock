from SmartApi import SmartConnect
import pandas as pd
import login as l
import requests

obj=SmartConnect(api_key=l.apikey)
data=obj.generateSession(l.username,l.password,l.totp)
refreshToken=data['data']['refreshToken']
feedToken=obj.getfeedToken()
l.feed_token=feedToken

userProfile=obj.getProfile(refreshToken)
print(userProfile)

#historic api

def OHLCHistory(symbol,token,interval,fdate,todate):
    try:
        historicParam={
            "exchange":"NSE",
            "tradingsymbol":symbol,
            "symboltoken":token,
            "interval":interval,
            "fromdate":fdate,
            "todate":todate
        }
        history=obj.getCandleData(historicParam)['data']
        history=pd.DataFrame(history)

        history=history.rename(
            columns={0:"Date Time",1:"Open",2:"High",3:"Low",4:"Close",5:"Volume"}
        )

        history['Date Time']=pd.to_datetime(history["Date Time"])

        history=history.set_index('Date Time')

        return history
    except Exception as e:
        print("API Failed ....{}".format(e))

def placeorder(symbol,token,qty,exch_seg,buy_sell,ordertype,price):
    try:
        orderparams={
            "variety":"NORMAL",
            "tradingsymbol":symbol,
            "symboltoken":token,
            "transactiontype":buy_sell,
            "exchange":exch_seg,
            "ordertype":ordertype,
            "producttype":"DELIVERY",
            "duration":"DAY",
            "price": price,
            "squreoff":"0",
            "stoploss":"0",
            "quantity":qty
        }
        orderId=obj.placeOrder(orderparams)
        print("Order Placed Successfully...")
        print("Your Order ID : {}".format(orderId))
    except Exception as e:
        print("Order Failed : {}".format(e))
def get_candle_type(row):
    open_price = row['Open']
    high_price = row['High']
    low_price = row['Low']
    close_price = row['Close']

    body_size = abs(open_price - close_price)
    shadow_size_above = high_price - max(open_price, close_price)
    shadow_size_below = min(open_price, close_price) - low_price

    # Determine precise candle type
    if body_size <= 0.02 * max(body_size, shadow_size_above, shadow_size_below):
        if shadow_size_above >= 2 * body_size and shadow_size_below >= 2 * body_size:
            return "Neutral Doji"
        elif shadow_size_above >= 2 * body_size:
            return "Dragonfly Doji"
        elif shadow_size_below >= 2 * body_size:
            return "Gravestone Doji"
        else:
            return "Doji"
    elif close_price > open_price:
        if open_price == low_price and close_price == high_price:
            return "Marubozu"
        elif open_price == low_price:
            return "Bullish Engulfing"
        else:
            return "Bullish Candle"
    elif open_price > close_price:
        if open_price == high_price and close_price == low_price:
            return "Marubozu"
        elif close_price == low_price:
            return "Bearish Engulfing"
        else:
            return "Bearish Candle"
    else:
        return "Indecisive Candle"
def candletype(df):
    df['CandleType'] = df.apply(get_candle_type, axis=1)
    return df
# df = pd.DataFrame(data)
# df = candletype(df)
minute1data=OHLCHistory("IDEA-EQ","14366","THREE_MINUTE","2023-11-16 09:30","2023-11-17 15:30")
print("1 Minute Live Data:")
minute1data_df=pd.DataFrame(minute1data)
minute1data_df=candletype(minute1data_df)
print((minute1data).to_string())
print("printing minute one data with candle type")
print(minute1data_df.to_string())
print(placeorder("IDEA-EQ","14366",1,'NSE','BUY','LIMIT',14.50))
# print(placeorder("SBIN-EQ","3045",1,'NSE','BUY','MARKET',0))
print("E N D    P R O G R A M")