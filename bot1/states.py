import sqlite3
#--
from aiogram import Bot, Router
from aiogram. types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State
#--
add_channel_state = State('add_channel')
edit_channel_state = State('edit_channel')
review_msg_state = State("review_msg")
#--
conn = sqlite3.connect('data/mydatabase.db')
cursor = conn.cursor()
#--
from cfg import *
from bot1.fun import *
from bot1.db import *
from bot1.keyb import *
#--
bot = Bot(TOKEN, parse_mode="HTML")
router = Router()



@router.message(review_msg_state)
async def review_msg_state_handler(message: Message, state: FSMContext) -> None:
    try:
        data = await state.get_data()
        code = data.get('code')
        us = cursor.execute('SELECT channel_link FROM channels WHERE id = ?', (code, )).fetchone()[0]
        CHANNEL_ID = await get_channel_id(us)

        await bot.forward_message(chat_id=CHANNEL_ID, from_chat_id=message.chat.id, message_id=message.message_id)
        await message.answer("Отзыв получен")
    except Exception as e:
        await message.answer("Возникла ошибка при отправлении сообщения, владелец уведомлён об ошибке")
        await bot.send_message(code, text="Ошибка при отправки сообщения в канал, проверьте состояние канала и находиться ли бот в нём")
    finally:
        await state.clear()

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
