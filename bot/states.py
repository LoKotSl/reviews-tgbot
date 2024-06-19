import sqlite3
#--
from aiogram import Bot, Router
from aiogram. types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State
#--
add_channel_state = State('add_channel')
edit_channel_state = State('edit_channel')
#--
conn = sqlite3.connect('data/mydatabase.db')
cursor = conn.cursor()
#--
from cfg import *
from bot.fun import *
from bot.db import *
from bot.keyb import *
#--
bot = Bot(TOKEN)
router = Router()




@router.message(add_channel_state)
async def add_channel_state_handler(message: Message, state: FSMContext) -> None:
    tag_exists = await check_tag_exists(message.text)
    if tag_exists:
        await state.clear()
        add_channel_to_db(message.from_user.id, message.text)
        await message.answer("Канал успешно добавлен", reply_markup=keyb.start_kb)
    else:
        await message.answer("Канала не существует")

@router.message(edit_channel_state)
async def edit_channel_state_handler(message: Message, state: FSMContext) -> None:
    tag_exists = await check_tag_exists(message.text)
    if tag_exists:
        await state.clear()
        edit_channel_in_db(message.from_user.id, message.text)
        await message.answer("Канал успешно изменён", reply_markup=keyb.start_kb)
    else:
        await message.answer("Ошибка при изменении канал")
