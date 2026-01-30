from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, String
from slugify import slugify

from .base_model import BaseModel


class CategoryPayment(BaseModel):
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    slug: Mapped[str] = mapped_column(unique=True, nullable=False)
    recurring_expenses: Mapped[list["RecurringExpense"]] = relationship(back_populates="category")

    def __init__(self, **kw):
        super().__init__(**kw)
        if not self.slug and self.title:
            self.slug = slugify(self.title)

    def __repr__(self):
        return f"<Type(id={self.id}, title={self.title})>"


class RecurringExpense(BaseModel):
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    user: Mapped["User"] = relationship(back_populates="user")
    amount: Mapped[int] = mapped_column(default=0)
    day_of_month: Mapped[int] = mapped_column(default=0)
    category_id: Mapped[int] = mapped_column(ForeignKey(""))
    category: Mapped["CategoryPayment"] = relationship(back_populates="recurring_expenses")
    is_active: Mapped[bool] = mapped_column(default=True)

    def __repr__(self):
        return f"<RecurringExpense(id={self.id}, amount={self.amount})>"
