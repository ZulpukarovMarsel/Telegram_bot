from .base_repository import BaseRepository
from models.recurring_expense import RecurringExpense, CategoryPayment


class CategoryPaymentRepository(BaseRepository):
    model = CategoryPayment


class RecurringExpenseRepository(BaseRepository):
    model = RecurringExpense
