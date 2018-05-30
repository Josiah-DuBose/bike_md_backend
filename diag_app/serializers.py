from .models import Problem, Solution, Tech, Model, Commit, Notification, Brand, Year
from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance

    class Meta:
        model = User
        fields = ['id', 'password', 'email', 'username']


class TechSerializer(serializers.ModelSerializer):
    included_serializers = {
        "user": UserSerializer,
    }

    class Meta:
        model = Tech
        fields = ['id', 'experience', 'job_title', 'shop', 'user',
                  'tech_rating']

    class JSONAPIMeta:
        included_resources = ['user']


class CommitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Commit
        fields = ['id', 'solution', 'tech', 'posted', 'text', 'url']


class SolutionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Solution
        fields = ['id', 'description', 'time_required', 'parts_cost',
                  'problem', 'tech', 'posted', 'score',
                  'url']


class ProblemSerializer(serializers.ModelSerializer):
    included_serializers = {
        "tech": TechSerializer,
    }

    class Meta:
        model = Problem
        fields = ['id', 'title', 'system', 'description', 'tech',
                  'model', 'posted', 'mileage', 'url']


    class JSONAPIMeta:
        included_resources = ['tech']


class BrandSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Brand
        fields = ['id', 'name', 'make_id']


class YearSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Year
        fields = ['id', 'value']



class ModelSerializer(serializers.ModelSerializer):
    included_serializers = {
        "problems": ProblemSerializer,
    }

    class Meta:
        model = Model
        fields = ['id', 'name', 'brand', 'year', 'url', 'problems']

    class JSONAPIMeta:
        included_resources = ['problems']


class NotificationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Notification
        fields = ['id', 'tech', 'message', 'posted', 'solution', 'commit']
