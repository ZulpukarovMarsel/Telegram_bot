from config.config import dp, token, db
from app.config.db import Base
from app.commands.commands import *  

from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from sqlalchemy import create_engine

import asyncio
import logging
import sys


engine = create_engine(db)


async def main() -> None:
    Base.metadata.create_all(engine)
    logging.info("Database tables created successfully.")

    bot = Bot(token=token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        stream=sys.stdout,
    )
    asyncio.run(main())
