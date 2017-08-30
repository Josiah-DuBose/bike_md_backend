from django.conf.urls import url
import diag_app
from rest_framework.authtoken import views

urlpatterns = [
    url(r'^api-token-auth/', views.obtain_auth_token)
    (r'^problem_details/([0-9]+)'), TemplateView.as_view(template_name='build_templates/problem_detail.html')),
]
