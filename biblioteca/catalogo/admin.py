from django.contrib import admin

from catalogo.models import Author, Genre, Book, Copy, Language

#admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(Copy)
#admin.site.register(Book)

# Register your models here.
class MyAuthorAdmin(admin.ModelAdmin):
    list_display = ('name','surname','birthDate')
admin.site.register(Author,MyAuthorAdmin)

class MyBookAdmin(admin.ModelAdmin):
    list_display = ('title','author','show_genre')
admin.site.register(Book,MyBookAdmin)