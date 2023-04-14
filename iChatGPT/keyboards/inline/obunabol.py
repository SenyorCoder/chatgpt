from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

check_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Kanalga obuna bo'lish 📢", url="https://t.me/teleshopuz")
        ],
        [
            InlineKeyboardButton(text="Obuna bo'ldim ✅", callback_data="check_subs")
        ]
    ]
)