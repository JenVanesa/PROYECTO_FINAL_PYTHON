from django.urls import reverse_lazy
from django.views.generic.edit import FormView

from usuarios.forms import RegisterForm

# Create your views here.

class UserRegistration(FormView):
    template_name= 'usuarios/registration.html'
    form_class = RegisterForm
    success_url=reverse_lazy('usuarios:success')

    def form_valid(self, form):
        form.save()
        return super(UserRegistration, self).form_valid(form)
