from django import forms
from django.forms import ModelForm,Textarea
from django.core.exceptions import NON_FIELD_ERRORS
from .models import contact,internship,planguage,project,postgrad,undergrad,srsec,sec,photo,overviewm,jobprofilem,benefitsm,logom,media,headofficem,Workm,Sales_officem,statisticsm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class MyRegistrationForm(UserCreationForm):
    #email=forms.EmailField(required=True)
    #first_name=forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'first name','cols': 0, 'rows': 1}))
    #last_name=forms.CharField(required=True)
    #student_company=forms.CharField(required=True)
    class Meta:
        model=User
        widgets={'user_type':Textarea(attrs={'placeholder':'Student or Company','cols': 80, 'rows': 1}),'email':Textarea(attrs={'placeholder':'Email','cols': 80, 'rows': 1}),'username':Textarea(attrs={'placeholder':'Username','cols': 80, 'rows': 1}),'first_name':Textarea(attrs={'placeholder':'First Name','cols': 80, 'rows': 1}),'last_name':Textarea(attrs={'placeholder':'Last Name','cols': 80, 'rows': 1})}
        fields=['username','first_name','last_name','email','password1','password2','user_type']
        
    def save(self,commit=True):
        user=super(MyRegistrationForm,self).save(commit=False)
        user.email=self.cleaned_data['email']
        #user.student_company=self.cleaned_data['student_or_company']
        if commit:
            user.save()
        return user    
    
    
    

    
    
class contactform(forms.ModelForm):
    upload_cv = forms.FileField(
        label='Select a file',
        help_text='max. 50 Megabytes'
    )
    class Meta:
        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "%(model_name)s's %(field_labels)s are not unique.",
            }
        }
        model=contact
        widgets={'email':Textarea(attrs={'placeholder':'email','cols': 80, 'rows': 1}),'mobile':Textarea(attrs={'placeholder':'mobile','cols': 80, 'rows': 1}),'temporary_address':Textarea(attrs={'placeholder':'temporary_address','cols': 80, 'rows': 3}),'permanent_address':Textarea(attrs={'placeholder':'permanent address','cols': 80, 'rows': 3}),'website':Textarea(attrs={'placeholder':'link','cols': 80, 'rows': 1}),}
        fields=['email','mobile','temporary_address','permanent_address','website','upload_cv']
    
    def clean_email(self):
        email=self.cleaned_data.get('email')
        return email
    

class photoform(forms.ModelForm):
    class Meta:
        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "%(model_name)s's %(field_labels)s are not unique.",
            }
        }
        model=photo
        ###widgets={'email':Textarea(attrs={'placeholder':'email','cols': 80, 'rows': 1}),'mobile':Textarea(attrs={'placeholder':'mobile','cols': 80, 'rows': 1}),'temporary_address':Textarea(attrs={'placeholder':'temporary_address','cols': 80, 'rows': 3}),'permanent_address':Textarea(attrs={'placeholder':'permanent address','cols': 80, 'rows': 3}),'website':Textarea(attrs={'placeholder':'link','cols': 80, 'rows': 1}),}
        fields=['upload']
    


    
class internshipform(forms.ModelForm):
    class Meta:
        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "%(model_name)s's %(field_labels)s are not unique.",
            }
        }
        model=internship
        
        fields=['field1','field2','field3']
        
class postgradform(forms.ModelForm):
    class Meta:
        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "%(model_name)s's %(field_labels)s are not unique.",
            }
        }
        model=postgrad
        
        fields=['year_of_passing','Last_spi','Cpi','Branch_of_study']
        
class undergradform(forms.ModelForm):
    class Meta:
        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "%(model_name)s's %(field_labels)s are not unique.",
            }
        }
        model=undergrad
        
        fields=['year_of_passing','Last_spi','Cpi','Branch_of_study']

class srsecform(forms.ModelForm):
    class Meta:
        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "%(model_name)s's %(field_labels)s are not unique.",
            }
        }
        model=srsec
        
        fields=['year_of_passing','percentage_obtained','school','Board']
        
class secform(forms.ModelForm):
    class Meta:
        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "%(model_name)s's %(field_labels)s are not unique.",
            }
        }
        model=sec
        
        fields=['year_of_passing','percentage_or_cpi','school','Board']
        
class languageform(forms.ModelForm):
    class Meta:
        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "%(model_name)s's %(field_labels)s are not unique.",
            }
        }
        model=planguage
        
        fields=['languages_known']
        
class projectform(forms.ModelForm):
    class Meta:
        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "%(model_name)s's %(field_labels)s are not unique.",
            }
        }
        model=project
        
        fields=['project1','project2','project3']

class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Select a file',
        help_text='max. 42 Megabytes'
    )
    
####################   
###company forms###
##################


class overviewform(forms.ModelForm):
    class Meta:
        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "%(model_name)s's %(field_labels)s are not unique.",
            }
        }
        model=overviewm
        
        fields=['description','url']
        
        
class jobprofileform(forms.ModelForm):
    class Meta:
        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "%(model_name)s's %(field_labels)s are not unique.",
            }
        }
        model=jobprofilem
        
        fields=['position','CPI_cut_off','Branches','description']
        
        
class benefitsform(forms.ModelForm):
    class Meta:
        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "%(model_name)s's %(field_labels)s are not unique.",
            }
        }
        model=benefitsm
        
        fields=['description']
        
class statisticsform(forms.ModelForm):
    class Meta:
        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "%(model_name)s's %(field_labels)s are not unique.",
            }
        }
        model=benefitsm
        
        fields=['description']

class logoform(forms.ModelForm):
    class Meta:
        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "%(model_name)s's %(field_labels)s are not unique.",
            }
        }
        model=logom
        
        fields=['upload']
        
    # def clean_ulpoad(self):
    #     upload=self.cleaned_data.get('upload')
    #     return upload
		
class mediaform(forms.ModelForm):
    class Meta:
        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "%(model_name)s's %(field_labels)s are not unique.",
            }
        }
        model=media
        
        fields=['upload']
		
class headofficeform(forms.ModelForm):
    class Meta:
        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "%(model_name)s's %(field_labels)s are not unique.",
            }
        }
        model=headofficem
        
        fields=['plot_number','Area','City','Pincode','Country','Phone','email']
		
class Workform(forms.ModelForm):
    class Meta:
        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "%(model_name)s's %(field_labels)s are not unique.",
            }
        }
        model=Workm
        
        fields=['plot_number','Area','City','Pincode','Country','Phone','email']

class Sales_officeform(forms.ModelForm):
    class Meta:
        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "%(model_name)s's %(field_labels)s are not unique.",
            }
        }
        model=Sales_officem
        
        fields=['plot_number','Area','City','Pincode','Country','Phone','email']
		