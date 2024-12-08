from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage, name='homepage'),
    path('signup/', views.SignupPage, name='signup'),
    path('login/', views.LoginPage, name='login'),
    path('logout/', views.LogoutPage, name='logout'),
    path('recipes/grilled-chicken/', views.grilled_chicken_recipe, name='grilledchi'),
    path('recipes/Spaghetti Carbonara/', views.speg, name='speg'),
    path('recipes/Avacado toast/', views.avacado, name='avacado'),
    path('recipes/chocolate browines/', views.brownie, name='brownie'),
    path('home/',views.Home, name ='home'),
    path('recipes/', views.recipes, name='recipes'),
    path('about/', views.about, name='about'),
    path('search/', views.recipe_search, name='recipe_search'),
    path('recipes/<int:recipe_id>/', views.recipe_detail, name='recipe_detail'),
    path('search/', views.recipe_search, name='recipe_search'),
    path('recipe_search/', views.recipe_search, name='recipe_search'),
    path('recipes/hydbir/', views.hydbir, name='hydbir'),
    path('about/',views.about, name='about'),

]