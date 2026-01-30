from .base_repository import BaseRepository
from models.goal import Goal


class GaolRepository(BaseRepository):
    model = Goal
