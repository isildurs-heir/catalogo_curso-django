from django.shortcuts import render
from catalogo.models import Genre, Book, Copy, Author, Language
from django.shortcuts import render

# Create your views here.

def index(request):
    nGen = Genre.objects.all().count()
    nLeng = Language.objects.all().count()
    nBooks = Book.objects.all().count()
    nCopys = Copy.objects.all().count()
    nAvailbles = Copy.objects.all().filter(status__exact='a').count()
    nAuthors = Author.objects.all().count()

    context = {
        'nGen':nGen,
        'nLeng':nLeng,
        'nBooks':nBooks,
        'nCopys':nCopys,
        'nAvaibles':nAvailbles,
        'nAuthors':nAuthors,
    }

    return render(request,'index.html',context)