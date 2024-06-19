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

language_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Русский", callback_data="rus"),
            InlineKeyboardButton(text="English", callback_data="eng")
        ]
    ],
    resize_keyboard=True,
    selective=True
)

stars_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="🌟🌟🌟🌟🌟", callback_data="🌟🌟🌟🌟🌟")],
        [InlineKeyboardButton(text="🌟🌟🌟🌟", callback_data="🌟🌟🌟🌟")],
        [InlineKeyboardButton(text="🌟🌟🌟", callback_data="🌟🌟🌟")],
        [InlineKeyboardButton(text="🌟🌟", callback_data="🌟🌟")],
        [InlineKeyboardButton(text="🌟", callback_data="🌟")]
    ],
    resize_keyboard=True,
    selective=True
)