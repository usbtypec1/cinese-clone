from aiogram import Router, F
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message
from dishka import FromDishka

from application.queries.list_categories import ListCategoriesQuery
from application.queries.list_cities import ListCitiesQuery
from presentation.telegram.filters.callback_data.advertisement.create import \
    AdvertisementTypeCallbackData, AdvertisementCategoryCallbackData, \
    AdvertisementDeliveryOptionCallbackData, AdvertisementCityCallbackData, \
    AdvertisementPhoneNumberVisibilityCallbackData
from presentation.telegram.filters.states import AdvertisementCreateStates
from presentation.telegram.ui.views.advertisement import (
    AdvertisementTypeListView, AdvertisementCategoryListView,
    AdvertisementProductTitleView, AdvertisementProductDescriptionView,
    AdvertisementProductPhotosView, AdvertisementProductPriceView,
    AdvertisementDeliveryOptionView, AdvertisementCityListView,
    AdvertisementPhoneNumberView, AdvertisementCreateConfirmView,
)
from presentation.telegram.ui.views.base import answer_view, \
    edit_message_by_view


advertisement_create_router = Router(name=__name__)


@advertisement_create_router.callback_query(
    AdvertisementPhoneNumberVisibilityCallbackData.filter(),
    StateFilter(AdvertisementCreateStates.phone_number_visibility),
)
async def on_advertisement_phone_number_visibility_chosen(
    callback_query: CallbackQuery,
    callback_data: AdvertisementPhoneNumberVisibilityCallbackData,
    state: FSMContext,
) -> None:
    await state.update_data(
        is_phone_number_visible=callback_data.is_visible,
    )
    await state.set_state(AdvertisementCreateStates.confirm)
    data = await state.get_data()
    print(data)
    view = AdvertisementCreateConfirmView()
    await answer_view(callback_query.message, view)


@advertisement_create_router.callback_query(
    AdvertisementCityCallbackData.filter(),
)
async def on_advertisement_city_chosen(
    callback_query: CallbackQuery,
    callback_data: AdvertisementCityCallbackData,
    state: FSMContext,
) -> None:
    view = AdvertisementPhoneNumberView()
    await state.update_data(city_id=callback_data.city_id)
    await state.set_state(AdvertisementCreateStates.phone_number_visibility)
    await answer_view(callback_query.message, view)


@advertisement_create_router.callback_query(
    AdvertisementDeliveryOptionCallbackData.filter(),
    StateFilter(AdvertisementCreateStates.delivery_option),
)
async def on_advertisement_delivery_option_chosen(
    callback_query: CallbackQuery,
    callback_data: AdvertisementDeliveryOptionCallbackData,
    state: FSMContext,
    list_cities_query: FromDishka[ListCitiesQuery],
) -> None:
    cities_list_response = await list_cities_query.execute()
    view = AdvertisementCityListView(cities_list_response.cities)
    await state.update_data(advertisement_delivery_option=callback_data.option)
    await state.set_state(AdvertisementCreateStates.city)
    await answer_view(callback_query.message, view)


@advertisement_create_router.message(
    F.text,
    StateFilter(AdvertisementCreateStates.price),
)
async def on_advertisement_price_entered(
    message: Message,
    state: FSMContext,
) -> None:
    await state.update_data(advertisement_price=message.text)
    await state.set_state(AdvertisementCreateStates.delivery_option)
    view = AdvertisementDeliveryOptionView()
    await answer_view(message, view)


@advertisement_create_router.message(
    F.photo,
    StateFilter(AdvertisementCreateStates.photos),
)
async def on_advertisement_photos_entered(
    message: Message,
    state: FSMContext,
) -> None:
    data = await state.get_data()
    advertisement_photos = data.get('advertisement_photos', [])
    advertisement_photos.append(message.photo[-1].file_id)
    await state.update_data(advertisement_photos=advertisement_photos)
    await state.set_state(AdvertisementCreateStates.price)
    view = AdvertisementProductPriceView()
    await answer_view(message, view)


@advertisement_create_router.message(
    F.text,
    StateFilter(AdvertisementCreateStates.description),
)
async def on_advertisement_description_entered(
    message: Message,
    state: FSMContext,
) -> None:
    await state.update_data(advertisement_description=message.text)
    await state.set_state(AdvertisementCreateStates.photos)
    view = AdvertisementProductPhotosView()
    await answer_view(message, view)


@advertisement_create_router.message(
    F.text,
    StateFilter(AdvertisementCreateStates.title),
)
async def on_advertisement_title_entered(
    message: Message,
    state: FSMContext,
) -> None:
    await state.update_data(advertisement_title=message.text)
    await state.set_state(AdvertisementCreateStates.description)
    view = AdvertisementProductDescriptionView()
    await answer_view(message, view)


@advertisement_create_router.callback_query(
    AdvertisementCategoryCallbackData.filter(),
    StateFilter(AdvertisementCreateStates.category),
)
async def on_advertisement_category_chosen(
    callback_query: CallbackQuery,
    callback_data: AdvertisementCategoryCallbackData,
    state: FSMContext,
) -> None:
    await state.update_data(
        advertisement_category_id=callback_data.category_id,
    )
    await state.set_state(AdvertisementCreateStates.title)
    view = AdvertisementProductTitleView()
    await edit_message_by_view(callback_query.message, view)


@advertisement_create_router.callback_query(
    AdvertisementTypeCallbackData.filter(),
    StateFilter(AdvertisementCreateStates.type),
)
async def on_advertisement_type_chosen(
    callback_query: CallbackQuery,
    callback_data: AdvertisementTypeCallbackData,
    state: FSMContext,
    list_category_query: FromDishka[ListCategoriesQuery],
) -> None:
    await state.update_data(advertisement_type=callback_data.type)
    await state.set_state(AdvertisementCreateStates.category)
    category_list_response = await list_category_query.execute()
    view = AdvertisementCategoryListView(category_list_response.categories)
    await edit_message_by_view(callback_query.message, view)


@advertisement_create_router.callback_query(
    F.data == 'create_advertisement',
)
async def on_create_advertisement(
    callback_query: CallbackQuery,
    state: FSMContext,
) -> None:
    view = AdvertisementTypeListView()
    await state.set_state(AdvertisementCreateStates.type)
    await edit_message_by_view(callback_query.message, view)
