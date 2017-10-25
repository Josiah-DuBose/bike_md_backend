from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from diag_app import views
from django.views.generic import TemplateView
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework_jwt.views import obtain_jwt_token


router = routers.DefaultRouter(trailing_slash=False)
router.register(r'user', views.UserView, 'list')
router.register(r'model', views.ModelViewSet)
router.register(r'problem', views.ProblemViewSet)
router.register(r'solution', views.SolutionViewSet)
router.register(r'tech', views.TechViewSet)
router.register(r'notification', views.NotificationViewSet)
router.register(r'commit', views.CommitViewSet)


urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^api-token-refresh/', refresh_jwt_token),
    url(r'^api-token-auth/', obtain_jwt_token),
]
