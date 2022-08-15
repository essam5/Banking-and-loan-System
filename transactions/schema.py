import graphene
from . import types, mutations
from graphene_django.filter.fields import DjangoFilterConnectionField


class TransactionQuery(graphene.ObjectType):
    transaction = graphene.relay.Node.Field(types.TransactionNode)
    transactions = DjangoFilterConnectionField(types.TransactionNode)


class TransactionMutation(graphene.ObjectType):
    transaction_create = mutations.TransactionCreateMutation.Field()
    transaction_update = mutations.TransactionUpdateMutation.Field()
