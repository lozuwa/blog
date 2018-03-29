from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	return render(request, "blog/index.html")

def post(request):
	print(request.POST.get("id"))
	return render(request, "blog/lessons_learned_from_making_an_image_dataset_from_scratch.html")

def contact(request):
	return render(request, "blog/contact.html")

def about(request):
	return render(request, "blog/about.html")
