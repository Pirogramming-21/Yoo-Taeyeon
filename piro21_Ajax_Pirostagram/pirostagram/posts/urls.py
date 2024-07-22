from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('like/<int:post_id>/', views.like_post, name='like_post'),
    path('comment/<int:post_id>/', views.add_comment, name='add_comment'),
    path('comment/delete/<int:comment_id>/', views.delete_comment, name='delete_comment'),
]