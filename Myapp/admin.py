from django.contrib import admin
from .models import Signup ,User,Imageupload, Resume_Uploader
# Register your models here.
@admin.register(Signup)
class SignupAdmin(admin.ModelAdmin):
    list_display = ('id', 'First_Name','Last_Name','username','Email','Password')
@admin.register(User)
class SignupAdmin(admin.ModelAdmin):
    list_display = ('id','Username','Password')
@admin.register(Imageupload)
class Image(admin.ModelAdmin):
    list_display = ['id','photo','date']
@admin.register(Resume_Uploader)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ['id','name','dob','gender','locality','city','pin',
                    'state','mobile','email','job_city','profile_image',
                    'my_file']








