import asyncio
import sqlite3
#--
from aiogram import Bot, Dispatcher, types, F, Router
from aiogram. filters import CommandStart, CommandObject
from aiogram. types import Message, ReplyKeyboardRemove
from aiogram.utils.deep_linking import create_start_link
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State
#--
from bot1 import callback, states
from bot1.fun import *
from bot1.db import *
from bot1.keyb import *
from cfg import *
#--
add_channel_state = State('add_channel')
edit_channel_state = State('edit_channel')
review_msg_state = State("review_msg")
#--
bot = Bot(TOKEN, parse_mode="HTML")
dp = Dispatcher()
router = Router
#--
dp.include_routers(callback.router)
dp.include_routers(states.router)
conn = sqlite3.connect('data/mydatabase.db')
cursor = conn.cursor()



#Стартовое сообщение
@dp.message(CommandStart())
async def start(message: Message, command: CommandObject, state: FSMContext) -> None:
    code = command.args
    if check_id_in_db(code):
        await message.answer("Отправьте отзыв:")
        await state.set_state(review_msg_state)
        await state.update_data(code=code)
    else:    
        await message.answer("Добавьте канал и получайте отзывы по своей ссылке", reply_markup=keyb.start_kb)

#---

@dp.message(F.text.lower() == "добавить канал")
async def start(message: types.Message, state: FSMContext):
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




















async def main():
    await bot.delete_webhook() #drop_pending_updates=True
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())