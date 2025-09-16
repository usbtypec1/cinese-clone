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


class PhotoView(ABC):
    photo: str | None = None
    caption: str | None = None
    reply_markup: ReplyMarkup | None = None

    def get_photo(self) -> str | None:
        return self.photo

    def get_caption(self) -> str | None:
        return self.caption

    def get_reply_markup(self) -> ReplyMarkup | None:
        return self.reply_markup


class TextView(ABC):
    text: str | None = None
    reply_markup: ReplyMarkup | None = None

    def get_text(self) -> str | None:
        return self.text

    def get_reply_markup(self) -> ReplyMarkup | None:
        return self.reply_markup


type View = TextView | PhotoView


async def answer_text_view(message: Message, view: TextView) -> Message:
    return await message.answer(
        text=view.get_text(),
        reply_markup=view.get_reply_markup(),
    )


async def answer_photo_view(message: Message, view: PhotoView) -> Message:
    return await message.answer_photo(
        photo=view.get_photo(),
        caption=view.get_caption(),
        reply_markup=view.get_reply_markup(),
    )


async def answer_view(message: Message, view: View) -> Message:
    match view:
        case TextView():
            return await answer_text_view(message=message, view=view)
        case PhotoView():
            return await answer_photo_view(message=message, view=view)


async def edit_message_by_view(
    message: Message,
    view: TextView,
) -> Message:
    return await message.edit_text(
        text=view.get_text(),
        reply_markup=view.get_reply_markup(),
    )
