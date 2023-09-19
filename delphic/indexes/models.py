from django.contrib.auth import get_user_model
from django.db import models
from rest_framework_api_key.models import APIKey

User = get_user_model()


class CollectionStatus(models.TextChoices):
    COMPLETE = "COMPLETE"
    RUNNING = "RUNNING"
    QUEUED = "QUEUED"
    ERROR = "ERROR"


class Document(models.Model):
    collection = models.ForeignKey(
        "Collection", related_name="documents", on_delete=models.CASCADE
    )
    file = models.FileField(upload_to="documents/")
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


class Collection(models.Model):
    # Want to tie the jobs to the source api key
    api_key = models.ForeignKey(APIKey, blank=True, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=CollectionStatus.choices)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    model = models.FileField(upload_to="models/")
    processing = models.BooleanField(blank=True, null=True, default=False)

    def __str__(self):
        return self.title


# class Chat(models.Model):
#     collection = models.ForeignKey(
#         "Collection", related_name="documents", on_delete=models.CASCADE
#     )
#     user = models.ForeignKey(
#         "User", related_name="chats", on_delete=models.CASCADE
#     )
#     chat = models.TextField()
#     created = models.DateTimeField(auto_now_add=True)
#     modified = models.DateTimeField(auto_now=True)
