import graphene
from graphql_auth import mutations
from graphql_auth.schema import UserQuery, MeQuery
from .mutations import (
    BankAccountTypeCreateMutation,
    BankAccountTypeUpdateMutation,
    UserBankAccountCreateMutation,
    UserBankAccountUpdateMutation,
)
from loans.schema import LoanMutation, LoanQuery
from transactions.schema import TransactionMutation, TransactionQuery

from graphene_django.filter.fields import DjangoFilterConnectionField
from . import types


class AuthMutation(graphene.ObjectType):
    register = mutations.Register.Field()
    token_auth = mutations.ObtainJSONWebToken.Field()
    update_account = mutations.UpdateAccount.Field()
    verify_account = mutations.VerifyAccount.Field()
    resend_activation_email = mutations.ResendActivationEmail.Field()
    send_password_reset_email = mutations.SendPasswordResetEmail.Field()
    password_reset = mutations.PasswordReset.Field()
    password_change = mutations.PasswordChange.Field()
    bank_account_type_create = BankAccountTypeCreateMutation.Field()
    user_bank_account_create = UserBankAccountCreateMutation.Field()
    bank_account_type_update = BankAccountTypeUpdateMutation.Field()
    user_bank_account_update = UserBankAccountUpdateMutation.Field()


class BankQuery(graphene.ObjectType):
    user_bank_account = graphene.relay.Node.Field(types.BankAccountNode)
    user_bank_accounts = DjangoFilterConnectionField(types.BankAccountNode)
    bank_account_type = graphene.relay.Node.Field(types.BankAccountTypeNode)
    bank_account_types = DjangoFilterConnectionField(types.BankAccountTypeNode)


class Query(
    UserQuery, MeQuery, LoanQuery, BankQuery, TransactionQuery, graphene.ObjectType
):
    pass


class Mutation(AuthMutation, LoanMutation, TransactionMutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
