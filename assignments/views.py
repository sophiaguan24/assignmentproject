from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import View
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from assignments.models import Assignment

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
        }
        return render(request, 'assignments/assignment.html', context)
    def post(self, request, username):
        user = User.objects.get(username = username)
        allAssignments = Assignment.objects.filter(userAssignments=user)
        name = request.POST['assignmentName']
        description = request.POST['assignmentDescription']
        dueDate = request.POST['assignmentDue']
        # complete = request.POST['assignmentComplete']
        assignment= Assignment(userAssignments=user,name=name,description=description, dueDate=dueDate)
        assignment.save()
        context = {'allAssignments': allAssignments,
        'user': user,
        }
        return render(request, 'assignments/assignment.html', context)

class MakeView(View):
    def post(self, request, username):
        print(request.POST)
        return render(request, 'assignments/make.html')





# Create your views here.
