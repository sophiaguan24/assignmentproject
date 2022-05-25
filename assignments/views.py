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
from assignments.models import Assignment, StudentProfile

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
        user = User.objects.get(username = username)
        allAssignments = Assignment.objects.filter(userAssignments=user)
        context = {'allAssignments': allAssignments,
        'user': user,
        'authenticated': request.user
        }
        return render(request, 'assignments/assignment.html', context)
    def post(self, request, username):
        user = User.objects.get(username = username)
        allAssignments = Assignment.objects.filter(userAssignments=user)
        name = request.POST['assignmentName']
        description = request.POST['assignmentDescription']
        dueDate = request.POST['assignmentDue']
        complete = request.POST.get('assignmentComplete') == 'on'
        print(complete)
        assignment=Assignment(userAssignments=user,name=name, description=description, dueDate=dueDate)
        assignment.save()
        context = {'allAssignments': allAssignments,
        'user': user,
        'authenticated': request.user
        }
        return render(request, 'assignments/assignment.html', context)

class MakeView(View):
    def post(self, request, username):
        return render(request, 'assignments/make.html')

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
        user = User.objects.get(username = username)
        profile = StudentProfile.objects.get(user=user)
        context={'profile': profile,
        'user': user,
        'authenticated': request.user
        }
        return render(request, 'assignments/editprofile.html', context)
    def post(self, request, username):
        user = User.objects.get(username = username)
        profile = StudentProfile.objects.get(user=user)
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
        return render(request, 'assignments/create.html')
    def post(self,request,username):
        user = User.objects.get(username = username)
        context={
        'user': user,
        'authenticated':request.user
        }
        return render(request, 'assignments/create.html')

class EditAssignView(View):
    def get(self,request,username):
        user = User.objects.get(username = username)
        allAssignments = Assignment.objects.filter(userAssignments=user)
        context = {'allAssignments': allAssignments,
        'user': user,
        'authenticated': request.user
        }
        return render(request,'assignments/editassignment.html', context)
    def post(self,request,username):
        user = User.objects.get(username = username)
        allAssignments = Assignment.objects.filter(userAssignments=user)
        assignment_id = request.POST['assignment_id']
        print(assignment_id)
        assignment=Assignment.objects.get(id=assignment_id)
        dueDate = assignment.dueDate.strftime('%FT%T')
        context = {'allAssignments': allAssignments,
        'user': user,
        'authenticated': request.user,
        'assignment': assignment,
        'dueDate': dueDate
        }
        return render(request,'assignments/editassignment.html',context)
class SaveEditView(View):
    def get(self,request,username):
        user = User.objects.get(username = username)
        allAssignments = Assignment.objects.filter(userAssignments=user)
        context = {'allAssignments': allAssignments,
        'user': user,
        'authenticated': request.user
        }
        return render(request, 'assignments/assignment.html', context)
    def post(self,request,username):
        user = User.objects.get(username = username)
        allAssignments = Assignment.objects.filter(userAssignments=user)
        name = request.POST['assignmentName']
        description = request.POST['assignmentDescription']
        dueDate = request.POST['assignmentDue']
        complete = request.POST.get('assignmentComplete') == 'on'
        # complete = request.POST['assignmentComplete']
        assignment_id = request.POST['assignment_id']
        assignment=Assignment.objects.get(id=assignment_id)
        assignment.name = name
        print(assignment.name)
        assignment.description = description
        print(assignment.description)
        assignment.dueDate = dueDate
        print(assignment.description)
        assignment.complete = complete
        assignment.save()
        context = {'allAssignments': allAssignments,
        'user': user,
        'authenticated': request.user
        }
        return redirect('/assignments/'+ username)
         
class DeleteView(View):
    def get(self,request,username):
        assignment_id = request.POST['assignment_id']
        assignment=Assignment.objects.get(id=assignment_id)
        assignment.delete()
        return redirect('/assignments/'+ username)

    def post(self,request,username):
        assignment_id = request.POST['assignment_id']
        assignment=Assignment.objects.get(id=assignment_id)
        assignment.delete()
        return redirect('/assignments/'+ username)
