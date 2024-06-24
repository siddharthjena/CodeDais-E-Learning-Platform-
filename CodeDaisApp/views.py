from django.shortcuts import render,redirect,get_object_or_404
from .forms import signup
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from .models import Course, Enrollment
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    courses = Course.objects.all()
    #courses1 = Course.objects.get(id=1)
    name=request.user
    d = {'courses':courses,'name':name}
    return render(request,'CodeDaisApp/home.html',d)

def register(request):
    if request.method == 'POST':
        f=signup(request.POST)
        if f.is_valid:
            f.save()
            return render(request,'CodeDaisApp/success.html')
    else:
        f=signup()
        d={'form':f}
        return render(request,'CodeDaisApp/signup.html',d)
    
def login_view(request):
    if request.method == 'POST':
        f = AuthenticationForm(request=request, data=request.POST)
        if f.is_valid():
            username = f.cleaned_data['username']
            password = f.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        f = AuthenticationForm()
    return render(request, 'CodeDaisApp/login.html', {'form': f})



def dashboard(request):
    if request.user.is_authenticated:
        # Filter enrolled courses for the logged-in user
        name = request.user
        
        return render(request, 'CodeDaisApp/dashboard.html', {'name': name})
    else:
        return redirect('login')  # Redirect to login page if not logged in

def enrolled_courses(request):
    if request.user.is_authenticated:
        enrolled_courses = Enrollment.objects.filter(user=request.user)
        print(enrolled_courses)
        return render(request, 'CodeDaisApp/enrolled.html', {'enrolled_courses': enrolled_courses})
    else:
        return redirect('login')  # Redirect to login page if not logged in

def buy_course(request, course_id):
    if request.user.is_authenticated:
        course = get_object_or_404(Course, id=course_id)
        if request.method == 'POST':
            Enrollment.objects.create(user=request.user, course=course)
            return redirect('dash')
        return render(request, 'CodeDaisApp/buy_course.html', {'course': course})
    else:
        return redirect('login')  # Redirect to login page if not logged in



def logout_view(request):
    logout(request)
    return redirect('login')


def buy(request):
    return render(request,'CodeDaisApp/buy_course.html')