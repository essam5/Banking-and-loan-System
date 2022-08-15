from http.client import ACCEPTED


FLAT_RATE = 1
REDUCING_BALANCE = 2

INTEREST_TYPE_CHOICES = (
    (FLAT_RATE, "flate_rate"),
    (REDUCING_BALANCE, "reduncing_balance"),
)

ACCEPTED = 1
PENDING = 2
REJECTED = 3

LOAN_STATUS = (
    (ACCEPTED, "accepted"),
    (PENDING, "pending"),
    (REJECTED, "rejected"),
)

FEE_CHARGE_METHOD_CHOICES = (
    (1, "Deduct from principal balance"),
    (2, "Add the fee on top of the loan"),
)

DAILY = 1
MONTHLY = 2
QUARTERLY = 3
BI_ANNUAL = 4
YEARLY = 5

PAYMENT_FREQUENCY_CHOICES = (
    (DAILY, "daily"),
    (MONTHLY, "monthly"),
    (QUARTERLY, "quarterly"),
    (BI_ANNUAL, "bi-annual"),
    (YEARLY, "yearly"),
)

CASH = 1
BANK = 2

PAYMENT_METHOD = (
    (CASH, "cash"),
    (BANK, "bank"),
)
