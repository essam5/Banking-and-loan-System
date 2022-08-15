DEPOSIT = 1
WITHDRAWAL = 2
INTEREST = 3

TRANSACTION_TYPE_CHOICES = (
    (DEPOSIT, "Deposit"),
    (WITHDRAWAL, "Withdrawal"),
    (INTEREST, "Interest"),
)

ACCEPTED = 1
PENDING = 2
REJECTED = 3

TRANSACTION_STATUS = (
    (ACCEPTED, "accepted"),
    (PENDING, "pending"),
    (REJECTED, "rejected"),
)
