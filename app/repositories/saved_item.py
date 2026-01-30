from .base_repository import BaseRepository
from models.saved_item import SavedItem


class SavedItemRepository(BaseRepository):
    model = SavedItem
