from django.db import models


class ChatQuery(models.Model):
    """Stores a user question and the model's answer."""

    question = models.TextField()
    answer = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # show a short preview in admin lists
        return self.question[:50]
