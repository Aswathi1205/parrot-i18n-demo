import json

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser

from .models import TranslationKey, Translation


class EnglishJSONUploadView(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request):
        uploaded_file = request.FILES.get("file")

        if not uploaded_file:
            return Response(
                {"error": "Please upload a JSON file."},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            data = json.load(uploaded_file)
        except json.JSONDecodeError:
            return Response(
                {"error": "Invalid JSON file."},
                status=status.HTTP_400_BAD_REQUEST
            )

        if not isinstance(data, dict):
            return Response(
                {"error": "JSON must contain key-value pairs."},
                status=status.HTTP_400_BAD_REQUEST
            )

        imported_count = 0

        for key, value in data.items():
            translation_key, created = TranslationKey.objects.get_or_create(
                key=key
            )

            Translation.objects.update_or_create(
                translation_key=translation_key,
                locale="en",
                defaults={"text": value}
            )

            if created:
                imported_count += 1

        return Response({
            "message": "English JSON imported successfully.",
            "imported_keys": imported_count
        })