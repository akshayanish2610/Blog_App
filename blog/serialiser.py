from rest_framework import serializers
from blog.models import BlogModel

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model=BlogModel
        fields=(
            "user_id",
            "title",
            "msg"
        )