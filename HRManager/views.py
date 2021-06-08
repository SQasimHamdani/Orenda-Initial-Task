# from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# specific to this view
from django.views.generic import ListView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from employee.models import Employee,Department 
from django.urls import reverse_lazy
from .forms import CreateEmployeeForm

@method_decorator(login_required, name='dispatch')
class EmployeeListView(ListView):

    model = Employee
    template_name = 'HRManager/home.html'
    context_object_name = 'employees'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(EmployeeListView, self).get_context_data(**kwargs)
        departments = Department.objects.all()
        books = self.get_queryset()
        page = self.request.GET.get('page')
        paginator = Paginator(books, self.paginate_by)

        try:
            books = paginator.page(page)
        except PageNotAnInteger:
            books = paginator.page(1)
        except EmptyPage:
            books = paginator.page(paginator.num_pages)
        context['books'] = books
        context['departments'] = departments
        form = CreateEmployeeForm()
        context['form'] = form

        return context

def create_employee(request):
    form = CreateEmployeeForm()
    departments = Department.objects.all()
    
    if request.method == "POST":
        form = CreateEmployeeForm(request.POST, request.FILES or None)
        print(form.data)
        print(request.FILES.get('image'))
        if form.is_valid():

            form.save()
            return redirect("home")
        else:
            print(form.errors.as_data())
            print("invalid Form")
            context = {
                "form" : form,
                "departments" : departments,
                "message" : "Error: Form not saved "
            }

            return render(request,'HRManager/create.html', context)
        
    else:
        pass

    context = {
        "form" : form,
        "departments" : departments,
    }

    return render(request,'HRManager/create.html', context)


def delete_employee(request,id):
    if request.method == "POST":
        emp = get_object_or_404(Employee, id = id)
        if emp:
            emp.delete()
            return redirect("home")
        else:
            print("invalid Form")
            return redirect("home")
    else:
        return reverse_lazy()

def edit_employee(request,id):
    print("received id  = ",id)

    try:
        instance = get_object_or_404(Employee, id = id)
    except:
        return redirect('home')

    form = CreateEmployeeForm(instance=instance)
    departments = Department.objects.all()
    
    if request.method == "POST":

        

        # print(instance)

        form = CreateEmployeeForm(request.POST, request.FILES or None, instance=instance)
        # print(request.FILES.get('image'))
        if form.is_valid():

            form.save()
            print("form saved")
            return redirect("home")
        else:
            print(form.errors.as_data())
            print("invalid Form")
            context = {
                "form" : form,
                "departments" : departments,
                "message" : "Error: Form not saved "
            }

            return render(request,'HRManager/edit.html', context)
        
    else:
        print("Get")
        pass
    
    employee_id = instance.id
    print(employee_id)
    department_name = Employee.objects.filter(id = instance.id )[0].department


    context = {
        "form" : form,
        "departments" : departments,
        "department_name" : department_name,
        "employee_id" : employee_id,
    }
    return render(request,'HRManager/edit.html', context)
