from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String
from slugify import slugify
from .base_model import BaseModel


class SavedItem(BaseModel):
    user: Mapped["User"] = relationship(back_populates="user_data")
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    content: Mapped[str] = mapped_column(nullable=False)
    slug: Mapped[str] = mapped_column(unique=True, nullable=False)

    def __init__(self, **kw):
        super().__init__(**kw)
        if not self.slug and self.title:
            self.slug = slugify(self.title)

    def __repr__(self):
        return f"<SavedItem(id={self.id}, title={self.title})>"
