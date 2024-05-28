from django.urls import path

from education.apps import EducationConfig
from rest_framework.routers import DefaultRouter

from education.views.edmodule import EdModuleViewSet
from education.views.edvideo import (EdVideoCreateAPIView, EdVideoListAPIView, EdVideoUpdateAPIView,
                                     EdVideoDestroyAPIView, EdVideoRetrieveAPIView)


app_name = EducationConfig.name

router = DefaultRouter()
router.register(r'edmodule', EdModuleViewSet, basename='edmodule')

urlpatterns = [
                  path('edvideo/create/', EdVideoCreateAPIView.as_view(), name='edvideo-create'),
                  path('edvideo/', EdVideoListAPIView.as_view(), name='edvideo-list'),
                  path('edvideo/<int:pk>/', EdVideoRetrieveAPIView.as_view(), name='edvideo-detail'),
                  path('edvideo/update/<int:pk>/', EdVideoUpdateAPIView.as_view(), name='edvideo-update'),
                  path('edvideo/delete/<int:pk>/', EdVideoDestroyAPIView.as_view(), name='edvideo-delete'),
              ] + router.urls
