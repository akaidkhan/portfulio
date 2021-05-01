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

    if request.method == 'POST':
        new_form = forms.user_form(request.POST)

        if new_form.is_valid():
            user_name1 = new_form.cleaned_data['user_name1']
            user_name2 = new_form.cleaned_data['user_name2']
            user_dob = new_form.cleaned_data['user_dob']
            user_email = new_form.cleaned_data['user_email']

            diction.update({'user_name1':user_name1})
            diction.update({'user_name2':user_name2})
            diction.update({'user_dob':user_dob})
            diction.update({'user_email':user_email})
            diction.update({'form_submited':"Yes"})




    return render(request, 'home/form.html', context=diction)
