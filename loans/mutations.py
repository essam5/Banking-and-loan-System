import graphene

from . import models, types
from graphql_relay import from_global_id


class InterestTypeLoan(graphene.Enum):
    FLAT_RATE = 1
    REDUCING_BALANCE = 2


class PaymentFrequency(graphene.Enum):
    DAILY = 1
    MONTHLY = 2
    QUARTERLY = 3
    BI_ANNUAL = 4
    YEARLY = 5


class LoanStatus(graphene.Enum):
    ACCEPTED = 1
    PENDING = 2
    REJECTED = 3


class LoanTypeCreateInput(graphene.InputObjectType):
    name = graphene.String(description="The name of loan type.", required=True)
    rate = graphene.Decimal(description="First Name.", required=True)
    description = graphene.String(description="description of loan type", required=True)

    need_collateral = graphene.Boolean(
        description="does this type of Loan need Coollateral", default_value=False
    )
    need_guarantor = graphene.Boolean(
        description="does this type of loan need a gurantor", default_value=False
    )

    market = graphene.String(description="National ID.", required=False)
    min_amount_allowed = graphene.String(description="Residence ID.", required=False)

    max_amount_allowed = graphene.String(required=False)

    interest_type = InterestTypeLoan(description="Facebook page URL.", required=True)


class LoanTypeCreateMutation(graphene.Mutation):
    class Arguments:
        input = LoanTypeCreateInput(
            required=True, description="Field required to create Loan Type"
        )

    loan_type = graphene.Field(types.LoanTypeNode)
    success = graphene.Boolean()

    @classmethod
    def mutate(cls, root, info, input):
        success = False

        loan_type = models.loanType.objects.create(**input)
        if loan_type:
            success = True
        return LoanTypeCreateMutation(loan_type=loan_type, success=success)


class LoanTypeUpdateInput(graphene.InputObjectType):
    name = graphene.String(description="The name of loan type.", required=False)
    rate = graphene.Decimal(description="First Name.", required=False)
    description = graphene.String(
        description="description of loan type", required=False
    )


class LoanTypeUpdateMutation(graphene.Mutation):
    class Arguments:
        input = LoanTypeUpdateInput(
            required=True, description="Field required to Update Loan Type"
        )

    loan_type = graphene.Field(types.LoanTypeNode)
    success = graphene.Boolean()

    @classmethod
    def mutate(cls, root, info, input):
        success = False

        loan_type = models.loanType.objects.update(**input)
        if loan_type:
            success = True
        return LoanTypeUpdateMutation(loan_type=loan_type, success=success)


#################################### loan mutations ###########################################


class LoanCreateInput(graphene.InputObjectType):
    amount = graphene.Decimal(description="amount of account", required=True)
    currency = graphene.String(description="currency of amount", required=True)
    payment_frequency = PaymentFrequency(
        description="payment frequency the term of loan", required=False
    )
    tenure = graphene.Int(description="number of term of loan", required=False)


class LoanCreateMutation(graphene.Mutation):
    class Arguments:
        user_bank_account = graphene.ID(
            required=True, description="user bank account ID"
        )
        input = LoanCreateInput(
            required=True, description="Field required to create Loan "
        )

    loan = graphene.Field(types.LoanNode)
    success = graphene.Boolean()

    @classmethod
    def mutate(cls, root, info, user_bank_account, input):
        success = False
        user = info.context.user
        type, id = from_global_id(user_bank_account)
        bank_account = models.UserBankAccount.objects.get(id=id)
        loan = models.Loan.objects.create(**input, bank_account=bank_account, user=user)
        if loan:
            success = True
        return LoanCreateMutation(loan=loan, success=success)


class LoanUpdateInput(LoanCreateInput):
    status = graphene.Int(description="The status of loan.", required=False)


class LoanUpdateMutation(graphene.Mutation):
    class Arguments:
        input = LoanUpdateInput(
            required=True, description="Field required to update Bank Account"
        )

    loan = graphene.Field(types.LoanNode)
    success = graphene.Boolean()

    @classmethod
    def mutate(cls, root, info, input):
        success = False
        user = info.context.user

        if user.is_staff:
            loan = models.Loan.objects.update(**input)
            if loan:
                success = True
        return LoanUpdateMutation(loan=loan, success=success)
