from django.urls import path
from .views import (
    rasm, body,
    PostCreateView,
    PostUpdateView,
    PostDeleteView)
urlpatterns = [
    path('', rasm, name='home'),
    path('body/<str:pk>',body,name='body'),
    path('post/new/',PostCreateView.as_view(),name='post_new'),
    path('post/<int:pk>/edit',PostUpdateView.as_view(),name='post_edit'),
    path('post/<int:pk>/delete',PostDeleteView.as_view(),name='post_delete')
    
]