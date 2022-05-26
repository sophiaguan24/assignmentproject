from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import View
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from assignments.models import Assignment, StudentProfile, Subject

class IndexView(View):
    def get(self, request):
        # We'll use the built-in authenticaion form
        form = AuthenticationForm()
        # Send the template the form and the posts.
        context = {
            'form': form,
            'user': request.user,
        }
        return render(request, 'assignments/login.html', context)
    def post(self,request):
        if 'logout' in request.POST.keys():
            logout(request)
            form = AuthenticationForm()
        else:
            form = AuthenticationForm(data=request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(username = username, password = password)
                if user is not None:
                    login(request, user = user)
        context = {
            'form': form
        }
        return render(request, 'assignments/login.html', context)

class AssignmentView(View):
    # @login_required
    def get(self, request, username):
        user = request.user
        allAssignments = user.assignment_set.all()
        allClasses = user.subject_set.all()
        context = {'allAssignments': allAssignments,
        'allClasses': allClasses,
        'user': user,
        'authenticated': request.user
        }
        return render(request, 'assignments/assignment.html', context)
    def post(self, request, username):
        user = request.user
        allAssignments = user.assignment_set.all()
        allClasses = user.subject_set.all()
        name = request.POST['assignmentName']
        description = request.POST['assignmentDescription']
        dueDate = request.POST['assignmentDue']
        if not dueDate:
            dueDate = "2001-01-01 00:00"
        complete = request.POST.get('assignmentComplete') == 'on'
        assignmentClass = request.POST['subject']
        subject = Subject.objects.get(id=assignmentClass)
        print(complete)
        assignment=Assignment(userAssignments=user,assignmentClass=subject,name=name, description=description, dueDate=dueDate, complete=complete)
        assignment.save()
        context = {'allAssignments': allAssignments,
        'allClasses': allClasses,
        'user': user,
        'authenticated': request.user
        }
        return render(request, 'assignments/assignment.html', context)

class MakeView(View):
    def get(self,request,username):
        user = request.user
        allAssignments = user.assignment_set.all()
        allClasses = user.subject_set.all()
        context = {'allAssignments': allAssignments,
            'allClasses': allClasses,
            'user': user,
            'authenticated': request.user
        }
        return render(request, 'assignments/make.html', context)
    def post(self, request, username):
        user = request.user
        allAssignments = user.assignment_set.all()
        allClasses = user.subject_set.all()
        context = {'allAssignments': allAssignments,
        'allClasses': allClasses,
        'user': user,
        'authenticated': request.user
        }
        return render(request, 'assignments/make.html', context)

class ProfileView(View):
    def get(self,request,username):
        user = User.objects.get(username = username)
        try:
            profile = StudentProfile.objects.get(user=user)
        except StudentProfile.DoesNotExist:
            profile = None
        context = {'profile': profile,
        'user': user,
        'authenticated': request.user
        }
        return render(request, 'assignments/profile.html', context)
    def post(self,request,username):
        user = User.objects.get(username = username)
        try:
            profile = StudentProfile.objects.get(user=user)
        except StudentProfile.DoesNotExist:
            profile = None
        name = request.POST['profileName']
        bio = request.POST['profileBio']
        school = request.POST['profileSchool']
        grade = request.POST['profileGrade']
        print(grade)
        profile= StudentProfile(user=user,name=name,bio=bio, school=school,year_in_school=grade)
        profile.save()
        context = {'profile': profile,
        'user': user,
        'authenticated': request.user
        }
        return render(request, 'assignments/profile.html', context)

class EditView(View):
    def get(self, request, username):
        user = request.user
        profile= user.studentprofile
        context={'profile': profile,
        'user': user,
        'authenticated': request.user
        }
        return render(request, 'assignments/editprofile.html', context)
    def post(self, request, username):
        user = request.user
        profile = user.studentprofile
        context={'profile': profile,
        'user': user,
        'authenticated':request.user
        }
        return render(request, 'assignments/editprofile.html', context)

class CreateView(View):
    def get(self,request,username):
        user = User.objects.get(username = username)
        context={
        'user': user,
        'authenticated':request.user
        }
        return render(request, 'assignments/create.html',context)
    def post(self,request,username):
        user = User.objects.get(username = username)
        context={
        'user': user,
        'authenticated':request.user
        }
        return render(request, 'assignments/create.html', context)

class EditAssignView(View):
    def get(self,request,username):
        user = request.user
        allAssignments = user.assignment_set.all()
        allClasses = user.subject_set.all()
        context = {'allAssignments': allAssignments,
        'allClasses': allClasses,
        'user': user,
        'authenticated': request.user
        }
        return render(request,'assignments/editassignment.html', context)
    def post(self,request,username):
        user = request.user
        allAssignments = user.assignment_set.all()
        allClasses = user.subject_set.all()
        assignment_id = request.POST['assignment_id']
        assignment=Assignment.objects.get(id=assignment_id)
        dueDate = assignment.dueDate.strftime('%FT%T')
        print(assignment)
        assignmentName = assignment.assignmentClass.name
        context = {'allAssignments': allAssignments,
        'allClasses':allClasses,
        'user': user,
        'authenticated': request.user,
        'assignment': assignment,
        'dueDate': dueDate,
        'assignmentName': assignmentName,
        }
        return render(request,'assignments/editassignment.html',context)

class SaveEditView(View):
    def get(self,request,username):
        user = request.user
        allAssignments = user.assignment_set.all()
        allClasses = user.subject_set.all()
        context = {'allAssignments': allAssignments,
        'allClasses':allClasses,
        'user': user,
        'authenticated': request.user
        }
        return render(request, 'assignments/assignment.html', context)
    def post(self,request,username):
        user = request.user
        allAssignments = user.assignment_set.all()
        allClasses = user.subject_set.all()
        name = request.POST['assignmentName']
        description = request.POST['assignmentDescription']
        dueDate = request.POST['assignmentDue']
        complete = request.POST.get('assignmentComplete') == 'on'
        assignmentClass = request.POST['subject']
        # complete = request.POST['assignmentComplete']
        assignment_id = request.POST['assignment_id']
        assignment=Assignment.objects.get(id=assignment_id)
        assignment.name = name
        assignment.description = description
        assignment.dueDate = dueDate
        assignment.complete = complete
        subject = Subject.objects.get(id=assignmentClass)
        assignment.assignmentClass = subject
        assignment.save()

        context = {'allAssignments': allAssignments,
        'allClasses':allClasses,
        'user': user,
        'authenticated': request.user
        }
        return redirect('/assignments/'+ username)

class DeleteView(View):
    def get(self,request,username):
        return redirect('/assignments/'+ username)
    def post(self,request,username):
        assignment_id = request.POST['assignment_id']
        assignment=Assignment.objects.get(id=assignment_id)
        assignment.delete()
        return redirect('/assignments/'+ username)

class ClassesView(View):
    def get(self, request, username):
        user = request.user
        allClasses = user.subject_set.all()
        context = {'allClasses': allClasses,
        'user': user,
        'authenticated': request.user
        }
        return render(request, 'assignments/classes.html', context)
    def post(self, request, username):
        user = request.user
        allClasses = user.subject_set.all()
        name = request.POST['className']
        teacher = request.POST['classTeacher']
        description = request.POST['classDescription']
        subject=Subject(userClasses=user,name=name,teacher=teacher, description=description)
        subject.save()
        context = {'allClasses': allClasses,
        'user': user,
        'authenticated': request.user
        }
        return render(request, 'assignments/classes.html', context)
class MakeClassesView(View):
    def get(self,request,username):
        user = request.user
        allClasses = user.subject_set.all()
        context = {'allClasses': allClasses,
            'user': user,
            'authenticated': request.user
            }
        return render(request, 'assignments/newclass.html',context)
    def post(self, request, username):
        user = request.user
        allClasses = user.subject_set.all()
        context = {'allClasses': allClasses,
        'user': user,
        'authenticated': request.user
        }
        return render(request, 'assignments/newclass.html',context)

class EditClassesView(View):
    def get(self,request,username):
        user = request.user
        allClasses = user.subject_set.all()
        context = {'allClasses': allClasses,
        'user': user,
        'authenticated': request.user
        }
        return render(request,'assignments/editclass.html', context)
    def post(self,request,username):
        user = request.user
        allClasses = user.subject_set.all()
        subject_id = request.POST['class_id']
        Classes =Subject.objects.get(id=subject_id)
        context = {'allClasses': allClasses,
        'user': user,
        'authenticated': request.user,
        'class': Classes,
        }
        return render(request,'assignments/editclass.html',context)

class SaveClassView(View):
    def get(self,request,username):
        user = request.user
        allClasses = user.subject_set.all()
        context = {'allClasses': allClasses,
        'user': user,
        'authenticated': request.user
        }
        return render(request, 'assignments/classes.html', context)
    def post(self,request,username):
        user = request.user
        allClasses = user.subject_set.all()
        name = request.POST['className']
        teacher = request.POST['classTeacher']
        description = request.POST['classDescription']
        subject_id = request.POST['class_id']
        editclass = Subject.objects.get(id=subject_id)
        editclass.name = name
        editclass.teacher = teacher
        editclass.description = description
        editclass.save()
        context = {'allClasses': allClasses,
        'user': user,
        'authenticated': request.user
        }
        return redirect('/classes/'+ username)

class DeleteClassView(View):
    def get(self,request,username):
        return redirect('/classes/'+ username)

    def post(self,request,username):
        subject_id = request.POST['class_id']
        subject=Subject.objects.get(id=subject_id)
        subject.delete()
        return redirect('/classes/'+ username)
