from django.urls import path
from . import views

urlpatterns = [
    path('hello-world/', views.hello_world),
    path('articles/', views.AricleView.as_view())
]
