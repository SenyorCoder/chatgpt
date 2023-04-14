from aiogram import types, Bot

from keyboards.inline.linklar import havola
from loader import dp
from chatgpt import text
from aiogram.dispatcher.filters import Text
import asyncio
from aiogram.types import ChatActions

# @dp.message_handler(Text)
# async def send(message: types.Message):
#     natija = text(message.text)
#     await message.answer(f"{natija}")
# bot = Bot("6077126509:AAGHXpanNgDxq3tCHo8UCfqdbW66DqjMceI")



@dp.message_handler(Text)
async def atvet(message: types.Message):
    kutish = await message.answer_sticker("CAACAgIAAxkBAAEIkF5kN-9g0mBsf0eVSBdCjt23dVxdZQACxwoAAvxlAUrfEkMNGcJAQS8E")
    natija = text(message.text)
    if natija:
        await message.answer(f"{natija}\n\n@iChatGPTuz_bot", reply_markup=havola)
        await kutish.delete()
    else:
        await kutish.delete()
        await message.answer(f"<b>{message.from_user.full_name}</b> Iltimos bir ozdan so'ng qayta urunib ko'ring yoki /start bosing.")


