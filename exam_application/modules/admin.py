from django.contrib import admin

from .models import Module, Exam, ExamRegistration
# Register your models here.

class ExamAdmin(admin.TabularInline):
    model = Exam

class ModuleAdmin(admin.ModelAdmin):
    inlines = [ExamAdmin]


admin.site.register(Module, ModuleAdmin)
admin.site.register(ExamRegistration)
