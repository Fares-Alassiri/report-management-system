from django.urls import path
from core import views

urlpatterns = [
    path('', views.home),
    path('report/', views.reports,),
    path('report/<str:pk>/', views.report),
    path('report/<str:pk>/update', views.update_report),
    path('report/<str:pk>/delete', views.delete_report),
    path('report/create', views.create_report),
    path('report/<str:rid>/delete_attatchment/<str:aid>', views.delete_attachment),
]