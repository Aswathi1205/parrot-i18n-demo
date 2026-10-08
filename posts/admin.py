from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            "English",
            {
                "fields": (
                    "title_en",
                    "summary_en",
                    "body_en",
                )
            },
        ),
        (
            "Tamil",
            {
                "fields": (
                    "title_ta",
                    "summary_ta",
                    "body_ta",
                )
            },
        ),
    )