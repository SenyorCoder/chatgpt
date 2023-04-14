from aiogram import types
from data.config import Kanal
from keyboards.inline.obunabol import check_button

from loader import dp, bot
from utils.misc import subscribe

#
# @dp.message_handler(commands=['start'])
# async def show_channel(message: types.Message):
#     channels_format = str()
#     for channel in Kanal:
#         chat = await bot.get_chat(channel)
#         invite_link = await chat.export_invite_link()
#
#         channels_format += f"<a href='{invite_link}'>{chat.title}</a>\n"
#
#     await message.answer(f"<b>Botdan foydalanish uchun, iltimos kanalga obuna bo'ling!👇🏻</b>",
#                          reply_markup=check_button,
#                          disable_web_page_preview=True)
#
# @dp.callback_query_handler(text="check_subs")
# async def checker(call: types.CallbackQuery):
#     await call.answer()
#     result = str()
#     for channel in Kanal:
#         status = await subscribe.check(user_id=call.from_user.id, channel=channel)
#         if status:
#             result += f"<b>😊 Ajoyib! siz kanalga obuna bo'ldingiz!</b>\n\n<i>— Savolingizni yozing</i> "
#             await call.message.delete()
#             await call.message.answer(result, disable_web_page_preview=True)
#         else:
#             result += f"Obuna bo'lmagansiz! iltimos obuna bo'ling."
#             await call.message.answer(result, disable_web_page_preview=True)





@dp.message_handler(commands=['start'])
async def show_channel(message: types.Message):
    channels_format = str()
    for channel in Kanal:
        chat = await bot.get_chat(channel)
        invite_link = await chat.export_invite_link()
        channels_format += f"<a href='{invite_link}'>{chat.title}</a>\n"
        status = await subscribe.check(user_id=message.from_user.id, channel=channel)
        if status:
            await message.answer(f"<i>Savolingizni yozing <b>ChatGPT</b> javob beradi👇🏻</i>")
        else:
            await message.answer(f"<b>Botdan foydalanish uchun, iltimos kanalga obuna bo'ling!👇🏻</b>",
                         reply_markup=check_button,
                         disable_web_page_preview=True)

@dp.callback_query_handler(text="check_subs")
async def checker(call: types.CallbackQuery):
    await call.answer()
    result = str()
    for channel in Kanal:
        status = await subscribe.check(user_id=call.from_user.id, channel=channel)
        if status:
            result += f"<b>😊 Ajoyib! siz kanalga obuna bo'ldingiz!</b>\n\n<i>— Savolingizni yozing <b>ChatGPT</b> javob berishga tayyor.</i> "
            await call.message.delete()
            await call.message.answer(result, disable_web_page_preview=True)
        else:
            result += f"<b>Obuna bo'lmagansiz! iltimos kanalga obuna bo'ling.👮🏻‍♂️👆🏻</b>"
            await call.message.answer(result, disable_web_page_preview=True)





