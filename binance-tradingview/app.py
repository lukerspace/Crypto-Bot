from flask import Flask,request
import json,config
from binance.enums import *
from binance.client import Client


app=Flask(__name__)

client = Client(config.BINANCE_API_KEY, config.BINANCE_SECRET_KEY)

def order(side, quantity, symbol, order_type=ORDER_TYPE_MARKET):
    try:
        order = client.create_order(symbol=symbol, side=side, type=order_type, quantity=quantity)
        print(f"Sending order {order_type} - {side} {quantity} {symbol}")
    except Exception as e:
        print("An exception occured - {}".format(e))
        return False

    return order

@app.route("/",methods=["GET"])
def index():
        return("CRYPTO LOADING")

@app.route("/order", methods=["POST"])
def buy():
        data = json.loads(request.data)
        
        if data['passphrase'] != config.WEBHOOK_PASSPHRASE:
                return {
                "code": "error",
                "message": "Invalid passphrase"
                }

        side = data['strategy']['order_action'].upper()
      
        if side=="BUY":
                data["money"]=data["money"]*1
        elif side=="SELL":
                data["money"]=data["money"]*0.9
        else:
                print("ERROR")      
        if data['ticker']=='BTCUSDT':
                quantity = round(float(data["money"]/data['bar']['close']),5)
        if data['ticker']=='ETHUSDT':
                quantity = round(float(data["money"]/data['bar']['close']),4)
        if data['ticker']=='FTMUSDT':
                quantity = int(data["money"]/data['bar']['close'])
        if data['ticker']=='FLOWUSDT':
                quantity = round(float(data["money"]/data['bar']['close']),2)
        if data['ticker']=='MANAUSDT':
                quantity = int(data["money"]/data['bar']['close'])
        if data['ticker']=='SANDUSDT':
                quantity = int(data["money"]/data['bar']['close'])
        if data['ticker']=='FTTUSDT':
                quantity = round(float(data["money"]/data['bar']['close']),2)
        if data['ticker']=='ARUSDT':
                quantity = round(float(data["money"]/data['bar']['close']),2)
        if data['ticker']=='SOLUSDT':
                quantity = round(float(data["money"]/data['bar']['close']),2)
        if data['ticker']=='SUSHIUSDT':
                quantity = round(float(data["money"]/data['bar']['close']),1)
        if data['ticker']=='LRCUSDT':
                quantity = int(data["money"]/data['bar']['close'])
        if data['ticker']=='MASKUSDT':
                quantity = round(float(data["money"]/data['bar']['close']),1)
        if data['ticker']=='DOGEUSDT':
                quantity = int(data["money"]/data['bar']['close'])
        if data['ticker']=='UNIUSDT':
                quantity = round(float(data["money"]/data['bar']['close']),2)
        if data['ticker']=='UNIUSDT':
                quantity = round(float(data["money"]/data['bar']['close']),2)
        if data['ticker']=='ENSUSDT':
                quantity = round(float(data["money"]/data['bar']['close']),2)
        if data['ticker']=='ADAUSDT':
                quantity = round(float(data["money"]/data['bar']['close']),1)
        if data['ticker']=='MINAUSDT':
                quantity = round(float(data["money"]/data['bar']['close']),1)
        if data['ticker']=='ROSEUSDT':
                quantity = round(float(data["money"]/data['bar']['close']),1)
        if data['ticker']=='CRVUSDT':
                quantity = round(float(data["money"]/data['bar']['close']),1)
        if data['ticker']=='SLPUSDT':
                quantity = int(data["money"]/data['bar']['close'])
        if data['ticker']=='DARUSDT':
                quantity = int(data["money"]/data['bar']['close'])
        if data['ticker']=='LITUSDT':
                quantity = round(float(data["money"]/data['bar']['close']),1)
        if data['ticker']=='RADUSDT':
                quantity = round(float(data["money"]/data['bar']['close']),1)
        if data['ticker']=='AAVEUSDT':
                quantity = round(float(data["money"]/data['bar']['close']),3)
        if data['ticker']=='MATICUSDT':
                quantity = round(float(data["money"]/data['bar']['close']),1)

        # order_book=client.get_all_orders(symbol=data["ticker"])
        # order_list=[]
        # for buy_order in order_book:
        #         if buy_order["side"]=="BUY":
        #                 order_list.append(buy_order)
        # quantity=float(order_list[-1]["executedQty"])
        

        order_response = order(side, quantity, data['ticker'])
        
        if order_response:
                print("{} {} units- success ".format(side,quantity))
                return {
                "code": "{} {} units- success ".format(side,quantity),
                "message": "order executed"
                }
        else:
                return {
                "code": "error",
                "message": "order failed"
                }
