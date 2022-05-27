from django.urls import path
#import-ваме всяка нужна ни функция от views.py 
# така на всеки url е приспособена функция.
from .views import user_login,profile,logout_view, user_registration 



app_name = "accounts" # Даваме име на това под приложение, което ни дава възможността да извикваме лесно всеки от тези urlpattern-и  по име
# наппример вместо /profile можем да извикаме същата функция със: accounts:profile
# това е особено полезно, ако в няколко под приложения имаме същата фукнция /profile
# можем да извикаме всяка една от тях с името на под приложението и името на пътя. 
urlpatterns = [
  path('login/', user_login, name='login'),
  path('profile/', profile, name='profile'),
  path('logout/', logout_view, name='logout'),
  path('register/', user_registration, name='register'),


]