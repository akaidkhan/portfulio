from django.shortcuts import render
from django.http import HttpResponse
from home import forms
from home.models import Musician, Album


# Create your views here
# def form(request):
#     diction = {}
#     return render(request,'home/form.html', context= diction)
# def form(request):
#     new_form = forms.user_form()
#     diction = {'test_form': new_form, 'heading_1': "This form is created using django library"}
#
#     if request.method == 'POST':
#         new_form = forms.user_form(request.POST)
#
#         if new_form.is_valid():
#             user_name1 = new_form.cleaned_data['user_name1']
#             user_name2 = new_form.cleaned_data['user_name2']
#             user_dob = new_form.cleaned_data['user_dob']
#             user_email = new_form.cleaned_data['user_email']
#
#             diction.update({'user_name1':user_name1})
#             diction.update({'user_name2':user_name2})
#             diction.update({'user_dob':user_dob})
#             diction.update({'user_email':user_email})
#             diction.update({'form_submited':"Yes"})
#
#
#
#
#     return render(request, 'home/form.html', context=diction)
# def form(request):
#     new_form = forms.user_form()
#     diction = {'test_form': new_form, 'heading_1': "This form is created using django library"}
#
#     if request.method == 'POST':
#         new_form = forms.user_form(request.POST)
#
#         if new_form.is_valid():
#             diction.update({'field': new_form.cleaned_data['field']})
#             #diction.update({'boolean_field': new_form.cleaned_data['boolean_field']})
#             diction.update({'form_submited':"Yes"})
#
#
#
#     return render(request, 'home/form.html', context=diction)
# def form(request):
#     new_form = forms.user_form()
#     diction = {'test_form': new_form, 'heading_1': "This form is created using django library"}
#
#     if request.method == 'POST':
#         new_form = forms.user_form(request.POST)
#         diction.update({'test_form':new_form})
#         if new_form.is_valid():
#             diction.update({'field': 'Fields Match!!'})
#             diction.update({'form_submited':"Yes"})
#
#     return render(request, 'home/form.html', context=diction)
# def form(request):
#     new_form = forms.MusicianForm()
#     if request.method == 'POST':
#         new_form = forms.MusicianForm(request.POST)
#         if new_form.is_valid():
#             new_form.save(commit=True)
#             return index(request)
#     diction = {'test_form': new_form, 'heading_1':'Add New Musician'}
#     return render(request, 'home/form.html', context = diction)


def index(request):
    musician_list = Musician.objects.order_by('first_name')
    diction = {'text_1':'This a list of Musicians', 'musician':musician_list}
    return render(request, 'home/index.html', context=diction)


def form(request):
    new_form = forms.MusicianForm()
    if request.method == 'POST':
        new_form = forms.MusicianForm(request.POST)
        if new_form.is_valid():
            new_form.save(commit=True)
            return index(request)
    diction = {'test_form': new_form, 'heading_1':'Add New Musician'}
    return render(request, 'home/form.html', context=diction)
