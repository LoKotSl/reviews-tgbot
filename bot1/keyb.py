from aiogram. types import  (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
                            )

start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Получить ссылку"),
            KeyboardButton(text="Добавить канал")
        ]     
    ],
    input_field_placeholder="↓Выберите действие из панели↓",
    resize_keyboard=True,
    selective=True
)

addchanel_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Добавить канал")
        ]
    ]
)

cancle_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Отмена", callback_data="сancle")
        ]
    ]
)


editchan_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Изменить канал", callback_data="edit")
        ]
    ]
)