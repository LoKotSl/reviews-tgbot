import sqlite3
#--
from aiogram import Bot
from aiogram.types import Message
#--
from cfg import *
from bot1 import keyb
#--
bot = Bot(TOKEN, parse_mode="HTML")
#--
conn = sqlite3.connect('data/mydatabase.db')
cursor = conn.cursor()

async def check_tag_exists(link):
    try:
        tag_info = await bot.get_chat(link)
        return True
    except Exception:
        return False
    
async def get_channel_id(username):
    chat = await bot.get_chat(username)
    channel_id = chat.id
    return channel_id

async def yes_chan(message: Message):
    channel = cursor.execute('SELECT channel_link FROM channels WHERE id = ?', (message.from_user.id, )).fetchone()[0]
    await message.answer(f"Ваш канал: {channel}", reply_markup=keyb.editchan_kb)
