from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            "id",
            "publish_date",
        ]

    def to_representation(self, instance):
        data = super().to_representation(instance)

        lang = self.context.get("lang", "en")

        if lang == "ta":
            data["title"] = instance.title_ta or instance.title_en
            data["summary"] = instance.summary_ta or instance.summary_en
            data["body"] = instance.body_ta or instance.body_en
        else:
            data["title"] = instance.title_en
            data["summary"] = instance.summary_en
            data["body"] = instance.body_en

        return data