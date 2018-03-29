# Urlpatterns
from django.urls import path

# Import views
from . import views

urlpatterns = [
	path("", views.index, name="index"),
	path("home", views.index, name="index2"),
	path("about", views.about, name="about"),
	path("3/20/2018/", views.post, name="post"),
	path("contact", views.contact, name="contact"),
]
