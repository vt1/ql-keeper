from django.contrib import admin
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views
from graphene_django.views import GraphQLView


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('graphql/', csrf_exempt(views.graphql_view)),
    path('graphql/', views.graphql_view),
    # path('graphql/', jwt_cookie(GraphQLView.as_view())),
    path('', views.custom_login),
    path('logout/', views.logout_view, name='logout'),
    path('index/', views.index),
]