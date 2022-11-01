from audioop import reverse
from django.shortcuts import render
from .models import Book, BookInstance 
from django.views.generic import CreateView, DetailView, ListView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


def index(request):
    return render(request, 'catalog/index.html')

@login_required
def all_books(request):
    num_books = Book.objects.all()
    
    context ={'num_books':num_books}
    return render(request,'catalog/all_books.html', context=context)

def get_a_book(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_avail = BookInstance.objects.filter(status__exact='a').count()

    context = {
        'num_books':num_books,
        'num_instances':num_instances,
        'num_instances_avail':num_instances_avail
    }
    return render(request,'catalog/get_a_book.html',context=context )


class BookCreate(LoginRequiredMixin ,CreateView): #model_form.html

    model = Book
    fields = '__all__'
    #success_url = reverse_lazy("catalog:all_books")
    #success_url = reverse_lazy('app_name:post_detail' pk=post.id)


class BookDetail(DetailView):
    model = Book 


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'catalog/signup.html'


class CheckedOutBooksByUserView(LoginRequiredMixin, ListView):
    # List all book instances but filtered based off currently logged in user section
    model = BookInstance
    template_name = 'catalog/profile.html'
    paginate_by = 5 # 5 book instances per page

    def get_queryset(self):
        return BookInstance.objects.filter(borrover=self.request.user)