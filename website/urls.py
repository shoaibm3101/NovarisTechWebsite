from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", views.home, name="home"),
    path("service/", views.service, name="service"),
    path("contact/", views.contact, name="contact"),
    path("about/", views.about, name="about")
] 
