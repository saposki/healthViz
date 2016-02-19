from django.contrib import admin

# Register your models here.
from .models import Dash

class DashModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'timestamp']
    search_fields = ['title']
    class Meta:
        model = Dash

admin.site.register(Dash, DashModelAdmin)
