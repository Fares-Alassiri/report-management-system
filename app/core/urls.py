from django.urls import path

from django.contrib.auth import views as auth_views

from core import views

urlpatterns = [
    path('', views.home),
    path('signin', views.signin, name='signin'),
    path('signup', views.signup, name='signup'),
    path('signout', views.signout, name='signout'),
    path('account', views.account, name='account'),
    path('accounts/login/', views.accounts_login),
    path('account/editemail', views.editemail, name='editemail'),
    path('account/editpass', views.editpass, name='editpass'),
    path('reset_password/', auth_views.PasswordResetView.as_view(), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    path('report/', views.reports, name="reports"),
    path('reports/new/', views.reports_new, name="reports_new"),
    path('report/<str:pk>/', views.report),
    path('report/<str:pk>/update', views.update_report),
    path('report/<str:pk>/delete', views.delete_report),
    path('create/', views.create_report, name="create"),
    path('report/<str:rid>/delete_attatchment/<str:aid>', views.delete_attachment),
]