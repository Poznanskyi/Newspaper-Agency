from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from newspapers.models import Newspaper, Topic, Redactor


@admin.register(Redactor)
class RedactorAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("years_of_experience",)
    fieldsets = UserAdmin.fieldsets + (
        (("Additional info", {"fields": ("years_of_experience",)}),)
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            "Additional info",
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "years_of_experience",
                )
            }
        ),
    )


@admin.register(Newspaper)
class NewspaperAdmin(admin.ModelAdmin):
    search_fields = ("title",)
    list_filter = ("topic",)
    list_display = ("title", "publish_date", "topic")
    ordering = ("publish_date",)


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_display = ("name",)
    ordering = ("name",)