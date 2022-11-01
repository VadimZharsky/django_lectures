from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView, CreateView, ListView, DetailView, UpdateView, DeleteView
from classroom.models import Teacher
from classroom.forms import ContactForm
# Create your views here.

class HomeView(TemplateView):
    template_name = 'classroom/home.html'



class ThankYouView(TemplateView):
    template_name = 'classroom/thank_you.html'


class TeacherCreateView(CreateView):
    model = Teacher
    # model_form.html
    # .save()
    fields = "__all__"
    success_url = reverse_lazy('classroom:thank_you')


class TeacherListView(ListView):
    # model_list.html
    model = Teacher
    queryset = Teacher.objects.order_by('first_name')
    context_object_name = 'teacher_list'


class TeacherDetailView(DetailView):
    # model_detail.html
    model = Teacher
    # pk --> {{teacher}}


class TeacherUpdateView(UpdateView):
    # share model_form.html 
    model = Teacher
    fields = "__all__"
    success_url = reverse_lazy('classroom:all_teacher_list')


class TeacherDeleteView(DeleteView):
    # form --> confirm delete button
    # default template name
    # model_confirm_delete.html
    model = Teacher
    success_url = reverse_lazy('classroom:all_teacher_list')




class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'classroom/contact.html'

    # URL is not a template html file
    success_url = reverse_lazy('classroom:thank_you')

    #what to do with form?
    def form_valid(self, form):
        print(form.cleaned_data)
        # ContactForm(request, POST)
        return super().form_valid(form)