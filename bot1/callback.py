from aiogram import Dispatcher,Router, F
from aiogram. types import CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State
#--
from bot1 import keyb
#--
dp = Dispatcher()
router = Router()
#--
edit_channel_state = State('edit_channel')


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