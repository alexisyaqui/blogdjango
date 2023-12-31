from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = 'users'


urlpatterns = [
    path('registration/', views.UserRegistration.as_view(), name="registration"),
    path('success/', TemplateView.as_view(template_name='users/success_registration.html'), name="success")

]
