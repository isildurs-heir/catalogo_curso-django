from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from catalogo.models import Genre, Book, Copy, Author, Language
from catalogo.forms import GenreForm, AuthorForm
from django.http import JsonResponse
# Create your views here.

#testeando ajax
def test_ajax(request):
    return render(request,'test-ajax.html')

def getData(request):
    xd = Book.objects.all()
    libros = list(xd.values('title'))
    data = {'message':'damn','libros':libros}
    return JsonResponse(data)
#testeando ajax

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

class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 2
    context_object_name = 'authors'
    queryset = Author.objects.all()
    template_name = 'authors.html'

    #preguntar por funcion vista dentro de esta clase

def AuthorDetail(request,pk):
    author = Author.objects.get(pk = pk)
    books = Book.objects.filter(author__id = author.id)

    context = {
        'author':author,
        'books':books,
    }
    return render(request,'author.html',context)

class BookListView(generic.ListView):
    model = Book
    paginate_by = 3
    context_object_name = 'books'
    queryset = Book.objects.all()
    template_name = 'books.html'

def BookDetail(request,pk):
    book = Book.objects.get(pk = pk)
    author = book.author
    #author = Author.objects.filter(pk__exact = auth.id)

    context = {
        'book':book,
        'author':author,
    }
    return render(request,'book.html',context)


def genre_new(request):
    if request.method == "POST":
        formulario = GenreForm(request.POST)
        if formulario.is_valid():
            genero = formulario.save(commit=False)
            genero.name = formulario.cleaned_data['name']
            genero.save()
            return redirect('generos')
    else:
        formulario = GenreForm()

        return render(request, 'genero_new.html', {'formulario':formulario})

def genre_update(request,pk):
    genero = get_object_or_404(Genre, pk = pk)
    if request.method == "POST":
        formulario = GenreForm(request.POST, instance=genero)
        if formulario.is_valid():
            genero = formulario.save(commit=False)
            genero.nombre = formulario.cleaned_data['name']
            genero.save()
            return redirect('generos')
    else:
        formulario = GenreForm(instance=genero)
    return render(request,'genero_new.html', {'formulario':formulario})

class GenreListView(generic.ListView):
    model = Genre
    paginate_by = 2
    context_object_name = 'generos'
    queryset = Genre.objects.all()
    template_name = 'generos.html'