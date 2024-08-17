import datetime

import graphene
from django.db.models import Q
from graphene_django import DjangoObjectType
from graphql import GraphQLError

from users.schema import UserType
from vehicle.models import Vehicle


class VehicleType(DjangoObjectType):
    class Meta:
        model = Vehicle


class Query(graphene.ObjectType):
    vehicle = graphene.List(VehicleType, search=graphene.String(),
                            first=graphene.Int(), skip=graphene.Int())

    def resolve_vehicle(self, info, search=None, first=None, skip=None, **kwargs):
        qs = Vehicle.objects.all()

        if search:
            filter = (
                Q(url__icontains=search)
                | Q(description__icontains=search)
            )
            return qs.filter(filter)

        if skip:
            qs = qs[skip:]

        if first:
            qs = qs[:first]

        return qs


class CreateVehicle(graphene.Mutation):
    id = graphene.Int()
    vin = graphene.String()
    owner = graphene.Field(UserType)
    created_by = graphene.Field(UserType)
    created_date = graphene.DateTime()

    class Arguments:
        vin = graphene.String()

    def mutate(self, info, vin):
        user = info.context.user or None

        if user.is_anonymous:
            raise GraphQLError('You must be logged in!')

        utc_now = datetime.datetime.utcnow()

        vehicle = Vehicle(vin=vin, owner=user, created_by=user, created_date=utc_now, updated_by=user,
                          updated_date=utc_now)
        vehicle.save()

        return CreateVehicle(
            id=vehicle.id,
            vin=vehicle.vin,
            owner=vehicle.owner,
            created_by=vehicle.created_by,
            created_date=vehicle.created_date
        )


class Mutation(graphene.ObjectType):
    create_vehicle = CreateVehicle.Field()
