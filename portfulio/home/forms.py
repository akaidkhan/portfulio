from django import forms
from django.core import validators
from home import models


class MusicianForm(forms.ModelForm):
    class Meta:
        model = models.Musician
        fields = "__all__"

class AlbumForm(forms.ModelForm):
    class Meta:
        model = models.Album
        fields = "__all__"

# class user_form(forms.Form):
#     # <label for="user_name">Full Name</label>
#     # <input type="text" name="user_name" value="" required>
#     user_name1 = forms.CharField(required = False, label ='First name')
#
#     user_name2 = forms.CharField(required = False, label ='Last name',
#     widget = forms.TextInput( attrs= {'placeholder':'Enter your full name','style':'width:300px'} ) )
#
#     #<label for="user_email">User Email</label>
#     #<input type="email" name="user_email" value="" required>
#     user_email = forms.EmailField()
#
#
#     user_dob = forms.DateField(label="Date of Birth", widget = forms.TextInput( attrs={'type':'date'}))



#class user_form(forms.Form):
    #boolean_field = forms.BooleanField(required=False)
    #field = forms.CharField(max_length=15,min_length=5)
    #choices = (('','--SELECT OPTION--'),('1','First'),('2','Second'),('3','Third'))
    #field = forms.ChoiceField(choices=choices, required=False)
    #choices = (('A','A'),('B','B'),('C','C'))
    #field = forms.ChoiceField(choices=choices, widget=forms.RadioSelect)
    #choices = (('','--SELECT OPTION--'),('1','First'),('2','Second'),('3','Third'))
    #field = forms.MultipleChoiceField(choices=choices, required=False)
     #choices = (('A','A'),('B','B'),('C','C'))
     #field = forms.MultipleChoiceField(choices=choices, widget=forms.CheckboxSelectMultiple)

#
# class user_form(forms.Form):
#     user_email = forms.EmailField()
#     user_vmail = forms.EmailField()
#     name = forms.CharField(validators = [validators.MaxLengthValidator(10)])
#
#     def clean(self):
#         all_cleaned_data = super().clean()
#         user_email = all_cleaned_data['user_email']
#         user_vmail = all_cleaned_data['user_vmail']
#
#         if user_email != user_vmail:
#             raise forms.ValidationError("Fields Don't Match!!!!")
