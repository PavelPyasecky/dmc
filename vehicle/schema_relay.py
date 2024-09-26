import datetime

import graphene
from graphene import relay
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphql import GraphQLError

from vehicle import models


class VehicleNode(DjangoObjectType):
    class Meta:
        model = models.Vehicle
        filter_fields = {
            'vin': ['exact', 'icontains', 'istartswith'],
        }
        interfaces = (relay.Node,)


class Query(graphene.ObjectType):
    vehicle = relay.Node.Field(VehicleNode)
    vehicles = DjangoFilterConnectionField(VehicleNode)


class CreateVehicle(relay.ClientIDMutation):
    vehicle = graphene.Field(VehicleNode)

    class Input:
        vin = graphene.String()

    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):
        user = info.context.user

        if user.is_anonymous:
            raise GraphQLError('You must be logged in!')

        utc_now = datetime.datetime.utcnow()

        vehicle = models.Vehicle(**input, owner=user, created_by=user, created_date=utc_now, updated_by=user,
                                 updated_date=utc_now)
        vehicle.save()

        return CreateVehicle(vehicle=vehicle)


class Mutation(graphene.ObjectType):
    create_vehicle = CreateVehicle.Field()
