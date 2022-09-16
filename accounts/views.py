from django.views.generic import ListView, DetailView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.mixins import (
    LoginRequiredMixin, 
    UserPassesTestMixin
)

from django.urls import reverse_lazy

from accounts.forms import CustomUserCreationForm

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url= reverse_lazy('login')
    template_name = 'registration/sign_up.html'