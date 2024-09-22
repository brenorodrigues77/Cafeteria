from django.contrib import admin
from cafeteria.models import coffe

class coffeadmin(admin.ModelAdmin):
    list_display = ('title', 'description','value',)
    search_field = ('title')

admin.site.register(coffe, coffeadmin)