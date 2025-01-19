from django.core import signing
from django.http import JsonResponse
from django.shortcuts import redirect

from users.models import CustomUser


def activate(request, token):
    context = signing.loads(token)
    user = CustomUser.objects.get(username=context['username'])
    if not user.is_active:
        user.is_active = True
        user.save()

        status = 'success'
    else:
        status = 'already_activated'

    return redirect(f"http://localhost:3000/activate?status={status}", )
