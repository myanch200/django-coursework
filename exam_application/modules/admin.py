"""
Този сайт се грижи за това кои модели се появяват във администраторския панел
В този случай обозначаваме,че тъй като един курс или модул може да има много изпити 
искаме във формата за курсове да включим и много на брой изпити

"""

from django.contrib import admin

from .models import Module, Exam, ExamRegistration

# TabularInline ще ни даде възможността за добавяне на нови изпити директно в модела на курса
class ExamAdmin(admin.TabularInline):
    model = Exam

class ModuleAdmin(admin.ModelAdmin):
    inlines = [ExamAdmin]


admin.site.register(Module, ModuleAdmin)
admin.site.register(ExamRegistration)
