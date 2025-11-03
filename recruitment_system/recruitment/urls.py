from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('jobs/', views.job_list, name='job_list'),
    path('jobs/create/', views.job_create, name='job_create'),
    path('jobs/<int:pk>/update/', views.job_update, name='job_update'),
    path('jobs/<int:pk>/delete/', views.job_delete, name='job_delete'),

    path('candidates/', views.candidate_list, name='candidate_list'),
    path('candidates/create/', views.candidate_create, name='candidate_create'),
    path('candidates/<int:pk>/update/', views.candidate_update, name='candidate_update'),
    path('candidates/<int:pk>/delete/', views.candidate_delete, name='candidate_delete'),

    path('applications/', views.application_list, name='application_list'),
    path('applications/create/', views.application_create, name='application_create'),
    path('applications/<int:pk>/update/', views.application_update, name='application_update'),
    path('applications/<int:pk>/delete/', views.application_delete, name='application_delete'),
]