from django.urls import path
from . import views

urlpatterns = [
    path('', views.postList, name='post-list'),
    path('<int:id>/', views.postDetail, name='post-detail')
]