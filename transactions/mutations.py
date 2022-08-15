import graphene

from . import models, types
from graphql_relay import from_global_id


class TransactionType(graphene.Enum):
    DEPOSIT = 1
    WITHDRAWAL = 2
    INTEREST = 3


class TransactionStatus(graphene.Enum):
    ACCEPTED = 1
    PENDING = 2
    REJECTED = 3


class TransactionCreateInput(graphene.InputObjectType):
    amount = graphene.Decimal(description="amount of transaction", required=True)
    balance_after_transaction = graphene.Decimal(
        description="balance_after_transaction", required=True
    )
    transaction_type = TransactionType(description="transaction_type", required=False)


class TransactionCreateMutation(graphene.Mutation):
    class Arguments:
        user_bank_account = graphene.ID(
            required=True, description="user bank account ID"
        )
        input = TransactionCreateInput(
            required=True, description="Field required to create Transaction "
        )

    transaction = graphene.Field(types.TransactionNode)
    success = graphene.Boolean()

    @classmethod
    def mutate(cls, root, info, user_bank_account, input):
        success = False
        user = info.context.user
        if user.is_staff:
            type, id = from_global_id(user_bank_account)
            bank_account = models.UserBankAccount.objects.get(id=id)
            transaction = models.Transaction.objects.create(
                **input, account=bank_account
            )
            if transaction:
                success = True
        return TransactionCreateMutation(transaction=transaction, success=success)


class TransactionUpdateInput(TransactionCreateInput):
    amount = graphene.Decimal(description="amount of transaction", required=False)
    balance_after_transaction = graphene.Decimal(
        description="balance_after_transaction", required=False
    )
    status = graphene.Int(description="The status of Transaction.", required=False)


class TransactionUpdateMutation(graphene.Mutation):
    class Arguments:
        input = TransactionUpdateInput(
            required=True, description="Field required to update Bank Account"
        )

    transaction = graphene.Field(types.TransactionNode)
    success = graphene.Boolean()

    @classmethod
    def mutate(cls, root, info, input):
        success = False
        user = info.context.user

        if user.is_staff:
            transaction = models.Transaction.objects.update(**input)
            if transaction:
                success = True
        return TransactionUpdateMutation(transaction=transaction, success=success)
