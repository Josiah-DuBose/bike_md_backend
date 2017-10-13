from rest_framework import viewsets, permissions, generics, filters
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from . import models
from .models import Vote, Problem, Solution, Tech, Rating, Model, Commit, Notification
from .serializers import VoteSerializer, UserSerializer, RatingSerializer
from .serializers import ModelSerializer, SolutionSerializer, CommitSerializer
from .serializers import TechSerializer, NotificationSerializer, ProblemSerializer
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view, renderer_classes
from .forms import LoginForm
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import JsonResponse
import django_filters


# class viewsets
class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    model = User

# def register(request):
#     try:
#         payload = (request.body)
#     except ValueError:
#         return JsonResponse({"error": "Unable to parse request"}, status=400)
#
#     form = RegistrationForm(payload)
#     if form.is_valid():
#         user = user.objects.create_user(
#             form.cleaned_data["username"],
#             form.cleaned_data["email"],
#             form.cleaned_data["password"]
#         )
#         user.save()
#         return JsonResponse({"success": "User registered."}, status=201)
#     return HttpResponse(form.errors.as_json(), status=400, content_type="application/json")

class ModelViewSet(viewsets.ModelViewSet):
    queryset = Model.objects.all().order_by('name')
    serializer_class = ModelSerializer


class ProblemViewSet(viewsets.ModelViewSet):
    queryset = Problem.objects.all().order_by('-posted')
    serializer_class = ProblemSerializer


class SolutionViewSet(viewsets.ModelViewSet):
    queryset = Solution.objects.all()
    serializer_class = SolutionSerializer

class SolutionFilter(django_filters.rest_framework.FilterSet):

    class Meta:
        model = Solution
        fields = ['problem']


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

# Create user/tech
def create_user(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, _('Your profile was successfully updated!'))
            return redirect('settings:profile')
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'profiles/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

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
