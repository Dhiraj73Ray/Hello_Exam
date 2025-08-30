from django.urls import path

from .views import subject_list, subject_all, subject_enroll, subject_remove, Materials, upload_document, delete_document


urlpatterns = [
    path('subjects', subject_list, name="subject_list"),
    path("subjects/all/", subject_all, name="subject_all"),
    path("enroll/", subject_enroll, name="subject_enroll"),
    path("remove/delete/<int:pk>/", subject_remove, name="subject_remove"),
    path('materials/', Materials, name='material'),
    path('upload_document/', upload_document, name='upload_document'),
    path("materials/delete/<int:pk>/", delete_document, name="delete_document"),
]
