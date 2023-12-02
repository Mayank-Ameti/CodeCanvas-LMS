from django.urls import path
from .import views

urlpatterns = [
    path('instructor/',views.InstructorList.as_view()),
    path('instructor/<int:pk>/',views.InstructorDetail.as_view()),

]