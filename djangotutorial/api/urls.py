from django.urls import path
from . import views

urlpatterns = [
    path('', views.ApiOverview, name='home'),
    path('posts/', views.add_post, name='add-posts'),
    path('all/', views.view_posts, name='view-posts'),
    path('posts/<int:pk>/', views.post_detail, name='post-detail'),
    path('search/<int:pk>', views.search_post, name='search-post')
]
