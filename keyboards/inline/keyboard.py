from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from aiogram.utils.keyboard import InlineKeyboardBuilder
from lexicon import lexicon_owner


# Функция генератор клавиатуры с параметром количества кнопок в строке
def generate_inline_keyboard(
    width: int, *args: str, lst_button: str | None = None, **kwargs: str
) -> InlineKeyboardMarkup:
    kb_builder = InlineKeyboardBuilder()

    buttons: list[InlineKeyboardButton] = []

    if args:
        for button in args:
            buttons.append(
                InlineKeyboardButton(
                    text=(
                        lexicon_owner.LEXICON_GENERAL_COMMANDS[button]
                        if button in lexicon_owner.LEXICON_GENERAL_COMMANDS
                        else button
                    ),
                    callback_data=button,
                )
            )

    if kwargs:
        for button, text in kwargs.items():
            buttons.append(InlineKeyboardButton(text=text, callback_data=button))

    kb_builder.row(*buttons, width=width)

    if lst_button:
        kb_builder.row(
            InlineKeyboardButton(text=lst_button, callback_data="lst_button")
        )

    return kb_builder.as_markup()


# Функция генератор клавиатуры для персонального меню
def generate_personal_account_keyboard(
    width: int, *args: str, lst_button: str | None = None, **kwargs: str
) -> InlineKeyboardMarkup:
    kb_builder = InlineKeyboardBuilder()

    buttons: list[InlineKeyboardButton] = []

    if kwargs:
        for button, text in kwargs.items():
            buttons.append(
                InlineKeyboardButton(
                    text=lexicon_owner.LEXICON_PERSONAL_ACCOUNT_COMMANDS[text].format(
                        key=button
                    ),
                    callback_data=f"key_{button}_{text}",
                )
            )

    if args:
        for button in args:
            buttons.append(
                InlineKeyboardButton(
                    text=(
                        lexicon_owner.LEXICON_PERSONAL_ACCOUNT_COMMANDS[button]
                        if button in lexicon_owner.LEXICON_PERSONAL_ACCOUNT_COMMANDS
                        else button
                    ),
                    callback_data=button,
                )
            )

    kb_builder.row(*buttons, width=width)

    if lst_button:
        kb_builder.row(
            InlineKeyboardButton(text=lst_button, callback_data="lst_button")
        )

    return kb_builder.as_markup()


# Функция генератор клавиатуры для меню поплнения баланса
def generate_add_balance_keyboard(
    width: int, *args: str, lst_button: str | None = None, **kwargs: str
) -> InlineKeyboardMarkup:
    kb_builder = InlineKeyboardBuilder()

    buttons: list[InlineKeyboardButton] = []

    if args:
        for button in args:
            buttons.append(
                InlineKeyboardButton(
                    text=(
                        lexicon_owner.LEXICON_ADD_BALANCE_COMMANDS[button]
                        if button in lexicon_owner.LEXICON_ADD_BALANCE_COMMANDS
                        else button
                    ),
                    callback_data=button,
                )
            )

    if kwargs:
        for button, text in kwargs.items():
            buttons.append(InlineKeyboardButton(text=text, callback_data=button))

    kb_builder.row(*buttons, width=width)

    if lst_button:
        kb_builder.row(
            InlineKeyboardButton(text=lst_button, callback_data="lst_button")
        )

    return kb_builder.as_markup()


# Функция генератор клавиатуры для меню подключения
def generate_connect_key(
    width: int,
    url_button: str | None = None,
    *args: str,
) -> InlineKeyboardMarkup:
    kb_builder = InlineKeyboardBuilder()

    buttons: list[InlineKeyboardButton] = []

    if url_button:
        kb_builder.row(
            InlineKeyboardButton(
                text=(
                    lexicon_owner.LEXICON_CONNECT_KEY_COMMANDS["connect_this_device"]
                ),
                url=url_button,
            )
        )

    if args:
        for button in args:
            buttons.append(
                InlineKeyboardButton(
                    text=(
                        lexicon_owner.LEXICON_CONNECT_KEY_COMMANDS[button]
                        if button in lexicon_owner.LEXICON_CONNECT_KEY_COMMANDS
                        else button
                    ),
                    callback_data=button,
                )
            )

    kb_builder.row(*buttons, width=width)

    return kb_builder.as_markup()


# Функция генератор клавиатуры для меню единоразовой оплаты
def generate_one_time_pay(
    adjust: list,
    **kwargs: str,
) -> InlineKeyboardMarkup:
    kb_builder = InlineKeyboardBuilder()

    buttons: list[InlineKeyboardButton] = []

    if kwargs:
        for button, text in kwargs.items():
            buttons.append(InlineKeyboardButton(text=text, callback_data=button))

    kb_builder.row(*buttons)
    kb_builder.adjust(*adjust)

    return kb_builder.as_markup()


# Функция генератор клавиатуры для меню помощи и меню разморозки без баланса
def generate_link(
    width: int,
    **kwargs: str,
) -> InlineKeyboardMarkup:
    kb_builder = InlineKeyboardBuilder()

    buttons: list[InlineKeyboardButton] = []

    if kwargs:
        for button, text in kwargs.items():
            if button in lexicon_owner.LEXICON_CONTACTS:
                buttons.append(
                    InlineKeyboardButton(
                        text=text, url=lexicon_owner.LEXICON_CONTACTS[button]
                    )
                )
            else:
                buttons.append(InlineKeyboardButton(text=text, callback_data=button))
    kb_builder.row(*buttons, width=width)

    return kb_builder.as_markup()


# Функция генератор для меню оплатить
def create_link(link, last_btn: str | None = None, last1_btn: str | None = None):
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    if last_btn:
        kb_builder.row(InlineKeyboardButton(text=last_btn, url=link))
    if last1_btn:
        kb_builder.row(InlineKeyboardButton(text=last1_btn, callback_data=last1_btn))
    return kb_builder.as_markup()


start_menu = generate_inline_keyboard(1, **lexicon_owner.LEXICON_START_MENU_COMMANDS)
start_menu_re = generate_inline_keyboard(
    1, **lexicon_owner.LEXICON_START_MENU_COMMANDS_RE
)
check_promocode_menu = generate_inline_keyboard(
    2, **lexicon_owner.LEXICON_CHECK_PROMOCODE_COMMANDS
)
yes_promocode_menu = generate_inline_keyboard(1, **lexicon_owner.LEXICON_YES_PROMOCODE)
not_valid_promocode = generate_inline_keyboard(
    1, **lexicon_owner.LEXICON_NOT_VALID_PROMOCODE_COMMANDS
)
was_input_promocode = generate_inline_keyboard(
    1, **lexicon_owner.LEXICON_WAS_INPUT_COMMANDS
)
confirmation_add_key = generate_inline_keyboard(
    1, **lexicon_owner.LEXICON_CONFIRMATION_ADD_KEY
)
add_key = generate_inline_keyboard(2, **lexicon_owner.LEXICON_ADD_KEY_COMMANDS)
another_device_menu = generate_inline_keyboard(
    1, **lexicon_owner.LEXICON_ANOTHER_DEVICE_COMMANDS
)
support_menu = generate_link(1, **lexicon_owner.LEXICON_SUPPORT_COMMANDS)
active_key_menu = generate_inline_keyboard(
    1, **lexicon_owner.LEXICON_CONTROL_ACTIVE_KEY_COMMANDS
)
freeze_key_menu = generate_inline_keyboard(
    1, **lexicon_owner.LEXICON_CONTROL_FREEZE_KEY_COMMANDS
)
freeze_menu = generate_inline_keyboard(1, **lexicon_owner.LEXICON_FREEZE_COMMANDS)
unfreeze_menu_positive_balance = generate_link(
    1, **lexicon_owner.LEXICON_UNFREEZE_POZITIVE_COMMANDS
)
unfreeze_menu_negative_balance = generate_inline_keyboard(
    1, **lexicon_owner.LEXICON_UNFREEZE_NEGATIVE_COMMANDS
)
delete_menu = generate_inline_keyboard(1, **lexicon_owner.LEXICON_DELETE_COMMANDS)
referal_menu = generate_inline_keyboard(1, **lexicon_owner.LEXICON_REFERAL_MENU)
history_pay = generate_inline_keyboard(1, **lexicon_owner.LEXICON_HISTORY_PAY_COMMANDS)
all_history = generate_inline_keyboard(1, **lexicon_owner.LEXICON_ALL_HISTORY_COMMANDS)
three_days_later = generate_inline_keyboard(
    1, **lexicon_owner.LEXICON_THREE_DAYS_LATER_COMMANDS
)
answer_no_vpn = generate_inline_keyboard(1, *["input_answer_no_vpn"])
answer_stop_use = generate_inline_keyboard(1, *["input_answer_stop_use"])
no_vpn_kb = generate_inline_keyboard(1, **lexicon_owner.LEXICON_NO_VPN_COMMANDS)
stop_use_kb = generate_inline_keyboard(1, **lexicon_owner.LEXICON_STOP_USE_COMMANDS)
successful_payment = generate_inline_keyboard(
    1, **lexicon_owner.LEXICON_SUCCESSFUL_PAYMENT
)
freeze_successful_payment = generate_inline_keyboard(
    1, **lexicon_owner.LEXICON_FREEZE_SUCCESSFUL_PAYMENT
)
distribution_admin = generate_inline_keyboard(
    1, **lexicon_owner.LEXICON_DISTRIBUTION_ADMIN_COMMANDS
)
