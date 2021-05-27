import graphene
from graphene_django import DjangoObjectType
from .models import Bank, Branches

class BankType(DjangoObjectType):
    class Meta:
        model = Bank
        fields = ("__all__")

class BranchType(DjangoObjectType):
    class Meta:
        model = Branches
        fields = ("__all__")


class Query(graphene.ObjectType):
    branches = graphene.Field(BranchType, ifsc = graphene.String(required = True))
    banks = graphene.Field(BankType, bid = graphene.Int(required = True))
    

    def resolve_branches(root, info,ifsc):
        try:
            return Branches.objects.get(ifsc = ifsc)
        except Branch.DoesNotExist:
            return None

    def resolve_banks(root, info, bid):
        try:
            return Bank.objects.get(b_id = bid)
        except Bank.DoesNotExist:
            return None

schema = graphene.Schema(query=Query)



