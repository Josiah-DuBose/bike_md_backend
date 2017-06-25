from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import viewsets, permissions, generics, filters
from . import models, forms
from .forms import UserForm, TechForm, LoginForm
from .models import Vote, Problem, Solution, Tech, Rating, System, Brand
from .models import Model, Problem_Model, Notification, Commit
from .serializers import VoteSerializer, ProblemGetSerializer, UserSerializer
from .serializers import TechGetSerializer, RatingSerializer, SystemSerializer
from .serializers import BrandSerializer, ModelSerializer, ProblemPostSerializer
from .serializers import SolutionPostSerializer, SolutionGetSerializer
from .serializers import TechPostSerializer, NotificationSerializer
from .serializers import CommitSerializer
from django.views.generic import ListView
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django_filters.rest_framework import DjangoFilterBackend
import django_filters
from django.contrib.auth.models import User
from .permissions import IsStaffOrTargetUser


def create_account(request):
    return render(request, 'create_account.html')


def about_us(request):
    return render(request, 'about_us.html')


def login_user(request):
    form = LoginForm(request.POST or None)
    if request.POST:
        user = authenticate(username = request.POST['username'],
        password = request.POST['password'])
        if user is not None and user.is_active and form.is_valid():
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            return render(request, 'registration/login.html',{
                'login_message' : 'Enter the username and password correctly',})
    return render(request, 'registration/login.html')


@login_required(login_url='/login/')
def main_page(request):
    return render(request, 'main.html')


@login_required(login_url='/login/')
def notifications(request):
    return render(request, 'notifications.html')


@login_required(login_url='/login/')
def problem_list(request, model, id):
    return render(request, 'problem_list.html')


@login_required(login_url='/login/')
def model_detail(request, id):
    return render(request, 'bike_detail.html')


@login_required(login_url='/login/')
def problem_detail(request, id):
    return render(request, 'problem_detail.html')


@login_required(login_url='/login/')
def profile(request):
    return render(request, 'profile.html')


# class viewsets and filters
class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    model = User

    # def get_permissions(self):
    #     return (AllowAny() if self.request.method == 'POST'
    #             else IsStaffOrTargetUser()),


class SystemViewSet(viewsets.ModelViewSet):
    queryset = System.objects.all()
    serializer_class = SystemSerializer
    # permission_classes = (permissions.IsAuthenticated,)


# class ModelFilter(django_filters.rest_framework.FilterSet):
#
#     class Meta:
#         model = Model
#         fields = ['brand', 'year']


class ModelViewSet(viewsets.ModelViewSet):
    queryset = Model.objects.all().order_by('name')
    serializer_class = ModelSerializer
    # filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    # filter_class = ModelFilter
    # permission_classes = (permissions.IsAuthenticated,)


class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all().order_by('name')
    serializer_class = BrandSerializer
    # permission_classes = (permissions.IsAuthenticated,)


# class ProblemFilter(django_filters.rest_framework.FilterSet):
#     no_solutions = django_filters.BooleanFilter(name='solutions',
#                                                 lookup_expr='isnull')
#
#     class Meta:
#         model = Problem
#         fields = ['system', 'model', 'tech', 'no_solutions']


class ProblemViewSet(viewsets.ModelViewSet):
    queryset = Problem.objects.all().order_by('-posted')
    serializer_class = ProblemGetSerializer
    # filter_backends = (django_filters.rest_framework.DjangoFilterBackend,filters.SearchFilter,)
    # filter_class = ProblemFilter
    # search_fields = ['title']
    # permission_classes = (permissions.IsAuthenticated,)


# class ProblemPostViewSet(viewsets.ModelViewSet):
#     queryset = Problem.objects.all()
#     serializer_class = ProblemPostSerializer
#     # filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
#     # filter_class = ProblemFilter
#     # permission_classes = (permissions.IsAuthenticated,)


class SolutionViewSet(viewsets.ModelViewSet):
    queryset = Solution.objects.all()
    serializer_class = SolutionGetSerializer
    # permission_classes = (permissions.IsAuthenticated,)


# class SolutionPostViewSet(viewsets.ModelViewSet):
#     queryset = Solution.objects.all()
#     serializer_class = SolutionPostSerializer
#     # permission_classes = (permissions.IsAuthenticated,)


# class VoteFilter(django_filters.rest_framework.FilterSet):
#
#     class Meta:
#         model = Vote
#         fields = ['solution', 'tech']


class VoteViewSet(viewsets.ModelViewSet):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
    # filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    # filter_class = VoteFilter
    # permission_classes = (permissions.IsAuthenticated,)


class TechViewSet(viewsets.ModelViewSet):
    queryset = Tech.objects.all()
    serializer_class = TechGetSerializer
    # permission_classes = (permissions.IsAuthenticated,)


# class TechPostViewSet(viewsets.ModelViewSet):
#     queryset = Tech.objects.all()
#     serializer_class = TechPostSerializer

    # def get_permissions(self):
    #     return (AllowAny() if self.request.method == 'POST'
    #             else IsStaffOrTargetUser()),


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    # permission_classes = (permissions.IsAuthenticated,)


class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    # permission_classes = (permissions.IsAuthenticated,)


class CommitViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = CommitSerializer
