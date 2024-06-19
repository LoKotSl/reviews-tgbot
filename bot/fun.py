import sqlite3
#--
from aiogram import Bot
from aiogram.types import Message
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
#--
from cfg import *
from bot import keyb
#--
bot = Bot(TOKEN)
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

async def final_msg(message: Message, state: FSMContext):
    data = await state.get_data()
    text = data.get('text')
    star = data.get('star')
    user = data.get('user')
    code = data.get('code')
    lang = data.get('lang')
    first = data.get('first')
    if user == None:
        user = first
    else:
        pass
    try:
        us = cursor.execute('SELECT channel_link FROM channels WHERE id = ?', (code, )).fetchone()[0]
        CHANNEL_ID = await get_channel_id(us)

        full_msg = f"Отзыв от: @{user}\nОценка: {star}\nОтзыв: {text}"
        await bot.send_message(CHANNEL_ID, full_msg)
        if lang == "rus":
            await message.answer("Отзыв получен!")
        else:
            await message.answer("Feedback received!")
    except Exception:
        await message.answer("Возникла ошибка при отправлении сообщения, владелец уведомлён об ошибке")
        await bot.send_message(code, 
        "Ошибка при отправки сообщения в канал, проверьте состояние канала и находиться ли бот в нём")
    finally:
        await state.clear()
    
