import graphene
from graphene import relay
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphql import GraphQLError

from consumables import models


class SparesNode(DjangoObjectType):
    class Meta:
        model = models.Spares
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
        }
        interfaces = (relay.Node,)


class Query(graphene.ObjectType):
    spare = relay.Node.Field(SparesNode)
    spares = DjangoFilterConnectionField(SparesNode)


class CreateSpares(relay.ClientIDMutation):
    spare = graphene.Field(SparesNode)

    class Input:
        name = graphene.String()
        count = graphene.Int()
        cost = graphene.Float()

    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):
        user = info.context.user

        if user.is_anonymous:
            raise GraphQLError('You must be logged in!')

        spare = models.Spares(**input, created_by=user, updated_by=user)
        spare.save()
        return CreateSpares(spare=spare)


class Mutation(graphene.ObjectType):
    create_spares = CreateSpares.Field()
