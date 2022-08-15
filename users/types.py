import graphene
from graphene_django import DjangoObjectType
from . import models
from graphql_auth.schema import UserNode


class BankAccountTypeNode(DjangoObjectType):
    class Meta:
        model = models.BankAccountType
        interfaces = (graphene.relay.Node,)
        filter_fields = [
            "id",
            "name",
        ]


class BankAccountNode(DjangoObjectType):
    user = graphene.Field(UserNode)
    account_type = graphene.Field(BankAccountTypeNode)

    class Meta:
        model = models.UserBankAccount
        interfaces = (graphene.relay.Node,)
        filter_fields = ["id", "account_no", "gender", "balance"]
