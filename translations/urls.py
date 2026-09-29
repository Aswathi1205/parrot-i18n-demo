from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import (
    TranslationViewSet,
    TranslationTableView,
    TranslationUpdateView,
)
from .upload_views import EnglishJSONUploadView

from .views import (
    TranslationViewSet,
    TranslationTableView,
    TranslationUpdateView,
    TranslationExportView,
)

router = DefaultRouter()
router.register("translations", TranslationViewSet)

urlpatterns = [
    path("upload/", EnglishJSONUploadView.as_view()),
    path("translation-table/", TranslationTableView.as_view()),
    path("translation-update/", TranslationUpdateView.as_view()),
    path("translation-export/", TranslationExportView.as_view()),
]

urlpatterns += router.urls