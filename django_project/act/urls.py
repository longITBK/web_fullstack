from django.urls import path
from act import views


urlpatterns = [
    path("", views.login_page, name="login"),
    path("login/", views.login_page, name="login"),
    # path("hello/<str:name>", views.hello_there, name="hello"),
    path("home/", views.HomeView.as_view(), name="home"),
    path("building/", views.building, name="building"),
    path("building/create/", views.create_building, name="create_building"),
    path("building/update/<int:id>", views.update_building, name="update_building"),
    path("building/delete/<int:id>", views.delete_building, name="delete_building"),
    path("room/", views.ContactView.as_view(), name="room"),
    path('register/', views.register, name='register')
]