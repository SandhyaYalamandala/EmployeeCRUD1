from django.shortcuts import render, redirect
from .models import Employee
from .forms import EmployeeCreate
from django.http import HttpResponse

# READDING


def index(request):
    shelf = Employee.objects.all()
    return render(request, 'employee/Employee.html', {'shelf': shelf})

# CREATE


def upload(request):
    upload = EmployeeCreate()
    if request.method == 'POST':
        upload = EmployeeCreate(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('index')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'index'}}">reload</a>""")
    else:
        return render(request, 'employee/upload_form.html', {'upload_form': upload})

# UPDATE


def update_employee(request, employee_id):
    employee_id = int(employee_id)
    try:
        employee_sel = Employee.objects.get(id=employee_id)
    except Employee.DoesNotExist:
        return redirect('index')
    employee_form = EmployeeCreate(request.POST or None, instance=employee_sel)
    if employee_form.is_valid():
        employee_form.save()
        return redirect('index')
    return render(request, 'employee/upload_form.html', {'upload_form': employee_form})

# DELETE


def delete_employee(request, employee_id):
    employee_id = int(employee_id)
    try:
        employee_sel = Employee.objects.get(id=employee_id)
    except Employee.DoesNotExist:
        return redirect('index')
    employee_sel.delete()
    return redirect('index')
