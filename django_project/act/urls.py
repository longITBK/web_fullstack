from django.urls import path
from act import views


urlpatterns = [
    path("", views.login_page, name="login"),
    path("login/", views.login_page, name="login"),
    # path("hello/<str:name>", views.hello_there, name="hello"),
    path("home/", views.HomeView.as_view(), name="home"),
    path("building/", views.InformationView.as_view(), name="building"),
    path("room/", views.ContactView.as_view(), name="room"),
    path('register/', views.register, name='register')
]