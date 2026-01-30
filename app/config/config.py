from aiogram import Dispatcher
from decouple import config

token = config('TOKEN')
dp = Dispatcher()

db = config('DATABASE_URL_TEST')
