import graphene
from graphene import relay
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphql import GraphQLError

from consumables import models


class CompletedWorkNode(DjangoObjectType):
    id = graphene.ID(source='pk', required=True)

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


class UpdateCompletedWork(relay.ClientIDMutation):
    completedWork = graphene.Field(CompletedWorkNode)

    class Input:
        id = graphene.Int()
        name = graphene.String()
        hours = graphene.Int()
        cost = graphene.Float()

    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):
        user = info.context.user

        if user.is_anonymous:
            raise GraphQLError('You must be logged in!')

        completed_work = models.CompletedWork.objects.filter(id=input['id']).first()

        if completed_work and input:
            for key, value in input.items():
                setattr(completed_work, key, value)

            completed_work.save()
        return UpdateCompletedWork(completedWork=completed_work)



class Mutation(graphene.ObjectType):
    create_completed_work = CreateCompletedWork.Field()
    update_completed_work = UpdateCompletedWork.Field()
