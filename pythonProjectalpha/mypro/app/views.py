from django.shortcuts import render, HttpResponse, redirect, reverse
from .models import Customer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.


class Student:
    def __init__(self, name, course, age, marks):
        self.name = name,
        self.course = course,
        self.age = age,
        self.marks = marks,


std_data = [
    {'Name': 'Rayan', 'course': 'Python', 'Age': 20, 'Marks': 99},
    {'Name': 'Saad', 'course': 'C++', 'Age': 40, 'Marks': 100},
    {'Name': 'Sultan', 'course': 'CSS', 'Age': 32, 'Marks': 89},
    {'Name': 'Salar', 'course': 'Html', 'Age': 18, 'Marks': 80},
    {'Name': 'Humayun', 'course': 'Dart', 'Age': 35, 'Marks': 70},
    {'Name': 'Atif', 'course': 'Java', 'Age': 30, 'Marks': 75},
    {'Name': 'The Atif', 'course': 'Java', 'Age': 30, 'Marks': 75},
]

student = []


def index(request):
    # student.list()
    for i in range(len(std_data)):
        std_obj = Student(std_data[i]['Name'], std_data[i]['course'], std_data[i]['Age'], std_data[i]['Marks'])
        student.append(std_obj)
        # print(student)
    return render(request, 'index.html', {'std_data': student})


def data(request):
    if request.method == "POST":
        email = request.POST['em']
        password = request.POST['ps']
        customer_obj = Customer(email=email, password=password)

        try:
            customer_obj.save()
            # return redirect(reverse('data'))
            return HttpResponse('Data Saved')
        except:
            return HttpResponse('Data Not Saved')
    # name = request.POST['name']
    # course = request.POST['course']
    # age = request.POST['age']
    # marks = request.POST['marks']
    # # print(f"{name} , {course1} , {age} , {marks}")
    # std_obj = Student(name, age, course, marks)
    # student.append(std_obj)
    else:
        # obj = Customer.objects.get(email='rayan@gmail.com')
        obj = Customer.objects.all()
        return render(request, 'home.html', {'cus_data': obj})


def hello(request):
    return render(request, 'Hello.html')


def delete(request, id):
    obj = Customer.objects.get(pk=id)
    try:
        obj.delete()
        return redirect(reverse('data'))
    except:
        return HttpResponse('Data not Deleted')


def update(request, id):
    if request.method == 'POST':
        email = request.POST['em']
        password = request.POST['ps']
        obj = Customer.objects.get(pk=id)
        obj.email = email
        obj.password = password
        try:
            obj.save()
            return redirect(reverse('data'))
        except:
            return HttpResponse('YOu data bher ka lun')
    obj = Customer.objects.get(pk=id)

    return render(request, 'update.html', {'cus': obj})


def main(request):
    return render(request, 'main.html')


# @login_required(login_url='my_login')
def admin_panel(request):
    if request.user.is_authenticated:
        return render(request, 'admin.html')
    else:
        return redirect(reverse('my_login'))


# else:
#     return redirect(reverse('my_login'))


def my_login(request):
    if request.method == 'POST':
        email = request.POST['em']
        password = request.POST['ps']
        user = authenticate(username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse('admin'))
        else:
            return render(request, 'my_login.html', {'mes': 'Wrong Credentials'})
    return render(request, 'my_login.html')


def signup(request):
    email=request.POST['em']
    username=request.POST['username']
    password=request.POST['ps']

    obj=
    return render(request, 'signup.html')


def my_logout(request):
    logout(request)
    return redirect(reverse('my_login'))
