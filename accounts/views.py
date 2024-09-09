from .forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('scrawl:login')
    template_name = 'registration/signup.html'
