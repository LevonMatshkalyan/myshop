from django.contrib import admin
from django.urls import path , include
from .views import *


urlpatterns = [
    path('<int:pk>/' , detail , name='item_detail'),
    path('<int:pk>/delete/' , delete , name='item_delete'),
    path('new' , new , name='item_new'),
    path('<int:pk>/edit/' , edit , name='item_edit'),
    path('',items,name='items')
]
