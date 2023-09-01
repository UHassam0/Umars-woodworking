from . import views
from django.urls import path

urlpatterns = [
    path('', views.Homepage.as_view(), name='home'),
    path('projects', views.Projects.as_view(), name='manage'),
    path('createproject', views.CreateProject.as_view(), name='create_project'),
    path('projects/<int:pk>/edit', views.EditProject.as_view(), name='edit_project'),
    path('projects/<int:pk>/delete', views.DeleteProject.as_view(), name='delete_project')
]
