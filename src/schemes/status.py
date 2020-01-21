import graphene
from django.db.models import Q
from graphene_django import DjangoObjectType
from libs.common_db import *


class StatusType(DjangoObjectType):
    class Meta:
        model = Status


class StatusQuery(graphene.ObjectType):
    statuses = graphene.List(StatusType,
                             search=graphene.String(),
                             date_from=graphene.DateTime(),
                             date_to=graphene.DateTime())

    status = graphene.Field(StatusType,
                            title=graphene.String(),
                            statusid=graphene.Int())

    def resolve_statuses(self, info, **kwargs):
        search = kwargs.get('search')
        date_from = kwargs.get('date_from')
        date_to = kwargs.get('date_to')

        query_filter_set = Q(title__icontains=search) | Q(color__icontains=search) | Q(statusid__icontains=search)

        if None not in (search, date_from, date_to):
            return Status.objects.filter(query_filter_set, Q(created__range=(date_from,date_to)))

        if search is not None:
            return Status.objects.filter(query_filter_set)

        if None not in (date_from, date_to):
            return Status.objects.filter(created__range=(date_from, date_to))

        return Status.objects.all()

    def resolve_status(self, info, **kwargs):
        title = kwargs.get('title')
        statusid = kwargs.get('statusid')

        if title is not None:
            return Status.objects.get(title=title)

        if statusid is not None:
            return Status.objects.get(statusid=statusid)

        return None


class CreateStatus(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        color = graphene.String(required=True)

    status = graphene.Field(StatusType)

    def mutate(self, info, **kwargs):
        status = create_status(info, kwargs)
        return CreateStatus(status=status)


class UpdateStatus(graphene.Mutation):
    class Arguments:
        statusid = graphene.Int(required=True)
        title = graphene.String()
        color = graphene.String()

    status = graphene.Field(StatusType)

    def mutate(self, info, **kwargs):
        status = update_status(kwargs)
        status.save()
        return UpdateStatus(status=status)


class StatusMutation(graphene.ObjectType):
    create_status = CreateStatus.Field()
    update_status = UpdateStatus.Field()