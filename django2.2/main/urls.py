"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import include
from django.conf import settings
from django.urls import path
from graphene_django.views import GraphQLView

from .schemas import schema
from .views import TestView, TestStreamView, TestSSEView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('graphql/', GraphQLView.as_view(graphiql=True, schema=schema)),
    path('notifications/', include('notifications.urls', namespace='notifications')),

]

urlpatterns += [
    path('chat/', include('apps.chat.urls')),
]

urlpatterns += [
    path('test', TestView.as_view(), name="test"),
    path('test-stream', TestStreamView.as_view(), name="test-stream"),
    path('test-sse', TestSSEView.as_view(), name="test-sse"),

]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path(r'^__debug__/', include(debug_toolbar.urls)),
    ]
