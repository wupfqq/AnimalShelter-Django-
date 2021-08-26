from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Animal, Category, Curator, News



class AnimalAd(admin.ModelAdmin):
    list_display = ('name', 'gender', 'age', 'category', 'curator', 'aphoto','available')
    list_display_links = ('name', 'category')
    search_fields = ('name', 'curator')
    list_filter = ('category',)
    list_editable = ('curator',)
    fields = (
        'name', 'gender', 'age', 'category', 'photo', 'aphoto', 'curator', 'description', 'appearence','available'
    )
    readonly_fields = ('aphoto',)

    def aphoto(self, obj):
        if obj.photo:
            return mark_safe(f'<img src={obj.photo.url} width=84px')
        else:
            return 'No photo'
                                                    
    aphoto.short_description = 'Animal photo'

class CategoryAd(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)

class NewsAd(admin.ModelAdmin):
    list_display = ('title','aphoto')
    search_fields = ('title',)

    def aphoto(self, obj):
        if obj.photo:
            return mark_safe(f'<img src={obj.photo.url} width=84px')

class CuratorAd(admin.ModelAdmin):
    list_display = ('name', 'addres', 'aphoto')
    list_display_links = ('name',)
    search_fields = ('name',)
    def aphoto(self, obj):
        if obj.photo:
            return mark_safe(f'<img src={obj.photo.url} width=84px')



admin.site.register(News, NewsAd)
admin.site.register(Animal, AnimalAd)
admin.site.register(Category, CategoryAd)
admin.site.register(Curator, CuratorAd)
admin.site.site_title = "AnimalSheltersCommunity administration"
admin.site.site_header = "AnimalSheltersCommunity administration"
