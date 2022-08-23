from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Group(models.Model):
    name = models.CharField(max_length=255)
    profiles = models.ManyToManyField(Profile, related_name='profiles')

    def __str__(self):
        return self.name


class Report(models.Model):
    name = models.CharField(max_length=255)
    tags = models.ManyToManyField(Tag)
    groups = models.ManyToManyField(Group)
    author = models.ForeignKey(Profile, on_delete=models.SET_NULL, related_name='author', null=True)
    editors = models.ManyToManyField(Profile, related_name='editors')
    content = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    edited_at = models.DateTimeField(auto_now=True, null=True)
    attachment_ref = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name


class Attachment(models.Model):
    file = models.FileField(blank=True, null=True, upload_to='attachments/%Y/%m/%D/')
    report = models.ForeignKey(Report, on_delete=models.CASCADE)
