
from django.urls import path
from .views import Home, LoginView ,ImageUploader,delete,RESUME,CandidateView, deleter,edit
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',Home.as_view(), name = 'home'),
    path('Loginpage/', LoginView.as_view(), name = 'Login'),
    path ('imageuploader/',ImageUploader, name='imageuploader'),
    path ('delete/<int:id>/',delete, name='delete'),
    path('ResumeUploader/', RESUME.as_view(), name='Resumeuploader'),
    path('<int:pk>', CandidateView.as_view(), name="Candidates"),
    path('deleter/<int:id>/', deleter, name='deleter'),
    path('edit/<int:id>/',edit , name='edit'),


    


] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)