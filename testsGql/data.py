from django.utils import timezone
from .models import AuthUser, Category


def initdata_users():
    user = AuthUser(username='testUser', password='testUser', date_joined=timezone.now(),
                        is_active=True, is_staff=True, is_superuser=True)
    user.save()

    user = AuthUser(username='testUser2', password='testUser2', date_joined=timezone.now(),
                        is_active=True, is_staff=True, is_superuser=True)
    user.save()


def initdata_categories():
    category = Category(title='Category1', userid=AuthUser.objects.get(username='testUser'), created=timezone.now())
    category.save()

    category = Category(title='Category2', userid=AuthUser.objects.get(username='testUser'), created=timezone.now())
    category.save()

    category = Category(title='Category3', userid=AuthUser.objects.get(username='testUser'), created=timezone.now())
    category.save()


def get_user(_id):
    return AuthUser.objects.get(id=_id)