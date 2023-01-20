from django.urls import path, include
from .views import Home, Login, DoLogin, DoLogout

urlpatterns = [
    path("", Home, name="admin.index"),
    path("/", Home, name="admin.index"),
    #path("propertycontacts/", include("PropertyContact.urls")),
    path("login", Login, name="login"),
    path("dologin", DoLogin, name="dologin"),
    path("dologout", DoLogout, name="dologout"),
]
