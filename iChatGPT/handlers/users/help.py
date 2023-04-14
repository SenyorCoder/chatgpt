from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = (f"Salom {message.from_user.full_name} bot haqida savollaringiz javobi ushbu joyda bo'lishi mumkin!👇🏻\n\n<b>1. Savol javobini bermadi yoki kech berdi:</b>\nUshbu bot ChatGPTning 3.5 versiyasida ishlaydi. Savolaringizni osson yoki qiyinligiga qarab javobni ham tez yoki sekin berishi mumkin. Shuning uchun savolingizni yozib bir oz kuting agar shunda ham javob berilmasa /start tugmasini bosing!\n\n<b>2. Javobni imlo xatolar bilan bermoqda:</b>\nChatGPT asosan ingliz tiliga mo'ljallangan hisoblanadi. Siz savolni o'zbek tilida bergan bo'lsangiz ChatGPT javobni o'zbek tiliga tarjima qilib ulashadi va shunda imlo xatolar kelib chiqishga olib keladi.\n\nAgar savolingiz javobi ushbu joyda bo'lmasa iltimos adminga murojat qiling: @Midlle_Developer")
    
    await message.answer(text)