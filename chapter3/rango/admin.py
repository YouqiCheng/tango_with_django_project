from django.contrib import admin
from rango.models import Category, Page
#from rango.models import UserProfile

class PageAdmin(admin.ModelAdmin):
    list_display = ('title','category','url')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('views','likes')


admin.site.register(Category,CategoryAdmin)
admin.site.register(Page,PageAdmin)
#admin.site.register(UserProfile)
# Register your models here.
