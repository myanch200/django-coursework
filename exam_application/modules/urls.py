from django.urls import path
from . import views
app_name = "modules"

urlpatterns = [
    path('', views.index, name='index'),
    path('new', views.new, name='new_module'),
    path('create', views.create, name='create_module'),
    path('edit/<int:module_id>', views.edit, name='edit_module'),
    path('update/<int:module_id>', views.update, name='update_module'),
    path('<int:module_id>/', views.show, name='show'),
    path('<int:module_id>/new_exam_registration/<int:exam_id>/', views.new_exam_registration, name='new_exam_registration'),
    path('<int:module_id>/register_for_exam/<int:exam_id>/', views.register_for_exam, name='register_for_exam'),
    # path ('new', views.new, name='new'),
   
]
