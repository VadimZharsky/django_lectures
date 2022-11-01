import email
from django import forms
from . models import Review
from django.forms import ModelForm

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        # fields = "__all__" #pass all fields from model to form
        fields = ['first_name', 'last_name', 'stars']

        labels = {
            'first_name':'please enter your name',
            'last_name':'Surname',
            'stars':'Rating',
        }

        error_messages = {
            'stars': {
                'min_value':'min stars is 1',
                'max_value':'thank you but max stars is 5'
            }
        }

# class ReviewForm(forms.Form):
#     first_name = forms.CharField(label='First Name', max_length=100)
#     last_name = forms.CharField(label='Last Name', max_length=100)
#     email = forms.EmailField(label='Email')
#     review = forms.CharField(label='Please write your review here', 
#                         widget=forms.Textarea(attrs={'class':'myform', 'rows':'3', 'cols':'100'}))