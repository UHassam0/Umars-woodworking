from . import views
from django.urls import path

urlpatterns = [
    path('', views.Homepage.as_view(), name='example_projects'),
    path('projects', views.Projects.as_view(), name='manage'),
    path('createproject', views.CreateProject.as_view(), name='create'),
    path('<int:pk>/edit', views.EditProject.as_view(), name='edit'),
    path('<int:pk>/delete', views.DeleteProject.as_view(), name='delete')
]
