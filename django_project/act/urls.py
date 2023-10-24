from django.urls import path
from act import views


urlpatterns = [
    path("", views.login_page, name="login"),
    path("login/", views.login_page, name="login"),
    # path("hello/<str:name>", views.hello_there, name="hello"),
    path("home/", views.home, name="home"),
    path("information/", views.information, name="information"),
    path("contact/", views.contact, name="contact"),
    path('register/', views.register, name='register')
]