from django.conf.urls import url
import diag_app
from rest_framework.authtoken import views

urlpatterns = [
    # # django urls
    # url((r'^$'), views.main_page, name='main'),
    # url((r'^problem_list/([A-Za-z0-9]+)/([0-9]+)'), views.problem_list, name='problem_list'),
    # url((r'^model_detail/([0-9]+)'), views.model_detail, name='model_detail'),
    # url((r'^problem_detail/([0-9]+)'), views.problem_detail, name='problem_detail'),
    # url((r'^profile/$'), views.profile, name='profile'),
    # url(r'^create_account/$', views.create_account, name='create_account'),
    # url((r'^about/$'), views.about_us, name='about'),
    # url((r'^notifications/$'), views.notifications, name='notifications'),
    #
    # ### developemnt urls ###
    # url((r'^problems/'),TemplateView.as_view(template_name="build_templates/problem_listing.html")),
    # url((r'^model_details/([0-9]+)'), TemplateView.as_view(template_name='build_templates/bike_detail.html')),
    # url((r'^problem_details/([0-9]+)'), TemplateView.as_view(template_name='build_templates/problem_detail.html')),
]
