from .base_repository import BaseRepository
from models.credit import Credit


class CreditRepository(BaseRepository):
    model = Credit
