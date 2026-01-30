from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, String
from .base_model import BaseModel


class Goal(BaseModel):
    title: Mapped[str] = mapped_column(String(255))
    amount: Mapped[int] = mapped_column(default=0)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship(back_populates="goals")
    priority: Mapped[int] = mapped_column(default=0)

    def __repr__(self):
        return f"<Goal(id={self.id}), title={self.title}>"
