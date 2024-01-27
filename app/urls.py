from django.urls import path
from app import views
urlpatterns = [
    path('', views.home, name='home'),
    path('AdminRegistration', views.AdminRegistration, name='AdminRegistrationAdminRegistration'),
    path('insertAdminDetails', views.insertAdminDetails, name='insertAdminDetails'),
    path('userLogin', views.userLogin, name='userLogin'),
    path('userSignup', views.userSignup, name='userSignup')
]