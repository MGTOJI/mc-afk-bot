import os
import time
from javascript import require, On

mineflayer = require('mineflayer')

def create_bot():
    bot = mineflayer.createBot({
        'host': 'IKazem-VgMX.aternos.me',
        'port': 33125,
        'username': 'Igor_Bot_24h',
        'version': '1.26.2'
    })

    @On(bot, 'spawn')
    def handle_spawn(*args):
        print("🤖 Bot joined successfully! 24/7 mode active.")

    @On(bot, 'end')
    def handle_end(*args):
        print("⚠️ Bot disconnected. Reconnecting in 10 seconds...")
        time.sleep(10)
        create_bot()

create_bot()
