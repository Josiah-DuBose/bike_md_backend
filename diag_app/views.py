from rest_framework import viewsets, permissions, generics, filters
from . import models
from .models import Problem, Solution, Tech, Model, Commit, Notification, Year, Brand
from .serializers import UserSerializer, CommitSerializer, ProblemSerializer
from .serializers import ModelSerializer, SolutionSerializer, YearSerializer
from .serializers import TechSerializer, NotificationSerializer, BrandSerializer
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import django_filters


# class viewsets
class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    model = User


class ModelFilter(django_filters.rest_framework.FilterSet):

    class Meta:
        model = Model
        fields = ['brand', 'year']


class ModelViewSet(viewsets.ModelViewSet):
    queryset = Model.objects.all().order_by('name')
    serializer_class = ModelSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,filters.SearchFilter,)
    filter_class = ModelFilter


class YearViewSet(viewsets.ModelViewSet):
    queryset = Year.objects.all().order_by('-value')
    serializer_class = YearSerializer


class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all().order_by('name')
    serializer_class = BrandSerializer


class ProblemFilter(django_filters.rest_framework.FilterSet):
    posted_gte = django_filters.DateTimeFilter(name="posted", lookup_expr='gte')
    posted_lte = django_filters.DateTimeFilter(name="posted", lookup_expr='lte')

    class Meta:
        model = Problem
        fields = ['posted_gte', 'posted_lte', 'tech']


class ProblemViewSet(viewsets.ModelViewSet):
    queryset = Problem.objects.all().order_by('-posted')
    serializer_class = ProblemSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,filters.SearchFilter,)
    filter_class = ProblemFilter


class SolutionFilter(django_filters.rest_framework.FilterSet):

    class Meta:
        model = Solution
        fields = ['problem', 'tech']


class SolutionViewSet(viewsets.ModelViewSet):
    queryset = Solution.objects.all().order_by('-score')
    serializer_class = SolutionSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,filters.SearchFilter,)
    filter_class = SolutionFilter


class TechViewSet(viewsets.ModelViewSet):
    queryset = Tech.objects.all()
    serializer_class = TechSerializer


class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer


class CommitViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = CommitSerializer
