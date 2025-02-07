# main_app/views.py

from django.shortcuts import render

# Import HttpResponse to send text-based responses, like <h1>, <p> etc.
from django.http import HttpResponse

# Define the home view function so that utl.py can use home function
def home(request):
    # Send a simple HTML response
    return HttpResponse('<h1>Hello ᓚᘏᗢ</h1>')

def about(request):
    return render(request, "about.html")