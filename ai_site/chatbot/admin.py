from django.contrib import admin
from .models import ChatQuery


@admin.register(ChatQuery)
class ChatQueryAdmin(admin.ModelAdmin):
    list_display = ("question", "created_at")
    search_fields = ("question",)
from .models import Chat

@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = ("question", "created_at")
    search_fields = ("question",)

