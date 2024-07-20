from __future__ import annotations

from dataclasses import dataclass
from environs import Env


@dataclass
class TgBot:
    token: str  # Токен для доступа к телеграм-боту
    admin_ids: list[int]  # Список id администраторов бота
    server: str  # Сервер панели
    server_pc: str
    yoo_id: str
    yoo_token: str
    login_M_M: str
    login_M_P: str
    password_M_M: str
    password_M_P: str
    login_bd: str
    password_bd: str
    server_bd: str
    honest_bonus: int
    day_sum: int



@dataclass
class Config:
    tg_bot: TgBot


def load_config(path: str | None = None) -> Config:

    env: Env = Env()
    env.read_env(path)

    return Config(tg_bot=TgBot(token=env('BOTV_TOKEN'),
                               admin_ids=list(map(int, env.list('ADMIN_IDS'))),
                               server=env('SERVER'),
                               server_pc=env('SERVER_PC'),
                               yoo_id=env('yoo_id'),
                               yoo_token=env('yoo_token'),
                               login_M_M=env('login_M_M'),
                               login_M_P=env('login_M_P'),
                               password_M_M=env('password_M_M'),
                               password_M_P=env('password_M_P'),
                               login_bd=env('login_bd'),
                               password_bd=env('password_bd'),
                               server_bd=env('server_bd'),
                               honest_bonus=env('honest_bonus'),
                               day_sum=env('day_sum')
                               )
                  )

