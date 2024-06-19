import asyncio
import sqlite3
#--
from aiogram import Bot, Dispatcher, types, F, Router
from aiogram. filters import CommandStart, CommandObject
from aiogram. types import Message
from aiogram.utils.deep_linking import create_start_link
from aiogram.fsm.state import State
from aiogram.fsm.context import FSMContext
#--
from bot.db import *
from bot import callback, states
from bot.fun import *
from bot.keyb import *
from cfg import *
from bot.callback import info
from bot.timer import timeout
#--
add_channel_state = State('add_channel')
edit_channel_state = State('edit_channel')
review_msg_state = State("review_msg")
#--
bot = Bot(TOKEN)
dp = Dispatcher()
router = Router
#--
dp.include_routers(callback.router)
dp.include_routers(states.router)
conn = sqlite3.connect('data/mydatabase.db')
cursor = conn.cursor()
#--
last_used = {}
#--

#Стартовое сообщение
@dp.message(CommandStart())
async def start(message: Message, command: CommandObject, state: FSMContext) -> None:
    code = command.args
    if check_id_in_db(code):
        if timeout(f'{message.from_user.id}:TIMER__start', 86400):
            await message.answer("Вы недавно оставляли отзыв, попробуйте позже")
            return

        user_id = message.from_user.id
        user = message.from_user.username
        firstname = message.from_user.first_name
        await state.set_state(info.user)
        await state.update_data(user=user)
        await state.set_state(info.first)
        await state.update_data(first=firstname)
        await state.set_state(info.code)
        await state.update_data(code=code)
        await message.answer("Выберите язык / Choose language", reply_markup=keyb.language_kb)
    else:    
        await message.answer("Добавьте канал и получайте отзывы по своей ссылке", reply_markup=keyb.start_kb)

#---

@dp.message(F.text.lower() == "добавить канал")
async def add_channel(message: types.Message, state: FSMContext):
    cursor.execute("SELECT COUNT(*) FROM channels WHERE id = ?", (message.from_user.id,))
    if cursor.fetchone()[0]:
        await yes_chan(message)
    else:
        await message.reply("Пришлите @username канала, чтобы его добавить и незабудьте добавить бота в канал", reply_markup=keyb.cancle_kb,)
        await state.set_state(add_channel_state)

#---

@dp.message(F.text.lower() == "получить ссылку")
async def get_link(message: Message):
    if check_id_in_db(message.from_user.id):
        link = await create_start_link(bot, message.from_user.id)
        await message.answer(f"Ваша ссылка:\n{link}")
    else:
        await message.reply("Сначала добавьте канал")

@dp.message(info.text)
async def get_text(message: Message, state: FSMContext):
    await state.update_data(text=message.text)
    data = await state.get_data()
    lang = data.get('lang')
    if lang == "rus":
        await message.answer("↓Оцените работу от 1 до 5↓", reply_markup=stars_kb)
    else:
        await message.answer("↓Rate the work from 1 to 5↓", reply_markup=stars_kb)




















async def main():
    await bot.delete_webhook() #drop_pending_updates=True
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())