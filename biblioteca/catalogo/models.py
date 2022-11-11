from django.db import models
from django.urls import reverse
import uuid

# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    birthDate = models.DateField(null=True,blank=True)
    deathDate = models.DateField('Deceased',null=True,blank=True)
    #img

    def get_absolute_url(self):
        return reverse('autorInfo',args=[str(self.id)])

    def __str__(self):
        return '%s, %s' %(self.name,self.surname)

    class Meta:
        ordering = ['id']

class Language(models.Model):
    name = models.TextField(max_length=50)

    def __str__(self):
        return '%s (%s)' %(self.id,self.name)

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author,on_delete=models.SET_NULL,null=True)
    description = models.TextField(max_length=1000)
    isbn = models.CharField('ISBN',max_length=13,help_text='help_text=13 Caracteres <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    genre = models.ManyToManyField(Genre)
    lenguage = models.ForeignKey(Language,on_delete=models.SET_NULL,null=True)

    def get_absolute_url(self):
        return reverse('BookInfo',args=[str(self.id)])
    
    def __str__(self):
        return self.title

    def show_genre(self):
        return ', '.join([genre.name for genre in self.genre.all() [:2]])

    show_genre.short_description = 'Genre/s'

    class Meta:
        ordering = ['id']

class Copy(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4)
    book = models.ForeignKey(Book,on_delete=models.SET_NULL,null=True)
    returnDate = models.DateField(null=True,blank=True)

    COPY_STATUS = (
        ('m','maintenance'),
        ('o','out'),
        ('a','available'),
        ('r','reserved'),
    )
    status = models.CharField(max_length=1,choices=COPY_STATUS,blank=True,default='a')

    class Meta:
        ordering = ["returnDate"]

    def __str__(self):
        return '%s (%s)' %(self.id,self.book.title)