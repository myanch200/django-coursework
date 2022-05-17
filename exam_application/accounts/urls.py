from django.urls import path, include
from .views import user_login,profile,logout_view, user_registration
app_name = "accounts"
urlpatterns = [
  path('login/', user_login, name='login'),
  path('profile/', profile, name='profile'),
  path('logout/', logout_view, name='logout'),
  path('register/', user_registration, name='register'),


]