import logging
from aiogram import types
from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware

from data.config import Kanal
from keyboards.inline.obunabol import check_button
from utils.misc import subscribe
from loader import bot


class BigBrother(BaseMiddleware):
    async def on_pre_process_update(self, update: types.Update, data: dict):
        if update.message:
            user = update.message.from_user.id
            if update.message.text in ['/start', '/help']:
                return
        elif update.callback_query:
            user = update.callback_query.from_user.id
            if update.callback_query.data == "check_subs":
                return
        else:
            return

        final_status = True
        for channel in Kanal:
            status = await subscribe.check(user_id=user,
                                              channel=channel)
            final_status *= status
            # channel = await bot.get_chat(channel)
            if not status:
                await update.message.answer(f"<b>Botdan foydalanish uchun, iltimos kanalga obuna bo'ling!👇🏻</b>",
                                     reply_markup=check_button,
                                     disable_web_page_preview=True)


        if not final_status:
            await update.message.answer(disable_web_page_preview=True)
            raise CancelHandler()