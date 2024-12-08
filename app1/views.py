from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages


# Home Page view
def HomePage(request):
    return render(request, 'homepage.html')

# Signup Page view
def SignupPage(request):
    if request.method == 'POST':
        username = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password1 = request.POST.get('confirm_password')

        # Check if the passwords match
        if password != password1:
            messages.error(request, "Your password and confirm password do not match.")
            return redirect('signup')  # Redirect back to signup page

        try:
            # Create a new user
            my_user = User.objects.create_user(username=username, email=email, password=password)
            my_user.save()
            messages.success(request, "Registration successful! You can now log in.")
            return redirect('login')  # Redirect to the login page
        except Exception as e:
            messages.error(request, "An error occurred during registration.")
            return redirect('signup')  # Redirect back to signup page

    return render(request, 'signup.html')



# Login Page view
def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to the homepage after successful login
        else:
            # Use messages to display an error
            messages.error(request, 'Invalid username or password')  # Add error message
            return redirect('login')  # Redirect back to the login page

    return render(request, 'login.html')

def grilled_chicken_recipe(request):
    return render(request, 'grilledchi.html')

def speg(request):
    return render(request, 'speg.html')

def avacado(request):
    return render(request, 'avacado.html')
def brownie(request):
    return render(request, 'brownie.html')

def Home(request):
    return render(request, 'home.html')

def recipes(request):
    # Logic to fetch and display recipes
    return render(request, 'recipes.html')

def about(request):
    # Logic for about page
    return render(request, 'about.html')

def recipe_search(request):
    cuisine = request.GET.get('cuisine', '')
    difficulty = request.GET.get('difficulty', '')
    meal_type = request.GET.get('meal-type', '')

    # Build the query based on filters
    recipes = Recipe.objects.all()

    if cuisine:
        recipes = recipes.filter(cuisine=cuisine)
    if difficulty:
        recipes = recipes.filter(difficulty=difficulty)
    if meal_type:
        recipes = recipes.filter(meal_type=meal_type)

    return render(request, 'your_template.html', {'recipes': recipes})

def LogoutPage(request):
    logout(request)
    return redirect('login')

from .models import Recipe

def recipes(request):
    recipes_list = Recipe.objects.all()  # Fetch all recipes
    return render(request, 'recipes.html', {'recipes': recipes_list})

def recipe_detail(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)  # Fetch recipe by ID
    return render(request, 'recipe_detail.html', {'recipe': recipe})

from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Recipe  # Make sure to import the Recipe model
from django.shortcuts import render
from .models import Recipe
from django.shortcuts import render
from .models import Recipe

def recipe_search(request):
    cuisine = request.GET.get('cuisine')
    difficulty = request.GET.get('difficulty')
    meal_type = request.GET.get('meal_type')

    recipes = Recipe.objects.all()

    if cuisine:
        recipes = recipes.filter(cuisine=cuisine)
    if difficulty:
        recipes = recipes.filter(difficulty=difficulty)
    if meal_type:
        recipes = recipes.filter(meal_type=meal_type)

    return render(request, 'home.html', {'recipes': recipes})


def hydbir(request):
    return render(request, 'hydbir.html')


def about(request):
    return render(request, 'about.html')