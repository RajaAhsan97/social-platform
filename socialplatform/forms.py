from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Group

class logInForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class SignUpform(forms.ModelForm):
    password1 = forms.CharField(label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='confirm password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email']
    
    def clean_password2(self):
        pswd = self.cleaned_data
        if pswd['password1'] != pswd['password2']:
            raise ValidationError('Your password does not match, Re-enter your password again')
        
class GroupForm(forms.Form):
    name = forms.CharField(label="Group Name", initial="Group name...", max_length=100)
    description = forms.CharField(label="Group Description", initial="Description...", widget=forms.Textarea())


# get all groups 
def groupChoices():
   groups = Group.objects.all()
   return {f'{group}' : f'{group}' for group in groups}

class GroupPostForm(forms.Form):
    group = forms.ChoiceField(choices=groupChoices)
    message = forms.CharField(widget=forms.Textarea())
