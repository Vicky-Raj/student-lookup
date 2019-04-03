from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .forms import StduentForm
from django.http import HttpResponse
from home.models import Student

def home_page(request):
    if request.method == 'GET':
        if not request.GET.get('name') == None:
            students = [user.student for user in User.objects.filter(first_name__istartswith=request.GET.get('name'))]
            return render(request,'home/home.html',{'students':students})
        return render(request,'home/home.html',{'students':Student.objects.all()})

def detail_page(request,pk):
    student = get_object_or_404(Student,pk=pk)
    return render(request,'home/detail.html',{'student':student})

def stduent_create(request):
    if request.method == 'GET':
        form = StduentForm()
        return render(request,'home/studentform.html',{'form':form})
    if request.method == 'POST':
        user = User()
        user.username = request.POST.get('registerNo')
        user.first_name = request.POST.get('name')
        user.email = request.POST.get('registerNo') + '@skct.edu.in'
        user.set_password('123testpass')
        user.save()
        student = Student()
        student.user = user
        student.reg_no = request.POST.get('registerNo')
        student.dep = request.POST.get('department')
        student.room = request.POST.get('room')
        student.batch = request.POST.get('batch')
        student.parent_no = str(request.POST.get('parentNo'))
        student.student_no = str(request.POST.get('studentNo'))
        student.image = request.FILES['image']
        student.save()
        return redirect('home')

def student_edit(request, pk):
    if request.method == 'GET':
        student = get_object_or_404(Student, pk=pk)
        form = StduentForm(initial={
            'name':student.user.first_name,
            'registerNo':student.reg_no,
            'department':student.dep,
            'room':student.room,
            'batch':student.batch,
            'parentNo':student.parent_no,
            'studentNo':student.student_no,
            'image':student.image
        })
        return render(request,'home/studentform.html',{'form':form})
    if request.method == 'POST':
        student = get_object_or_404(Student, pk=pk)
        student.user.first_name = request.POST.get('name')
        student.user.email = request.POST.get('registerNo') + '@skct.edu.in'
        student.user.save()
        student.reg_no = request.POST.get('registerNo')
        student.dep = request.POST.get('department')
        student.room = request.POST.get('room')
        student.batch = request.POST.get('batch')
        student.parent_no = str(request.POST.get('parentNo'))
        student.student_no = str(request.POST.get('studentNo'))
        if request.FILES.get('image'):
            student.image = request.FILES['image']
        student.save()
        return redirect('home')

def student_delete(request, pk):
    if request.method == 'GET':
        student = get_object_or_404(Student, pk=pk)
        return render(request,'home/delete.html',{'student':student})
    if request.method == 'POST':
        student = get_object_or_404(Student, pk=pk)
        student.user.delete()
        return redirect('home')