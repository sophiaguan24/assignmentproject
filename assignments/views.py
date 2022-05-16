from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import View
from django.utils import timezone

from django.shortcuts import render
class IndexView(View):
    def get(self,request):
        return render(request, 'assignments/login.html')

# Create your views here.
