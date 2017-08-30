from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from diag_app import views
from django.views.generic import TemplateView


router = routers.DefaultRouter(trailing_slash=False)
router.register(r'accounts', views.UserView, 'list')
router.register(r'models', views.ModelViewSet)
router.register(r'problems', views.ProblemViewSet)
router.register(r'solutions', views.SolutionViewSet)
router.register(r'votes', views.VoteViewSet)
router.register(r'tech', views.TechViewSet)
router.register(r'ratings', views.RatingViewSet)
router.register(r'notifications', views.NotificationViewSet)
router.register(r'commits', views.CommitViewSet)


urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^', include('diag_app.urls', namespace='api', app_name='diag_app')),
    # url(r'^admin/', admin.site.urls),
    # url(r'^login/$', views.login_user, name='login'),
    # url(r'^logout/$', auth_views.logout, {'next_page': 'login'},
    #     name='logout'),
]
