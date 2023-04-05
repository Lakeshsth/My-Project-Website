from django import forms
from .models import Signup,  User , Imageupload, Resume_Uploader
class Signup_page(forms.ModelForm):
    class Meta:
        model = Signup
        fields = ('First_Name','Last_Name','username','Email','Password')
        widgets = {
            'First_Name': forms.TextInput(attrs={'class':'form-control'}),
            'Last_Name': forms.TextInput(attrs={'class':'form-control'}),
            'username': forms.TextInput(attrs={'class':'form-control'}),
            'Email': forms.TextInput(attrs={'class':'form-control'}),
            'Password': forms.TextInput(attrs={'class':'form-control'})
        }
class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('Username','Password')
        widgets = {
            'Username': forms.TextInput(attrs={'class':'form-control'}),
            'Password': forms.PasswordInput(attrs={'class':'form-control'}),
        }
class ImageForm(forms.ModelForm):
    class Meta:
        model = Imageupload
        fields = '__all__'
        labels = {'photo':''}
# --------------------Resume Uploader__________-
GENDER_CHOICES =[
    ("Male", 'Male'),
    ('Female', 'Female'),]
JOB_CITY_CHOICE= [
    ('Kathmandu', 'Kathmandu'),
    ('Bhaktapur', 'Bhaktapur'),
    ('Lalitpur', 'Lalitpur'),
    ('Pokhara', 'Pokhara'),
    ('Biratnagar', 'Biratnagar'),
    ('Birgunj', 'Birgunj'),
    ('Chitwan', 'Chitwan'),
    ('Dharan', 'Dharan'),
    ('Butwal', 'Butwal'),
    ('Hetauda', 'Hetauda'),
    ('Nepalgunj', 'Nepalgunj'),
    ('Bharatpur', 'Bharatpur'),
    ('Janakpur', 'Janakpur'),
]
class ResumeUploaderForm(forms.ModelForm):
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect)
    job_city = forms.MultipleChoiceField(label='Preferred JOb Locations', choices=JOB_CITY_CHOICE,widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = Resume_Uploader
        fields = ['id','name','dob','gender','locality','city','pin',
                    'state','mobile','email','job_city','profile_image',
                    'my_file']
        labels = {'name': 'Full Name','dob':'Date of Birth','pin'
                  :'Pin code','mobile':'Mobile No.','email':'Email ID','my_file':'Document'}
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'dob': forms.TextInput(attrs={'class':'form-control','id':'datepicker'}),
            'locality': forms.TextInput(attrs={'class':'form-control'}),
            'city': forms.TextInput(attrs={'class':'form-control'}),
            'pin': forms.TextInput(attrs={'class':'form-control'}),
            'state': forms.Select(attrs={'class':'form-control'}),
            'mobile': forms.NumberInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
        }