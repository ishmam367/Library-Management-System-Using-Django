from django.contrib import admin

# Register your models here.

from .models import Author, Genre, Book, BookInstance, Language

#admin.site.register(Book)
#admin.site.register(Author)
admin.site.register(Genre)
#admin.site.register(BookInstance)
admin.site.register(Language)

class BooksInstanceInline(admin.TabularInline):
    model = BookInstance    



class BookInline(admin.TabularInline):
    model = Book   


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines= [BookInline]

admin.site.register(Author, AuthorAdmin)

# Register the Admin classes for Book using the decorator
#Now to create and register the new models; for the purpose of this demonstration, 
#we'll instead use the @register decorator to register the models (this does exactly the same thing as the admin.site.register() syntax):
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]


#Unfortunately we can't directly specify the genre field in list_display because it is a ManyToManyField 
#(Django prevents this because there would be a large database access "cost" in doing so). 



    

# Register the Admin classes for BookInstance using the decorator
@admin.register(BookInstance)




class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')
    list_display = ('book', 'status','due_back','borrower','id')
    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back','borrower')
        }),)

    








