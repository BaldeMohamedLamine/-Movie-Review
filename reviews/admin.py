from django.contrib import admin
from .models import Film,Critique

class FimlAdmin(admin.ModelAdmin):
    list_display = ('title','genre','casting','duration','poster')
    search_fields = ('title','genre',)

    def has_add_permission(self, request):
        return True
    
    def has_change_permission(self, request, obj = None):
        return True
    
    def has_delete_permission(self, request, obj = None):
        return True

class CritiqueAdmin(admin.ModelAdmin):
    list_display = ()
    search_fields = ()

    def has_add_permission(self, request):
        return True
    
    def has_change_permission(self, request, obj = None):
        return True
    
    def has_delete_permission(self, request, obj = None):
        return True
    
admin.site.register(Film,FimlAdmin)
admin.site.register(Critique,CritiqueAdmin)