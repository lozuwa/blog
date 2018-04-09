from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	return render(request, "blog/index.html")

def contact(request):
	return render(request, "blog/contact.html")

def about(request):
	return render(request, "blog/about.html")

# Posts
def workstation(request):
	return render(request, "blog/create_your_own_deep_learning_workstation.html")

def database_scratch(request):
	return render("blog/lessons_learned_from_making_an_image_database_from_scratch.html")

def first_ai_product(request):
	return render("blog/lessons_learned_from_creating_an_AI_product.html")

def metra_architectures_and_feature_extractors(request):
	return render("blog/index.html")
