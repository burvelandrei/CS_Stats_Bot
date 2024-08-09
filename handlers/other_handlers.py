from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command

# Инициализируем роутер уровня модуля
router: Router = Router()


@router.message(Command(commands='my_id'))
async def com_help(message: Message):
    await message.answer(text=str(message.from_user.id))


# Этот хэндлер удаляет сообщения которые не обрабатываются
@router.message()
async def delete_warning_message(message: Message):
    print(message.text)
    await message.delete()