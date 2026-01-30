from .base_repository import BaseRepository
from models.transaction import Transaction, Type


class TypeRepository(BaseRepository):
    model = Type


class TransactionRepository(BaseRepository):
    model = Transaction
