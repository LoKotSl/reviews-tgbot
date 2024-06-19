from aiogram import Dispatcher, Router, types, F
from aiogram. types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
#--
from bot import keyb
from bot.fun import final_msg
#--
dp = Dispatcher()
router = Router()
#--
edit_channel_state = State('edit_channel')

class info(StatesGroup):
    text = State()
    star = State()
    user = State()
    code = State()
    lang = State()
    first = State()


@router.callback_query(F.data == "сancle")
async def cancle(callback: CallbackQuery, state: FSMContext):
    await callback.answer("")
    await state.clear()
    await callback.message.delete()
    await callback.message.answer("Меню", reply_markup=keyb.start_kb)

@router.callback_query(F.data == "edit")
async def edit(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer("Пришлите @username канала для изменения", reply_markup=keyb.cancle_kb)
    await state.set_state(edit_channel_state)

@router.callback_query(F.data.in_({"rus", "eng"}))
async def area(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.delete()
    lang = callback.data
    await state.set_state(info.lang)
    await state.update_data(lang=lang)
    if lang == "eng":
        await callback.message.answer("Send feedback:")
    else:
        await callback.message.answer("Отправьте отзыв:")
    await state.set_state(info.text)

@router.callback_query(F.data.in_({"🌟🌟🌟🌟🌟", "🌟🌟🌟🌟", "🌟🌟🌟", "🌟🌟", "🌟"}))
async def stars(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.delete()
    star = callback.data
    await state.set_state(info.star)
    await state.update_data(star=star)
    await final_msg(callback.message, state)



    
