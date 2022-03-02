from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import CreateView, TemplateView
from .models import Course, Assignment, submit
from .models import sign_up, note, project
# Create your views here.

def home(request):
    return render(request,"index.html") 

def semester(request):
    return render(request,"semester.html")

def courses(request):
    return render(request,"courses.html")


def CSE1(request):
    return render(request,"CSE1.html")

def notes(request):
    if request.method == 'POST':
        doc_file = request.FILES['docx']
        saving = submit.objects.create(file_upload=doc_file)
        saving.save()
        return HttpResponse('Done!submition sucessful!!!.')
    else:

        note_list = note.objects.all()
        return render(request,'Note.html', {'note_list':note_list})
    

def projects(request):

    if request.method == 'POST':
        doc_file = request.FILES['docx']
        saving = submit.objects.create(file_upload=doc_file)
        saving.save()
        return HttpResponse('Done!submition sucessful!!!.')
    else:
        project_list = project.objects.all()
        return render(request,'project.html', {'project_list':project_list})

def assignment(request):

    if request.method == 'POST':
        doc_file = request.FILES['docx']
        saving = submit.objects.create(file_upload=doc_file)
        saving.save()
        return HttpResponse('Done!submition sucessful!!!.')
    else:

        ass_list = Assignment.objects.all()
        return render(request,'assignment.html', {'ass_list':ass_list})

def services(request):
    return render(request,"services.html")
    
def about(request):
    return render(request,"about.html")

def courselist(request):
    course_list = Course.objects.all()
    return render(request,'courselist.html', {'course_list': course_list})

def sign_uppage(request):
    return render(request,'sign_up.html')


def login_page(request):
    return render(request,'login.html')

def signin(request):
    usernm = request.GET.get("username")
    lastnm = request.GET.get("lastname")
    clas = request.GET.get("class")
    eml = request.GET.get("email")
    phnum = request.GET.get("phonenumber")
    passwd = request.GET.get("password")
    stuid = request.GET.get("student_id")
    sign_up(
        first_name = usernm,
        last_name =lastnm,
        student_class = clas,
        phone_number = phnum,
        password = passwd,
        student_ID = stuid
    ).save()
    return render(request, 'sign_up.html',{'message':"successul"})





def loginview(request):
    stuid = request.GET.get("student_id")
    passwd = request.GET.get("password")
    
    x = sign_up.objects.get(student_ID = stuid)
    onlinepass = x.password #sign_up.objects.filter(password == passwd).get(password)

    if passwd == onlinepass:
        return render(request, 'semester.html',{'message':"successul"})   
    else:
        return render(request, 'login.html',{'message':"failed"})



