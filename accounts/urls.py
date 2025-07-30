from django.urls import path
from .views import user_login, dashboard_view, user_register,SignUpView, edit_user, EditUserView
from django.contrib.auth.views import LoginView, LogoutView,PasswordChangeView, PasswordChangeDoneView
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView, PasswordResetDoneView,PasswordResetCompleteView
from .views import admin_page_view


urlpatterns=[
    # path('login/', user_login, name='login'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('password-change/', PasswordChangeView.as_view(), name='password_change'),
    path('password-change-done/', PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password-reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset/complate/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('profile/', dashboard_view, name='user_profile'),
    path('sign_up/', user_register, name='user_register'),
    # path('sign_up/', SignUpView.as_view()   , name='user_register'),
    path('profile/edit/', edit_user, name='profile_edit_infos'),
    # path('profile/edit/', EditUserView.as_view(), name='profile_edit_infos'),
    path('adminpage/', admin_page_view, name='admin_page'),
]