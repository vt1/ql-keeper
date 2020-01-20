import graphene
from django.http import QueryDict
from django.utils import timezone
import datetime
from graphene_django import DjangoObjectType
from graphene import relay
# from graphql_extensions.auth.decorators import login_required
from schemes.product import ProductMutation, ProductQuery
from schemes.debit import DebitMutation, DebitQuery
from schemes.warehouse import WarehouseQuery, WarehouseMutation
from schemes.productComment import ProductCommentMutation, ProductCommentQuery
from promise import promise

promise.async_instance.disable_trampoline()

class UserType(DjangoObjectType):
    class Meta:
        model = AuthUser


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category


class UpdateCategory(graphene.Mutation):
    class Arguments:
        categoryid = graphene.Int(required=True)
        title = graphene.String(required=True)

    category = graphene.Field(CategoryType)

    def mutate(self, info, categoryid, title):
        category = Category.objects.get(pk=categoryid)
        category.title = title
        category.save()
        return UpdateCategory(category=category)


class CreateCategory(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)

    category = graphene.Field(CategoryType)

    def mutate(self, info, title):
        user_instance = AuthUser.objects.get(pk=info.context.user.id)
        current_time = timezone.now()
        category = Category(title=title,
                            userid=user_instance,
                            created=current_time)
        category.save()
        return CreateCategory(category=category)


class Mutation(graphene.ObjectType):
    create_category = CreateCategory.Field()
    update_category = UpdateCategory.Field()
    create_pricetype = CreatePriceType.Field()


class Query(graphene.ObjectType):
    users = graphene.List(UserType)
    user = graphene.Field(UserType,
                          userid=graphene.Int(),
                          username=graphene.String(),
                          email=graphene.String(),
                          description=graphene.String())

    categories = graphene.List(CategoryType)
        
    def resolve_user(self, info, **kwargs):
        userid = kwargs.get('userid')
        username = kwargs.get('username')
        email = kwargs.get('email')
        description = kwargs.get('description')

        if userid is not None:
            return AuthUser.objects.get(pk=userid)

        if username is not None:
            return AuthUser.objects.get(username=username)

        if email is not None:
            return AuthUser.objects.get(email=email)

        if description is not None:
            return AuthUser.objects.get(description=description)

        return None

    def resolve_users(self, info, **kwargs):
        return AuthUser.objects.all()

    def resolve_categories(self, info, **kwargs):
        return Category.objects.all()

    def resolve_pricetypes(self, info, **kwargs):
        return Pricetype.objects.all()

    def resolve_pricetype(self, info, **kwargs):
        pricetypeid = kwargs.get('pricetypeid')
        title = kwargs.get('title')

        if pricetypeid is not None:
            return Pricetype.objects.get(pricetypeid=pricetypeid)

        if title is not None:
            return Pricetype.objects.get(title=title)

    
class RootQuery(Query,
                ProductQuery,
                ProductDetailsQuery,
                WarehouseQuery,
                CreditCommentQuery,                
                graphene.ObjectType):
    pass


class RootMutation(Mutation,
                   ProductMutation,
                   ProductDetailsMutation,
                   WarehouseMutation,
                   CreditCommentMutation,
                   graphene.ObjectType):
    pass


schema = graphene.Schema(query=RootQuery, mutation=RootMutation)
