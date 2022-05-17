from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import View
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render
from assignments.models import Assignment
# def IndexView(request):
#     if request.POST:
#         if 'inputUsername' in request.POST.keys():
#             user = authenticate(username=request.POST['inputUsername'],
#                 password=request.POST['inputPassword'])
#                 if user is not None:
#                     login(request,user)
#             else:
#                 pass
#         elif 'logout' in request.POST.keys():
#             logout(request)
class assignmentView(View):
    # @login_required
    def get(self, request):
        user = User.objects.get(username = 'sophia')
        allAssignments = Assignment.objects.filter(userAssignments=user)
        context = {'allAssignments': allAssignments}
        return render(request, 'assignments/assignment.html', context)
# class getAssignment(View):



# Create your views here.
