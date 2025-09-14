from aiogram import Router

from .create import advertisement_create_router


advertisement_router = Router(name=__name__)
advertisement_router.include_routers(
    advertisement_create_router,
)
