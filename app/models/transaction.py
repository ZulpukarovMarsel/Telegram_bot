import datetime

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, String
from slugify import slugify
from .base_model import BaseModel


class Type(BaseModel):
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    slug: Mapped[str] = mapped_column(unique=True, nullable=False)
    transactions: Mapped[list["Transaction"]] = relationship(back_populates="type")

    def __init__(self, **kw):
        super().__init__(**kw)
        if not self.slug and self.title:
            self.slug = slugify(self.title)

    def __repr__(self):
        return f"<Type(id={self.id}, title={self.title})>"


class Transaction(BaseModel):
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    user: Mapped["User"] = relationship(back_populates="transactions")
    amount: Mapped[int] = mapped_column(nullable=False)
    date: Mapped[datetime.datetime] = mapped_column(nullable=False, index=True)
    type_id: Mapped[int] = mapped_column(ForeignKey("types.id"), nullable=False)
    type: Mapped["Type"] = relationship(back_populates="transaction")
    description: Mapped[str | None]

    def __repr__(self):
        return f"Transaction(id={self.id})"
