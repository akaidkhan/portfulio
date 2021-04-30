from django import forms

class user_form(forms.Form):
    # <label for="user_name">Full Name</label>
    # <input type="text" name="user_name" value="" required>
    user_name1 = forms.CharField(required = False, label ='First name')

    user_name2 = forms.CharField(required = False, label ='Last name')

    #<label for="user_email">User Email</label>
    #<input type="email" name="user_email" value="" required>
    user_email = forms.EmailField()
