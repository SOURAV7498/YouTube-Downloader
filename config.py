import os

class Config:
    API_ID = int(os.getenv("API_ID", '21140176'))
    API_HASH = os.getenv("API_HASH", 'b081ec8da8cf5263a6593041c1ae2a3b')
    BOT_TOKEN = os.getenv("BOT_TOKEN", '8348778650:AAFtt5gch26hxzsG-ihJ1lVF7IQCn6Weq5Y')
