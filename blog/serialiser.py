from rest_framework import serializers
from blog.models import BlogModel,BlogRegistration

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model=BlogModel
        fields=(
            "user_id",
            "title",
            "msg"
        )

class RegSerializer(serializers.ModelSerializer):
    class Meta:
        model=BlogRegistration
        fields=(
            "name",
            "propic",
            "email",
            "password"
        )