import os
import dotenv 
from dotenv import *

load_dotenv()

BINANCE_API_KEY = os.getenv("BINANCE_API_KEY")

BINANCE_SECRET_KEY = os.getenv("BINANCE_SECRET_KEY")

WEBHOOK_PASSPHRASE="crypto"