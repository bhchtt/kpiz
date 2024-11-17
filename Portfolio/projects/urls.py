# projects/urls.py
from django.urls import path
from .views import project_list, project_create, project_update, project_delete

app_name = 'projects'

urlpatterns = [
    path('', project_list, name='project_list'),
    path('create/', project_create, name='project_create'),
    path('<int:pk>/update/', project_update, name='project_update'),
    path('<int:pk>/delete/', project_delete, name='project_delete'),
]


