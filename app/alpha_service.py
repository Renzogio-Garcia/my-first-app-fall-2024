#this is the app/alpha_service.py file...

import os

from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv("ALPHAVANTAGE_API_KEY", default="demo")