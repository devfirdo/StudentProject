from django.shortcuts import render,redirect
from .import views
from Studentapp.models import Studenttable


def home(request):
    return render(request,'home.html')

def studentdetails(request):
    return render(request,'studentdetails.html')

def submit(request):
    if request.method == 'POST':
        name = request.POST["sname"]
        address = request.POST['saddress']
        age = request.POST['sage']
        email = request.POST['semail']
        date = request.POST['sdate']
        qualification = request.POST['squalification']
        gender = request.POST['sgender']
        number = request.POST['snumber']
        std = Studenttable(StudentName=name,Address=address,Age=age,Email=email,JoiningDate=date,Qualification=qualification,Gender=gender,MobileNumber=number)    
        std.save()
        return redirect('submission')

def submission(request):
    std = Studenttable.objects.all()
    return render(request,'studentdetails.html',{'details':std})

def delete(request,pk):
    std = Studenttable.objects.get(id=pk)
    std.delete()
    return redirect('submission')

def edit(request,pk):
    std = Studenttable.objects.get(id=pk)
    return render(request,'editpage.html',{'editdetails':std})


def update(request,pk):
    if request.method == 'POST':
        std = Studenttable.objects.get(id=pk)
        std.StudentName = request.POST["sname"]
        std.Address = request.POST['saddress']
        std.Age = request.POST['sage']
        std.Email = request.POST['semail']
        std.JoiningDate = request.POST['sdate']
        std.Qualification = request.POST['squalification']
        std.Gender = request.POST['sgender']
        std.MobileNumber = request.POST['snumber']
        std.save()
        return redirect('submission')
    
def personal(request,pk):
    std = Studenttable.objects.get(id=pk)
    return render(request,'personaldetails.html',{'pdetails':std})