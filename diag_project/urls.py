from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from rest_framework import routers
from diag_app import views
from django.views.generic import TemplateView


router = routers.DefaultRouter(trailing_slash=False)
router.register(r'accounts', views.UserView, 'list')
router.register(r'systems', views.SystemViewSet)
router.register(r'brands', views.BrandViewSet)
router.register(r'models', views.ModelViewSet)
router.register(r'problems', views.ProblemViewSet)
# router.register(r'post-problems', views.ProblemPostViewSet)
router.register(r'solutions', views.SolutionViewSet)
# router.register(r'post-solutions', views.SolutionPostViewSet)
router.register(r'votes', views.VoteViewSet)
router.register(r'tech', views.TechViewSet)
# router.register(r'post-techs', views.TechPostViewSet)
router.register(r'ratings', views.RatingViewSet)
router.register(r'notifications', views.NotificationViewSet)
router.register(r'commits', views.CommitViewSet)


urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^', include('diag_app.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', views.login_user, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'},
        name='logout'),
]
