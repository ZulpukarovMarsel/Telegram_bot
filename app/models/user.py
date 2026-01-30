from .base_model import BaseModel
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List


class User(BaseModel):
    username: Mapped[str] = mapped_column(unique=True, nullable=False)
    full_name: Mapped[str] = mapped_column(nullable=True)
    user_data: Mapped[List["SavedItem"]] = relationship(back_populates="user")
    reserve: Mapped[int] = mapped_column(default=0)
    balance: Mapped[int] = mapped_column(default=0)
    transactions: Mapped[List["Transaction"]] = relationship(back_populates="user")
    credits: Mapped[List["Credit"]] = relationship(back_populates="user")
    goals: Mapped[List["Goal"]] = relationship(back_populates="user")

    def __repr__(self):
        return f"<User(id={self.id}, full_name={self.full_name})>"
