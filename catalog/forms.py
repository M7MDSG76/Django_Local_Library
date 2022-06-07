from cProfile import label
from dataclasses import fields
from django import forms
import datetime
from django.core.exceptions import ValidationError 
from django.utils.translation import gettext_lazy as _

from .models import BookInstance

from django.contrib.auth.models import User
    
class RenewBookModelForm(forms.ModelForm):
    
    def clean_due_back(self):
       data = self.cleaned_data['due_back']

       # Check if a date is not in the past.
       if data < datetime.date.today():
           raise ValidationError(_('Invalid date - renewal in past'))

       # Check if a date is in the allowed range (+4 weeks from today).
       if data > datetime.date.today() + datetime.timedelta(weeks=4):
           raise ValidationError(_('Invalid date - renewal more than 4 weeks ahead'))

       # Remember to always return the cleaned data.
       return data
    
    class Meta:
         model = BookInstance
         fields = ['due_back']
         labels = {'due_back': _('renewal date')}
         help_texts = {'due_back': _('Enter a date between now and 4 weeks (default 3)')}
    
    
def check_sympols(input):
    """ 
    Some fields cannot contain symplos, This method check if the input contain any sympols.
    """
    
    sympols = ['~','`', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '=', '+', '<',
               '>', ',', '.', '?', '/', '\\', '|', '[', ']', '{', '}', ';', "'", '"', ':', '_']
    sympols_counter = 0
   # Loop within input range
    for char in range(len(input)):   
        # Iterate over sympols   
        for sympol in sympols:
            #Check if char in input equals the iterated sympol rais a VError.
            if input[char] == sympol:
                sympols_counter += 1 
    
    if sympols_counter == 0:
        return False
    elif sympols_counter > 0:
        return True

            
class CreateLibraryMemberForm(forms.Form):
    """
    To create Library Member we need to create a new User first
    therefore we take user cardentials to create a new account as 
    a Library Member.      
    """
    username = forms.CharField(max_length=150,
        help_text=_(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),error_messages={
            "unique": _("A user with that username already exists."),
        })
    
    first_name= forms.CharField(label= _('first name'), max_length=150)
    last_name= forms.CharField(label = _('last name'), max_length=150)
    email= forms.EmailField(label = _('email address'))
    password= forms.CharField(label = _('password'), help_text='Enter a password')
    #confirm_password= forms.CharField(label = _('Confirm password'), help_text= 'Confirm the password')
    
    def clean_username(self):
        data= self.cleaned_data['username']
        if User.objects.all().filter(username= data):
            raise ValidationError(_('Username is already existed, Try another user name'))
        return data
    
    def clean_first_name(self):
        data = self.cleaned_data['first_name']
        return data
        
    def clean_last_name(self):
        data = self.cleaned_data['last_name']
        return data
        
    def clean_email(self):
        data = self.cleaned_data['email']
        return data
    # def clean_confirm_password(self):
    #     data = self.cleaned_data['confirm_password']
    #     return data
    def clean_password(self):
        """
        Password sinitization rules:
        - Passowrd Length bigger than 8 chars.
        - Password should contain sympols.
        - Password should match the 'confirm password'.
        """
        data = self.cleaned_data['password']
        #confirm_password = self.cleaned_data['confirm_password']

        if len(data) < 8:
            raise ValidationError(_('Password should be longer than 8 characters'))

        if check_sympols(data) == False:
            raise ValidationError(self.erorr_messages['password_mismatch'])
        
        # if data != confirm_password:
        #     raise ValidationError(_('Passwords not matching!'))
        
        return data

    
    