from django.contrib import admin
    

from .models import Post


class Admin(admin.ModelAdmin):
    list_filter= ('title','date')
    search_fields =('title',)

admin.site.register(Post,Admin)
