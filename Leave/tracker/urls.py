from django.urls import path
from .import views
urlpatterns = [
    path('',views.index, name='index'),
    path('dashboard',views.dashboard, name='dashboard'),
    path('apply',views.apply, name='apply'),
    path('total',views.total, name='total'),
    path('login',views.login, name='login'),
    path('register',views.register, name='register'),
    path('profile',views.profile, name='profile'),
    path('logout',views.logout, name='logout'),
    path('profile_update',views.profile_update,name='profile_update'),
    path('delete/<str:id>',views.delete, name='delete'),
    path('preview/<str:id>',views.preview, name='preview'),
    path('profile_edit/<str:id>',views.profile_edit,name='profile_edit'),
]