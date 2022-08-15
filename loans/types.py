import graphene
from graphene_django import DjangoObjectType
from . import models
from graphql_auth.schema import UserNode


class LoanTypeNode(DjangoObjectType):
    class Meta:
        model = models.loanType
        interfaces = (graphene.relay.Node,)
        filter_fields = [
            "id",
            "name",
            "rate",
        ]


class LoanNode(DjangoObjectType):
    user = graphene.Field(UserNode)
    loan_type = graphene.Field(LoanTypeNode)

    class Meta:
        model = models.Loan
        interfaces = (graphene.relay.Node,)
        exclude = [
            "bank_account",
        ]
        filter_fields = ["id", "status", "currency", "amount"]


class LoanNodeConnection(graphene.relay.Connection):
    class Meta:
        node = LoanNode
