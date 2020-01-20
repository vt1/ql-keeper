from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.views import LoginView
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView
from django.shortcuts import render
from django.contrib.auth import logout


def custom_login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('index/')
    else:
        return LoginView.as_view()(request)


def graphql_view(request):
    return csrf_exempt(GraphQLView.as_view(graphiql=True))(request)
    '''
    if request.user.is_superuser:
        return csrf_exempt(GraphQLView.as_view(graphiql=True))(request)
    else:
        return HttpResponse('404, not super user')
    '''


def index(request):
    if request.user.is_authenticated:
        return render(request, 'site/index.html')
    else:
        return HttpResponseRedirect('/')


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')