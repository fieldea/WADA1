from django.contrib.auth.models import User
from rest_framework import serializers


from .models import  DataSource, Format, Folder, Diagram, Tag, TagDiagram, Comment, Summary, SearchResult


class FormatSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Format
        fields = ['url', 'Year', 'Temp', 'Anomaly']

