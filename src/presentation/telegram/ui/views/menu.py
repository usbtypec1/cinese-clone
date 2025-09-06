from aiogram.types import User

from presentation.telegram.ui.views.base import TextView


class MenuView(TextView):
    
    def __init__(self, user: User):
        self.user = user
    
    def get_text(self) -> str:
        return (
            f""
        )