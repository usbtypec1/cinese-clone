from aiogram.types import TelegramObject, Message, CallbackQuery
from dishka import Provider, provide, Scope

from application.common.types import CurrentUserId


class PresentationProvider(Provider):

    @provide(scope=Scope.REQUEST)
    def provide_current_user_id(self, obj: TelegramObject) -> CurrentUserId:
        if isinstance(obj, Message):
            return CurrentUserId(obj.from_user.id)
        if isinstance(obj, CallbackQuery):
            return CurrentUserId(obj.from_user.id)
        raise TypeError(f"Unsupported type: {type(obj)}")
