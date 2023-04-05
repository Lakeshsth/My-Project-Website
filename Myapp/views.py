from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login , logout
from .models import Signup ,Imageupload,Resume_Uploader
from django.views import View
from .forms import Signup_page,LoginForm,ImageForm, ResumeUploaderForm
class Home(View):
    def get(self,request):
        fm = Signup_page()
        return render(request,'Myapp/home.html',{'form': fm})
    def post(self,request):
        fm = Signup_page(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('Login')
        else:
            return render(request, 'Myapp/Loginpage.html',{'form':fm})
            
        
class LoginView(View):
    def get(self,request):
        fm = LoginForm()
        return render(request,'Myapp/Loginpage.html',{'forms': fm})
    def post(self,request):
        print(request.POST['Username'])
        print(request.POST['Password'])
        user = Signup.objects.all()
        pass1 = request.POST['Password']
        if pass1 in [username.Password for username in user]:
            return render(request,"Myapp/afterlogin.html")
        else:
            return redirect('Login')
def ImageUploader(request):
    if request.method == 'POST':
        print(request.POST)
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    form = ImageForm()
    img =Imageupload.objects.all()
    return render(request, 'Myapp/imageuploader.html', {'img': img, 'form': form})

def delete(request,id):
    photo = Imageupload.objects.get(id=id)
    photo.delete()
    return redirect('imageuploader')


#----------RESUME UPLOADER--------
class RESUME(View):
    def get(self, request):
        form = ResumeUploaderForm()
        candidates = Resume_Uploader.objects.all()
        return render(request,'Myapp/resumeform.html', {'candidates':candidates, 'form':form})
    def post(self,request):
        form = ResumeUploaderForm(request.POST, request.FILES)
        candidates = Resume_Uploader.objects.all()
        print(request.POST, 11111111111111111111111111111)
        if form.is_valid():
            form.save()
        return render(request,'Myapp/resumeform.html', {'candidates':candidates,'form':form})
class CandidateView(View):
    def get(self,request, pk):
        candidate = Resume_Uploader.objects.get(pk=pk)
        return render(request, 'Myapp/candidates.html', {'candidate':candidate})
def deleter(request,id):
    Delete = Resume_Uploader.objects.get(id=id)
    Delete.delete()
    return redirect('Resumeuploader' )

def edit(request,id):
    if request.method == 'POST':
        candidate = Resume_Uploader.objects.get(id=id)
        fm = ResumeUploaderForm(request.POST,instance=candidate)
        if fm.is_valid():
            fm.save()
            return render(request,'Myapp/candidates.html',{'candidate':candidate})
    else:
        candidate = Resume_Uploader.objects.get(id=id)
        fm = ResumeUploaderForm(instance=candidate)
    return render(request,'Myapp/edit.html',{'form':fm})




        
        


        


        
