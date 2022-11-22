from django.contrib import admin

from .models import Genre, Book, Author

admin.site.register(Genre)


# admin.site.register(Book)
# admin.site.register(Author)




@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_genre', 'created_by', 'year_of_issue', 'published')
    filter_horizontal = ('genre',)
    list_filter = ('title', 'created_by', 'year_of_issue', 'genre', 'published')


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'photo')


