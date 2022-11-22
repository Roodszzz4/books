from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=55)
    photo = models.ImageField(upload_to='image/')
    biography = models.TextField(blank=False, null=False)

    def __str__(self):
        return self.name


class Genre(models.Model):
    title = models.CharField(max_length=55)

    def __str__(self):
        return self.title


class Book(models.Model):
    title = models.CharField(max_length=55)
    created_by = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    year_of_issue = models.IntegerField(blank=False, null=False)
    published = models.CharField(max_length=55)
    language = models.CharField(max_length=20)
    genre = models.ManyToManyField(Genre, blank=True)

    def __str__(self):
        return self.title

    def display_genre(self):
        return ', '.join([genre.title for genre in self.genre.all()])

    display_genre.short_description = 'Genre'
