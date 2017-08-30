from .models import Vote, Problem, Solution, Tech, Rating, Model, Commit, Notification
from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'password', 'email', 'username']


class TechSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tech
        fields = ['id', 'experience', 'job_title', 'shop', 'user',
                  'tech_rating']


class CommitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Commit
        fields = ['id', 'solution', 'tech', 'posted', 'text', 'url']


class VoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vote
        fields = "__all__"


class SolutionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Solution
        fields = ['id', 'description', 'time_required', 'parts_cost',
                  'problem', 'tech', 'posted', 'score',
                  'url']


class ProblemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Problem
        fields = ['id', 'title', 'system', 'description', 'tech',
                  'model', 'posted', 'url']


class RatingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rating
        fields = "__all__"


class ModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Model
        fields = ['id', 'name', 'brand', 'year', 'url']


class NotificationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Notification
        fields = ['id', 'tech', 'message', 'posted', 'solution', 'commit']
