from rest_framework import viewsets, permissions, generics, filters
from . import models
from .models import Vote, Problem, Solution, Tech, Rating, Model, Commit, Notification
from .serializers import VoteSerializer, UserSerializer, RatingSerializer
from .serializers import ModelSerializer, SolutionSerializer, CommitSerializer
from .serializers import TechSerializer, NotificationSerializer, ProblemSerializer
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import rest_framework_filters as filters


# class viewsets
class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    model = User


class ModelViewSet(viewsets.ModelViewSet):
    queryset = Model.objects.all().order_by('name')
    serializer_class = ModelSerializer


class ProblemFilter(filters.FilterSet):
    posted_gte = filters.DateTimeFilter(name="posted",lookup_type="gte")

    class Meta:
        model = Problem
        fields = ['posted', 'posted_gte', 'tech']


class ProblemViewSet(viewsets.ModelViewSet):
    queryset = Problem.objects.all().order_by('-posted')
    serializer_class = ProblemSerializer
    filter_class = ProblemFilter


class SolutionFilter(filters.FilterSet):

    class Meta:
        model = Solution
        fields = ['problem', 'tech']


class SolutionViewSet(viewsets.ModelViewSet):
    queryset = Solution.objects.all()
    serializer_class = SolutionSerializer
    filter_class = SolutionFilter


class VoteViewSet(viewsets.ModelViewSet):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer


class TechViewSet(viewsets.ModelViewSet):
    queryset = Tech.objects.all()
    serializer_class = TechSerializer


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer


class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer


class CommitViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = CommitSerializer
