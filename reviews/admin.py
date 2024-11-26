from django.contrib import admin

from .models import Critique
from .models import Film


class FilmAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'casting', 'duration', 'poster')
    search_fields = ('title', 'genre')

    def has_add_permission(self, request):
        return True

    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return True


class CritiqueAdmin(admin.ModelAdmin):
    list_display = ()  # Assurez-vous d'ajouter les champs ici si nécessaire
    search_fields = ()  # Assurez-vous d'ajouter des champs ici si nécessaire

    def has_add_permission(self, request):
        return True

    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return True


admin.site.register(Film, FilmAdmin)
admin.site.register(Critique, CritiqueAdmin)
