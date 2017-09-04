from django.conf.urls import url
import diag_app
from rest_framework.authtoken import views

urlpatterns = [
    url(r'^auth/', views.obtain_auth_token),
]
