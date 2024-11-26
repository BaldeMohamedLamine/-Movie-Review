from django.contrib.auth import views as auth_views
from django.urls import path

from .views import profile_view
from users.views import ActivationUserView
from users.views import CustomLoginView
from users.views import CustomUserCreationView
from users.views import LogoutView

urlpatterns = [
    path('', CustomUserCreationView.as_view(), name='register'),
    path('accounts/login/', CustomLoginView.as_view(), name='login'),
    path('accounts/activation/<uid>/<token>', ActivationUserView.as_view(), name='confirm_user_activation'),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),
    path('profile/', profile_view, name='profile'),

    # URL pour la récupération du mot de passe
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),
]
