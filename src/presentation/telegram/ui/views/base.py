from abc import ABC

from aiogram.types import (
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    ForceReply,
    Message,
)


type ReplyMarkup = (
    InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply
)


class TextView(ABC):
    text: str | None = None
    reply_markup: ReplyMarkup | None = None

    def get_text(self) -> str | None:
        return self.text

    def get_reply_markup(self) -> ReplyMarkup | None:
        return self.reply_markup


type View = TextView


async def answer_text_view(message: Message, view: TextView) -> Message:
    return await message.answer(
        text=view.get_text(),
        reply_markup=view.get_reply_markup(),
    )


async def answer_view(message: Message, view: View) -> Message:
    match view:
        case TextView():
            return await answer_text_view(message=message, view=view)


async def edit_message_by_view(
    message: Message,
    view: View,
) -> Message:
    match view:
        case TextView():
            return await message.edit_text(
                text=view.get_text(),
                reply_markup=view.get_reply_markup(),
            )
