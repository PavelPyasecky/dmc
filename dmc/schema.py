import graphene
from graphql_auth.schema import UserQuery, MeQuery

import consumables.schema_relay
import vehicle.schema_relay
import users.schema

from graphql_auth import relay


class AuthMutation(graphene.ObjectType):
    register = relay.Register.Field()
    verify_account = relay.VerifyAccount.Field()
    resend_activation_email = relay.ResendActivationEmail.Field()
    send_password_reset_email = relay.SendPasswordResetEmail.Field()
    password_reset = relay.PasswordReset.Field()
    password_change = relay.PasswordChange.Field()
    archive_account = relay.ArchiveAccount.Field()
    delete_account = relay.DeleteAccount.Field()
    update_account = relay.UpdateAccount.Field()
    send_secondary_email_activation = relay.SendSecondaryEmailActivation.Field()
    verify_secondary_email = relay.VerifySecondaryEmail.Field()
    swap_emails = relay.SwapEmails.Field()

    # django-graphql-jwt inheritances
    token_auth = relay.ObtainJSONWebToken.Field()
    verify_token = relay.VerifyToken.Field()
    refresh_token = relay.RefreshToken.Field()
    revoke_token = relay.RevokeToken.Field()


class Query(UserQuery, MeQuery, vehicle.schema_relay.Query, consumables.schema_relay.Query, graphene.ObjectType):
    pass


class Mutation(AuthMutation, users.schema.Mutation, vehicle.schema_relay.Mutation, consumables.schema_relay.Mutation,
               graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
