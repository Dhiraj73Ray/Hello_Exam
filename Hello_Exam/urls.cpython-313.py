�
    Er&h�  �                   ��   � S r SSKJr  SSKJrJr  SSKJrJr  SSK	J
r
Jr  \" S\R                  R                  5      \" S\" S5      5      \" S	\
S
S9\" S\SS9\" S\" S5      5      \" S\SS9\" S\SS9/rg)a�  
URL configuration for Hello_Exam project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
�    )�admin)�path�include)�Subjects�	Resources)�Profile�Reportszadmin/� z	core.urlszprof/�profile)�namezsubj/�subjectsztest/zquestion_answer.urlszmat/�materialzstat/�reportN)�__doc__�django.contribr   �django.urlsr   r   �subjects.viewsr   r   �students.viewsr   r	   �site�urls�urlpatterns� �    �KD:\Software Developmemt\Django\Youtube\DJANGO\Hello_Exam\Hello_Exam\urls.py�<module>r      s�   ���  !� %� .� +� 	��5�:�:�?�?�#���W�[�!�"���'�	�*���(��,���'�0�1�2�����,���'��)�	�r   