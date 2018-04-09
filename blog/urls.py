# Urlpatterns
from django.urls import path

# Import views
from . import views

urlpatterns = [
	path("", views.index, name="index"),
	path("home", views.index, name="index2"),
	path("about", views.about, name="about"),
	path("11/22/2017", views.workstation, name="workstation"),
	path("12/15/2017", views.database_scratch, name="database_scratch"),
	path("12/30/2017", views.first_ai_product, name="first_ai_product"),
	path("1/10/2018", views.metra_architectures_and_feature_extractors, name="metra_architectures_and_feature_extractors"),
	path("contact", views.contact, name="contact"),
]
