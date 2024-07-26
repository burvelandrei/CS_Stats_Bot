from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from lexicon.lexicon_owner import LEXICON_MAIN_MENU, LEXICON_MAIN_MENU_ADMIN, LEXICON_MAIN_MENU_OWNER, \
    LEXICON_MAIN_MENU_MANAGER


def gen_kb(adjust: list,
           *args: str,
           lst_button: str|None = None,
           **kwargs: str) -> ReplyKeyboardMarkup:

    kb_builder = ReplyKeyboardBuilder()

    buttons: list[KeyboardButton] = []

    if args:
        for button in args:
            buttons.append(KeyboardButton(
                text=LEXICON_MAIN_MENU[button] if button in LEXICON_MAIN_MENU else button
            ))

    if kwargs:
        for text in kwargs.values():
            buttons.append(KeyboardButton(
                text=text
            ))

    kb_builder.row(*buttons, width=1)
    kb_builder.adjust(*adjust)

    if lst_button:
        kb_builder.row(KeyboardButton(
            text=lst_button
            ))

    return kb_builder.as_markup(
        resize_keyboard=True,
        one_time_keyboard=False
        )

main_menu = gen_kb([2, 3, 1], **LEXICON_MAIN_MENU) # изменить если вернёться кнопка популярные вопросы [1, 3, 2]
main_menu_owner = gen_kb([2, 3, 1, 1], **LEXICON_MAIN_MENU_OWNER)
main_menu_admin = gen_kb([2, 3, 1, 1], **LEXICON_MAIN_MENU_ADMIN)
main_menu_manager = gen_kb([2, 3, 1, 1], **LEXICON_MAIN_MENU_MANAGER)