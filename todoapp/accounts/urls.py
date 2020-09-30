from django.urls import path
from django.contrib.auth import views as auth_views
from .views import register, edit


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
    path('edit/', edit, name="edit"),
    path('password-change/', auth_views.PasswordChangeView.as_view(), name="password_change"),
    path('passworf-change/done/', auth_views.PasswordChangeDoneView.as_view(), name="password_change_done"),
]
