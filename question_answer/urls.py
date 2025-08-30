from django.urls import path

from .views import Exams_list, Exams_Form


urlpatterns = [
    path('', Exams_list, name='take_exam'),
    path('form/', Exams_Form, name='exam_form'),
]
