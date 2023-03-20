from django.contrib import admin
from .models import User, Language, UserLanguage

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(UserLanguage)
class UserLanguageAdmin(admin.ModelAdmin):
    pass
