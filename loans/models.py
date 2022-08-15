from django.db import models
from . import constants
from users.models import UserBankAccount, ExtendUser


class loanType(models.Model):
    name = models.CharField(max_length=50)
    rate = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()
    need_collateral = models.BooleanField(
        help_text="does this type of Loan need Coollateral"
    )
    need_guarantor = models.BooleanField(
        help_text="does this type of loan need a gurantor"
    )
    market = models.CharField(
        null=True,
        help_text="these include the category of people who will be interested in this particular product",
        max_length=50,
    )
    min_amount_allowed = models.DecimalField(
        decimal_places=2, max_digits=12, null=True, blank=True
    )  # null means that any price
    max_amount_allowed = models.DecimalField(
        decimal_places=2, max_digits=12, null=True, blank=True
    )  # min price must not be more than maximum price
    interest_type = models.PositiveSmallIntegerField(
        choices=constants.INTEREST_TYPE_CHOICES
    )


class Loan(models.Model):
    status = models.PositiveSmallIntegerField(
        choices=constants.LOAN_STATUS, default=constants.PENDING
    )
    user = models.ForeignKey(ExtendUser, on_delete=models.CASCADE)
    amount = models.DecimalField(decimal_places=2, max_digits=12)
    currency = models.CharField(max_length=10)
    preferred_payment_date = models.DateField(null=True, blank=True)
    payment_method = models.PositiveSmallIntegerField(
        choices=constants.PAYMENT_METHOD, default=constants.CASH
    )
    bank_account = models.ForeignKey(
        UserBankAccount,
        on_delete=models.CASCADE,
        null=True,
        related_name="loan_payment_account",
    )
    loan_type = models.ForeignKey(loanType, on_delete=models.CASCADE)
    tenure = models.IntegerField(null=True)
    tenure_qualifier = models.CharField(max_length=50, null=True, blank=True)
    issue_date = models.DateField(null=True)
    payment_frequency = models.PositiveSmallIntegerField(
        choices=constants.PAYMENT_FREQUENCY_CHOICES, default=constants.MONTHLY
    )
    fee = models.IntegerField(null=True, blank=True)
    fee_charge_method = models.PositiveSmallIntegerField(
        null=True, blank=True, choices=constants.FEE_CHARGE_METHOD_CHOICES
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
