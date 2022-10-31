from datetime import datetime
from django import http
from django.http import HttpResponse
from django.shortcuts import render
from .models import Department,Role,Employee
from django.db.models import Q

def index(request):
  return render(request,'index.html')

def all_emp(request):
  emp = Employee.objects.all()
  context = {
    'emp':emp
  }
  return render(request,'all_emp.html',context)

def add_emp(request):
  if request.method == 'POST':
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    dept = int(request.POST['dept'])
    salary = int(request.POST['salary'])
    bonus = int(request.POST['bonus'])
    role = int(request.POST['role'])
    phone = int(request.POST['phone'])
    new_emp = Employee(first_name=first_name,last_name=last_name,dept_id=dept,salary=salary,bonus=bonus,role_id=role,phone=phone,joining_date=datetime.now())
    new_emp.save()
    return HttpResponse("<h1>Employee added successfully<h1>")

  elif request.method == 'GET':
    return render(request,'add_emp.html')
  
  else:
    return HttpResponse("Invalid request")

def remove_emp(request, emp_id = 0):
  if emp_id:
    try:
      emp_to_be_removed = Employee.objects.get(id=emp_id)
      emp_to_be_removed.delete()
      return HttpResponse("<h3>Employee removed successfully<h3>")
    except:
      return HttpResponse("Employee not found")

  emps = Employee.objects.all()
  context = {
    'emps':emps
  }
  return render(request,'remove_emp.html',context)

def filter_emp(request):
  if request.method == 'POST':
    name = request.POST['name']
    dept = request.POST['dept']
    role = request.POST['role']

    emps = Employee.objects.all()
    if name:
      emps = emps.filter(Q(first_name__icontains= name) | Q(last_name__icontains= name))
      # updating the emps with the filtered data
    
    if dept:
      emps = emps.filter(dept__name__icontains=dept)
    
    if role:
      emps = emps.filter(role__name__icontains=role)
    
    context = {
      'emp':emps
    }
    return render(request,'all_emp.html',context)
      

  elif request.method == 'GET':
    return render(request,'filter_emp.html')

  else:
    return HttpResponse("Invalid request")

