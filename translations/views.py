from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import TranslationKey, Translation
from .serializers import TranslationSerializer
from django.http import JsonResponse

class TranslationViewSet(viewsets.ModelViewSet):
    queryset = Translation.objects.all()
    serializer_class = TranslationSerializer


class TranslationTableView(APIView):

    def get(self, request):
        keys = TranslationKey.objects.all()

        table = []

        for key in keys:
            translations = Translation.objects.filter(
                translation_key=key
            )

            row = {
                "key": key.key,
                "en": "",
                "ta": "",
                "hi": ""
            }

            for translation in translations:
                row[translation.locale] = translation.text

            table.append(row)

        return Response(table)


class TranslationUpdateView(APIView):

    def post(self, request):
        key = request.data.get("key")
        locale = request.data.get("locale")
        text = request.data.get("text")

        if not key or not locale:
            return Response(
                {"error": "key and locale are required."},
                status=400
            )

        try:
            translation_key = TranslationKey.objects.get(key=key)
        except TranslationKey.DoesNotExist:
            return Response(
                {"error": "Translation key not found."},
                status=404
            )

        if locale == "en":
            return Response(
                {"error": "English is the default language and cannot be changed."},
                status=400
            )

        translation, created = Translation.objects.update_or_create(
            translation_key=translation_key,
            locale=locale,
            defaults={"text": text or ""}
        )

        return Response({
            "message": "Translation saved successfully.",
            "key": key,
            "locale": locale,
            "text": translation.text
        })
class TranslationExportView(APIView):

    def get(self, request):
        locale = request.query_params.get("locale")

        if not locale:
            return Response(
                {"error": "Please provide a locale."},
                status=400
            )

        translations = Translation.objects.filter(
            locale=locale
        ).select_related("translation_key")

        data = {}

        for translation in translations:
            data[translation.translation_key.key] = translation.text

        response = JsonResponse(data, json_dumps_params={"ensure_ascii": False})
        response["Content-Disposition"] = f'attachment; filename="{locale}.json"'

        return response