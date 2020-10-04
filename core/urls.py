from django.urls import path

from . import views

urlpatterns = [
    path('',views.home,name="index"),
    path('lang/<str:lang>',views.home_with_language,name="index-lang"),
]
