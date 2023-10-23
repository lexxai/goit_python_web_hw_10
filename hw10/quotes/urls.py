from django.urls import path
from . import views

app_name = 'quotes'

urlpatterns = [
    path('', views.main, name='main'),
    path('<int:page>', views.main, name='main_paginate'),  
    path('author/<str:author>', views.author, name='author'),  
    path('tag/<str:tag>', views.tag, name='tag'),  
    path('tag/<str:tag>/<int:page>', views.tag, name='tag_paginate'),  
]
