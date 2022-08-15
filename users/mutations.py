import graphene
from . import models, types
from graphql_relay import from_global_id


class Gender(graphene.Enum):
    MALE = "M"
    FEMALE = "F"


class BankAccountTypeCreateInput(graphene.InputObjectType):
    name = graphene.String(
        description="The name of the Bank account type.", required=True
    )
    maximum_withdrawal_amount = graphene.Decimal(
        description="maximum withdrawal amount.", required=True
    )
    annual_interest_rate = graphene.Decimal(
        description="Interest rate from 0 - 100", required=True
    )

    interest_calculation_per_year = graphene.Int(
        description="interest calculation per year (1-12)", required=False
    )


class BankAccountTypeCreateMutation(graphene.Mutation):
    class Arguments:
        input = BankAccountTypeCreateInput(
            required=True, description="Field required to create Bank Account Type"
        )

    account_type = graphene.Field(types.BankAccountTypeNode)
    success = graphene.Boolean()

    @classmethod
    def mutate(cls, root, info, input):
        success = False
        user = info.context.user

        if user.is_staff:
            account_type = models.BankAccountType.objects.create(**input)
            if account_type:
                success = True

        return BankAccountTypeCreateMutation(account_type=account_type, success=success)


class BankAccountTypeUpdateInput(BankAccountTypeCreateInput):
    name = graphene.String(
        description="The name of the Bank account type.", required=False
    )
    maximum_withdrawal_amount = graphene.Decimal(
        description="maximum withdrawal amount.", required=False
    )
    annual_interest_rate = graphene.Decimal(
        description="Interest rate from 0 - 100", required=False
    )


class BankAccountTypeUpdateMutation(graphene.Mutation):
    class Arguments:
        input = BankAccountTypeUpdateInput(
            required=True, description="Field required to Update Bank Account Type"
        )

    account_type = graphene.Field(types.BankAccountTypeNode)
    success = graphene.Boolean()

    @classmethod
    def mutate(cls, root, info, input):
        success = False
        user = info.context.user

        if user.is_staff:
            account_type = models.BankAccountType.objects.update(**input)
            if account_type:
                success = True
        return BankAccountTypeUpdateMutation(account_type=account_type, success=success)


################################ user bank account mutations ##########################


class UserBankAccountCreateInput(graphene.InputObjectType):
    account_no = graphene.Int(description="The account number.", required=True)
    gender = Gender(description="gender of user .", required=True)
    balance = graphene.Decimal(description="balance of account", required=False)

    interest_start_date = graphene.String(
        description="interest start date", required=False
    )
    initial_deposit_date = graphene.String(
        description="initial deposit date", required=False
    )


class UserBankAccountCreateMutation(graphene.Mutation):
    class Arguments:
        account_type = graphene.ID(required=True, description="account type ID")
        input = UserBankAccountCreateInput(
            required=True, description="Field required to create Bank Account "
        )

    user_bank_account = graphene.Field(types.BankAccountNode)
    success = graphene.Boolean()

    @classmethod
    def mutate(cls, root, info, account_type, input):
        success = False
        user = info.context.user
        type, id = from_global_id(account_type)
        account_type = models.BankAccountType.objects.get(id=id)
        user_bank_account = models.UserBankAccount.objects.create(
            **input, account_type=account_type, user=user
        )
        if user_bank_account:
            success = True
        return UserBankAccountCreateMutation(
            user_bank_account=user_bank_account, success=success
        )


class UserBankAccountupdateInput(UserBankAccountCreateInput):
    account_no = graphene.Int(description="The account number.", required=False)
    gender = Gender(description="gender of user .", required=False)


class UserBankAccountUpdateMutation(graphene.Mutation):
    class Arguments:
        input = UserBankAccountupdateInput(
            required=True, description="Field required to update Bank Account"
        )

    user_bank_account = graphene.Field(types.BankAccountNode)
    success = graphene.Boolean()

    @classmethod
    def mutate(cls, root, info, input):
        success = False
        user_bank_account = models.UserBankAccount.objects.update(**input)
        if user_bank_account:
            success = True
        return UserBankAccountUpdateMutation(
            user_bank_account=user_bank_account, success=success
        )
