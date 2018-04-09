# Urlpatterns
from django.urls import path

# Import views
from . import views

urlpatterns = [
	# Main
	path("", views.index, name="index"),
	path("about", views.about, name="about"),
	path("contact", views.contact, name="contact"),
	# Utils
	path("page_under_construction", views.page_under_construction, name="page_under_construction"),
	# Posts
	path("11/22/2017", views.workstation, name="workstation"),
	path("12/15/2017", views.database_scratch, name="database_scratch"),
	path("12/30/2017", views.first_ai_product, name="first_ai_product"),
	path("1/10/2018", views.meta_architectures_and_feature_extractors, name="meta_architectures_and_feature_extractors"),
]
