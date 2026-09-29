from django.db import models


class TranslationKey(models.Model):
    key = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.key


class Translation(models.Model):
    translation_key = models.ForeignKey(
        TranslationKey,
        on_delete=models.CASCADE,
        related_name="translations"
    )
    locale = models.CharField(max_length=20)
    text = models.TextField()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["translation_key", "locale"],
                name="unique_translation_per_locale"
            )
        ]

    def __str__(self):
        return f"{self.translation_key.key} - {self.locale}"