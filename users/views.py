from django.shortcuts import render
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
# Create your views here.

from users.forms import RegistrationForm
class UserRegistration(FormView):
    template_name = 'users/registration.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('users:success')

    def form_valid(self, form):
        form.save()
        return super(UserRegistration, self).form_valid(form)

