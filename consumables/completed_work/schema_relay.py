import graphene
from graphene import relay
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphql import GraphQLError

from consumables import models


class CompletedWorkNode(DjangoObjectType):
    class Meta:
        model = models.CompletedWork
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
        }
        interfaces = (relay.Node,)


class Query(graphene.ObjectType):
    completedWork = relay.Node.Field(CompletedWorkNode)
    completedWorkList = DjangoFilterConnectionField(CompletedWorkNode)


class CreateCompletedWork(relay.ClientIDMutation):
    completedWork = graphene.Field(CompletedWorkNode)

    class Input:
        name = graphene.String()
        hours = graphene.Int()
        cost = graphene.Float()

    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):
        user = info.context.user

        if user.is_anonymous:
            raise GraphQLError('You must be logged in!')

        completed_work = models.CompletedWork(**input, created_by=user, updated_by=user)
        completed_work.save()
        return CreateCompletedWork(completedWork=completed_work)


class Mutation(graphene.ObjectType):
    create_completed_work = CreateCompletedWork.Field()
