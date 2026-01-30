from datetime import date
from sqlalchemy import ForeignKey, String, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base_model import BaseModel


class Credit(BaseModel):
    title: Mapped[str] = mapped_column(String(255), nullable=True)
    amount: Mapped[int] = mapped_column(default=0)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    user: Mapped["User"] = relationship(back_populates="credits")
    due_date: Mapped[date] = mapped_column(Date, nullable=False, index=True)
    day_of_month: Mapped[int] = mapped_column(nullable=False)

    def __repr__(self):
        return f"<Credit(id={self.id}, title={self.title})>"
