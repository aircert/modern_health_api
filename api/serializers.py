from rest_framework import serializers
from .models import Program, Week, Page


class ProgramSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Program
        fields = ('id', 'name', 'owner', 'weeks', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')

    def validate_weeks(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("Program must have 2 or more weeks")
        return value

class WeekSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Week
        fields = ('id', 'name', 'owner', 'pages', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')

    def validate_pages(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("Week must have 2 or more pages")
        return value

class PageSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Page
        fields = ('id', 'name', 'owner', 'audio', 'video', 'article', 'question', 'form', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')
