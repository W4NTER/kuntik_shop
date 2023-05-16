from django.urls import path
from . import views

urlpatterns = [
    path('', views.Shop.as_view(), name="shop"),
    path('post/<int:post_id>/', views.post, name="post")
]