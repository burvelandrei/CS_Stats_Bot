import asyncio
import logging
import logging.config
from datetime import datetime

# from logging_data.logging_settings import logging_config

# from aiogram import Bot, Dispatcher
# from aiogram_dialog import setup_dialogs

# from config_data.config import Config, load_config
# from handlers import other_handlers, owner_handlers, sheduler_distribution, admin_handlers
# from apscheduler.schedulers.asyncio import AsyncIOScheduler

# from handlers.admin.Main import main_dialog_owner
# from handlers.admin.WorkingClients import working_clients_dialog
# from handlers.admin.Promocode import promocode_dialog
# from handlers.admin.SendMessages import send_messages_dialog
# from handlers.admin.Service_script import servise_script_dialog
# from handlers.admin.AdmMenu import AdmMain, AdmPromocode, AdmSendMessages, AdmWorkingClients
# from handlers.admin.MngMenu import MngMain, MngWorkingClients
# from keyboards.set_menu import set_main_menu
# from aiogram.fsm.storage.redis import RedisStorage, DefaultKeyBuilder
# from apscheduler.jobstores.redis import RedisJobStore
# from apscheduler_di import ContextSchedulerDecorator
# from middlewares.apscheduler_m import SchedulerMiddleware

# Инициализируем логгер
logger = logging.getLogger(__name__)


# Функция конфигурирования и запуска бота
async def main() -> None:
    # Кофигурируем логирование с помощью словаря
    # logging.config.dictConfig(logging_config)

    # Выводим в консоль информацию о начале запуска
    # logger.info('Starting BOTV')

    # # Загружаем конфиг в переменную config
    # config: Config = load_config()

    # # Инициализируем бот и диспетчер
    # bot: Bot = Bot(token=config.tg_bot.token, parse_mode='HTML')
    # storage = RedisStorage.from_url('redis://localhost:6379/0', key_builder=DefaultKeyBuilder(with_destiny=True))
    # dp: Dispatcher = Dispatcher(storage=storage)
    # jobstores = {
    #     'default': RedisJobStore(
    #         jobs_key='dispatched_trips_jobs',
    #         run_times_key='dispatched_trips_running',
    #         host='localhost',
    #         db=2,
    #         port=6379
    #     )
    # }

    # # Настраиваем кнопку Menu
    # await set_main_menu(bot)
    # # Сообщения по расписанию
    # scheduler = ContextSchedulerDecorator(AsyncIOScheduler(timezone="Europe/Moscow", jobstores=jobstores))
    # scheduler.ctx.add_instance(bot, declared_class=Bot)
    # scheduler.start()
    # try:
    #     scheduler.remove_job('balance')
    # except:
    #     pass
    # try:
    #     scheduler.remove_job('before_pay')
    # except:
    #     pass
    # try:
    #     scheduler.remove_job('no_connect_vpn')
    # except:
    #     pass
    # try:
    #     scheduler.remove_job('days_stop_use')
    # except:
    #     pass
    # scheduler.add_job(sheduler_distribution.balanse, id='balance', trigger='cron', hour=00,
    #                   minute=1, start_date=datetime.now())
    # scheduler.add_job(sheduler_distribution.before_pay, id='before_pay', trigger='cron', hour=10,
    #                   minute=00, start_date=datetime.now())
    # scheduler.add_job(sheduler_distribution.no_connect_vpn, id='no_connect_vpn', trigger='cron', hour=12,
    #                   minute=00, start_date=datetime.now())
    # scheduler.add_job(sheduler_distribution.thirty_days_stop_use, id='days_stop_use', trigger='cron', hour=11,
    #                   minute=00, start_date=datetime.now())
    # # scheduler.start()

    # # Регистриуем роутеры в диспетчере
    # dp.update.middleware.register(SchedulerMiddleware(scheduler))
    # dp.include_router(admin_handlers.router)
    # dp.include_router(owner_handlers.router)
    # dp.include_router(working_clients_dialog)
    # dp.include_router(send_messages_dialog)
    # dp.include_router(promocode_dialog)
    # dp.include_router(main_dialog_owner)
    # dp.include_router(servise_script_dialog)
    # dp.include_router(AdmMain.admin_dialog_owner)
    # dp.include_router(AdmPromocode.promocode_dialog)
    # dp.include_router(AdmSendMessages.send_messages_dialog)
    # dp.include_router(AdmWorkingClients.working_clients_dialog)
    # dp.include_router(MngMain.manager_dialog_owner)
    # dp.include_router(MngWorkingClients.working_clients_dialog)
    # dp.include_router(other_handlers.router)
    # setup_dialogs(dp)

    # # Пропускаем накопившиеся апдейты и запускаем polling
    # await bot.delete_webhook(drop_pending_updates=True)
    # try:
    #     await dp.start_polling(bot)
    # except Exception as ex:
    #     logging.error(f'[Exception] - {ex}', exc_info=True)
    # finally:
    #     await bot.session.close()
    pass


if __name__ == '__main__':
    asyncio.run(main())
