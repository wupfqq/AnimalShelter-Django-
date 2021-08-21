from django.contrib import admin
from .models import Animal,Category,Curator
# Register your models here.
class AnimalAd(admin.ModelAdmin):
    list_display = ('name','gender','age','category','curator')
    list_display_links = ('name','category')
    search_fields = ('name','curator')
    list_filter = ('category',)
    list_editable = ('curator',)

class CategoryAd(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)

class CuratorAd(admin.ModelAdmin):
    list_display = ('name','addres')
    list_display_links = ('name',)
    search_fields = ('name',)

admin.site.register(Animal,AnimalAd)
admin.site.register(Category,CategoryAd)
admin.site.register(Curator,CuratorAd)

