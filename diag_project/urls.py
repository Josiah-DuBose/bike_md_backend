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
router.register(r'users', views.UserView, 'list')
router.register(r'models', views.ModelViewSet)
router.register(r'problems', views.ProblemViewSet)
router.register(r'solutions', views.SolutionViewSet)
router.register(r'techs', views.TechViewSet)
router.register(r'notifications', views.NotificationViewSet)
router.register(r'commits', views.CommitViewSet)
router.register(r'brands', views.BrandViewSet)
router.register(r'years', views.YearViewSet)


urlpatterns = [
    url(r'^api/v1/', include(router.urls)),
    url(r'^api-token-refresh/', refresh_jwt_token),
    url(r'^api-token-auth/', obtain_jwt_token),
]
