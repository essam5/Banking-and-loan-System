import graphene
from . import types, mutations
from graphene_django.filter.fields import DjangoFilterConnectionField


class LoanQuery(graphene.ObjectType):
    loan = graphene.relay.Node.Field(types.LoanNode)
    loans = DjangoFilterConnectionField(types.LoanNode)


class LoanMutation(graphene.ObjectType):
    loan_type_create = mutations.LoanTypeCreateMutation.Field()
    loan_create = mutations.LoanCreateMutation.Field()
    loan_update = mutations.LoanUpdateMutation.Field()
