import datetime

from django.db import models
from django.utils import timezone

from django.contrib import admin

class Member(models.Model):
    Name = models.CharField(max_length=200)
    Email = models.CharField(max_length=255)


class DataSource(models.Model):
    Location = models.CharField(max_length=200)
    StartID = models.IntegerField(default=0)
    EndID = models.IntegerField(default=0)


class Format(models.Model):
    # ID = models.IntegerField(default=0)
    Year = models.IntegerField(default=0)
    Temp = models.FloatField(default=0.0)
    Anomaly = models.FloatField(default=0.0)


class Folder(models.Model):
    Title = models.CharField(max_length=255)


class Diagram(models.Model):
    # ID = models.IntegerField(default=0)
    Type = models.IntegerField(default=0)
    DataSourceID = models.ForeignKey(DataSource, on_delete=models.CASCADE)
    MemberID = models.ForeignKey(Member, on_delete=models.CASCADE)
    Title = models.CharField(max_length=255)
    Description = models.CharField(max_length=255)
    UploadDate = models.DateTimeField()
    Visit = models.IntegerField(default=0)


class Tag(models.Model):
    # ID = models.IntegerField(default=0)
    Title = models.CharField(max_length=255)


class TagDiagram(models.Model):
    TagID = models.ForeignKey(Tag, on_delete=models.CASCADE)
    DiagramID = models.ForeignKey(Diagram, on_delete=models.CASCADE)


class Comment(models.Model):
    # ID = models.IntegerField(default=0)
    DiagramID = models.ForeignKey(Diagram, on_delete=models.CASCADE)
    PostDate = models.DateTimeField()
    Content = models.CharField(max_length=255)


class Summary(models.Model):
    MemberID = models.ForeignKey(Member, on_delete=models.CASCADE)
    Visit = models.IntegerField(default=0)


class SearchResult(models.Model):
    Keyword = models.CharField(max_length=255)
    Order = models.IntegerField(default=0)
    DisplayMode = models.IntegerField(default=0)


class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField()


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'password', 'email')









