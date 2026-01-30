from config.config import dp, db
from app.config.db import Base
from aiogram.filters import CommandStart
from aiogram.types import Message

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine(db)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Привет, {message.from_user.username}! Что хотели?")
