from django.shortcuts import render

# Create your views here.

def index(request):
    variable = "something"
    context = {'variable':variable}
    return render(request, 'It/index.html', context)


def products(request):
    return render(request, 'It/products.html')


def service(request):
    return render(request, 'It/service.html')


def about(request):
    return render(request, 'It/about.html')


def contact(request):
    return render(request, 'It/contact.html')


# CRUD operation for Class based views.

from It.models import Student

from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView

class StudentReg(CreateView):
	model = Student
	fields = '__all__'
	template_name = 'CBV/studentreg.html'
	success_url ="/"

class Studentlist(ListView):
	model = Student
	template_name = 'CBV/studentlist.html'

class Studentdetail(DetailView):
	model =Student
	template_name = 'CBV/studentdetail.html'

class StudentUpdate(UpdateView):
	model = Student
	fields = "__all__"
	template_name = 'CBV/studentupdate.html'
	success_url ="/"


class StudentDelete(DeleteView):
	model = Student
	template_name = 'CBV/studentdelete.html'
	success_url ="/"
