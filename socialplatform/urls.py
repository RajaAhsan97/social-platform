from django.urls import path
from . import views

app_name = 'social'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('login/', views.loginView, name='login'),
    path('signup/', views.SignupView, name='signup'),
    path('logout/', views.logoutView, name='logout'),

    path('groups_list/', views.groupList, name='group-list'),
    path('posts/<int:group_id>/', views.postList, name='post-list'),

    path('groups/', views.createGroup, name='create-group'),
    path('create-post/', views.createPost, name='create-post'),

    path('group/', views.join_group, name='group-join')
]
