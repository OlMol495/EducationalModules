# from django.urls import path
#
# from education.apps import EducationConfig
# from rest_framework.routers import DefaultRouter
#
# from materials.views.course import CourseViewSet
# from materials.views.lesson import (LessonCreateAPIView, LessonListAPIView, LessonUpdateAPIView,
#                                     LessonDestroyAPIView, LessonRetrieveAPIView)
#
#
# app_name = EducationConfig.name
#
# router = DefaultRouter()
# router.register(r'courses', EdModulesViewSet, basename='edmodules')
#
# urlpatterns = [
#                   path('lesson/create/', LessonCreateAPIView.as_view(), name='lesson-create'),
#                   path('lesson/', LessonListAPIView.as_view(), name='lesson-list'),
#                   path('lesson/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson-detail'),
#                   path('lesson/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lesson-update'),
#                   path('lesson/delete/<int:pk>/', LessonDestroyAPIView.as_view(), name='lesson-delete'),
#                   path('subscription/', SubscriptionAPIView.as_view(), name='subscription'),
#               ] + router.urls
