import graphene
from graphene_django import DjangoObjectType

from loans.types import LoanNode
from . import models
from users.types import BankAccountNode


class TransactionNode(DjangoObjectType):
    account = graphene.Field(BankAccountNode)
    loan = graphene.Field(LoanNode)

    class Meta:
        model = models.Transaction
        interfaces = (graphene.relay.Node,)
        filter_fields = ["id", "amount", "status"]
