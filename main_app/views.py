# main_app/views.py

from django.shortcuts import render



class Cat:
    def __init__(self, name, breed, description, age):
        self.name = name
        self.breed = breed
        self.description = description
        self.age = age
# Create a list of Cat instances
cats = [
    Cat('Lolo', 'tabby', 'Kinda rude.', 3),
    Cat('Sachi', 'tortoiseshell', 'Looks like a turtle.', 0),
    Cat('Fancy', 'bombay', 'Happy fluff ball.', 4),
    Cat('Bonk', 'selkirk rex', 'Meows loudly.', 6)
]

# Define the home view function so that utl.py can use home function
def home(request):
    # Send a simple HTML response
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def cat_index(request):
    return render(request, "cats/index.html", {"cats":cats})
