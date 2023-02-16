from telethon import TelegramClient
import logging
import config
import Haron_Bot.handlers


class Bot(TelegramClient):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.me = None #Info about bot will be here
        
bot = Bot('bot', config.API_ID, config.API_HASH) #Create bot with API

bot.parse_mode = 'HTML'
logging.basicConfig(level=logging.INFO)


async def start():
    await bot.connect() #Connect bot to server  
    bot.me = await bot.sign_in(bot_token=config.api_token) #Signin with token and save bot info in file 
    await bot.run_until_disconnected()
    
def run():
    bot.loop.run_until_complete(start())