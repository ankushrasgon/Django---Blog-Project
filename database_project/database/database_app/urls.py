from django.conf.urls import url
from database_app import views
from django.urls import path
urlpatterns =[
path('',views.homepage,name='homepage'),
path('post/<int:pk>/', views.post_detail, name='post_detail'),
path('post/new/',views.post_new, name='post_new'),
path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
path('drafts/',views.post_draft_list,name='post_draft_list'),
path('post/<pk>/publish/', views.post_publish, name='post_publish'),
path('post/<pk>/remove/', views.post_remove,name='post_remove'),
path('post/<int:pk>/comment',views.add_comment_to_post,name='add_comment_to_post'),
]
