from django.shortcuts import render
from django.http import HttpResponse
from home import forms


# Create your views here
# def form(request):
#     diction = {}
#     return render(request,'home/form.html', context= diction)
def form(request):
    new_form = forms.user_form()
    diction = {'test_form': new_form, 'heading_1': "This form is created using django library"}
    return render(request, 'home/form.html', context=diction)
