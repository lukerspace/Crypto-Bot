from flask import Flask,request
import json,config
from binance.client import Client
from binance.enums import *

app=Flask(__name__)

client = Client(config.BINANCE_API_KEY, config.BINANCE_SECRET_KEY)

def order(side, quantity, symbol, order_type=ORDER_TYPE_MARKET):
    try:
        print(f"Sending order {order_type} - {side} {quantity} {symbol}")
        order = client.create_order(symbol=symbol, side=side, type=order_type, quantity=quantity)
    except Exception as e:
        print("An exception occured - {}".format(e))
        return False

    return order

@app.route("/")
def index():
        return("hello world")

@app.route("/buy", methods=["POST"])
def buy():
        data = json.loads(request.data)
        if data['passphrase'] != config.WEBHOOK_PASSPHRASE:
                return {
                "code": "error",
                "message": "Invalid passphrase"
                }

        side = data['strategy']['order_action'].upper()
        quantity = int(data["money"]/data['bar']['close'])
        print(quantity)
        order_response = order(side, quantity, data['ticker'])

        if order_response:
                return {
                "code": "success",
                "message": "order executed"
                }
        else:
                return {
                "code": "error",
                "message": "order failed"
                }


@app.route("/sell", methods=["POST"])
def sell():
        data = json.loads(request.data)
        if data['passphrase'] != config.WEBHOOK_PASSPHRASE:
                return {
                "code": "error",
                "message": "Invalid passphrase"
                }

        side = data['strategy']['order_action'].upper()
        quantity = int(data["money"]/data['bar']['close'])
        order_response = order(side, quantity, data['ticker'])

        if order_response:
                return {
                "code": "success",
                "message": "order executed"
                }
        else:
                return {
                "code": "error",
                "message": "order failed"
                }
app.run()