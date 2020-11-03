from . import views
from django.urls import path
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.index, name='index'),
    path('Task-list', views.TaskList, name='Task-list'),
    path('Task-list/(?P<priority>[a-z]+)', views.TaskList, name='Task-list'),
    path('Task-create', views.TaskCreate, name='Task-create'),
    path('Task-update/<int:id>', views.TaskUpdate, name='Task-update'),
    path('Task-delete/<int:id>', views.TaskDelete, name='Task-delete'),
    # path('Task-filter/(?P<priority>[a-z]+)', views.TaskFilter, name='Task-filter'),

    path('login', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('signup', views.signup, name='signup'),
]
