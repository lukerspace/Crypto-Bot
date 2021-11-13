import websocket,json, pprint,datetime

url="wss://stream.binance.com:9443/ws/ethusdt@kline_1m"

def on_open(ws):
    print("open connection")

def on_close(ws):
    print("close connection")

def on_message(ws, message):
    print("recieve msg")
    json_msg=json.loads(message)
    # pprint.pprint(json_msg["k"])
    pprint.pprint(json_msg["k"]["o"])
    pprint.pprint(json_msg["k"]["h"])
    pprint.pprint(json_msg["k"]["l"])
    pprint.pprint(json_msg["k"]["c"])
    pprint.pprint(datetime.datetime.fromtimestamp(json_msg["k"]["t"]/1000.0))

ws=websocket.WebSocketApp(url, on_open=on_open, on_close=on_close, on_message=on_message)
ws.run_forever()