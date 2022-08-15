from django.db import models

from loans.models import Loan

from .constants import TRANSACTION_TYPE_CHOICES, TRANSACTION_STATUS, PENDING
from users.models import UserBankAccount


class Transaction(models.Model):
    account = models.ForeignKey(
        UserBankAccount,
        related_name="transactions",
        on_delete=models.CASCADE,
    )
    amount = models.DecimalField(decimal_places=2, max_digits=12)
    balance_after_transaction = models.DecimalField(decimal_places=2, max_digits=12)
    transaction_type = models.PositiveSmallIntegerField(
        choices=TRANSACTION_TYPE_CHOICES
    )
    loan = models.ForeignKey(  # if this user make a loan from the bank
        Loan,
        related_name="transactions",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    status = models.PositiveSmallIntegerField(
        choices=TRANSACTION_STATUS, default=PENDING
    )
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.account.account_no)

    class Meta:
        ordering = ["timestamp"]
