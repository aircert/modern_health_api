from rest_framework import serializers
from .models import Program, Week, Page


class PageSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Page
        fields = ('id', 'name', 'owner', 'complete', 'audio', 'video', 'article', 'question', 'form', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')

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

class ProgramSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    owner = serializers.ReadOnlyField(source='owner.username')
    progress = serializers.SerializerMethodField()

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Program
        fields = ('id', 'name', 'owner', 'category', 'weeks', 'progress', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')

    def get_progress(self, obj):
        num_pages_complete = self.weeks.filter(pages__complete=True).count()
        num_pages = self.weeks.filter(pages__isnull=False).count()
        if num_pages_complete == 0:
            return 0
        return (num_pages_complete / num_pages) * 100

    def validate_weeks(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("Program must have 2 or more weeks")
        return value
