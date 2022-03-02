from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings




urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('services/', views.services, name="services"),
    path('semester/', views.semester, name="semester"),
    path('courses/', views.courses, name="courses"),
    path('CSE1/', views.CSE1, name="CSE1"),
    path('courselist/', views.courselist, name="courselist"),
    path('assignment/', views.assignment, name="assignment"),
    path('projects/', views.projects, name="projects"),
    path('notes/', views.notes, name="notes"),
    path('sign_up/', views.sign_uppage, name="sign_up"),
    path('loginuser/', views.login_page, name="loginuser"),
    path('loginurl/', views.loginview, name="loginurl"),
    path('siginuser/', views.signin),
   

]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
