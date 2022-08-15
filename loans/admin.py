from django.contrib import admin

from loans.models import loanType, Loan

admin.site.register(Loan)
admin.site.register(loanType)
