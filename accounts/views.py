from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, FormView, DetailView, View, UpdateView
from django.views.generic.edit import FormMixin
from django.http import HttpResponse
from django.shortcuts import render,redirect

from django.utils.safestring import mark_safe

from .forms import LoginForm, RegisterForm


# class LoginView(NextUrlMixin, RequestFormAttachMixin, FormView):
#     form_class = LoginForm
#     success_url = '/'
#     template_name = 'accounts/login.html'
#     default_next = '/'
#
#     def form_valid(self, form):
#         next_path = self.get_next_url()
#         return redirect(next_path)




class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = '/login/'

    User = get_user_model()

def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        form.save()
    return render(request, "registration/register.html", context)


# class UserDetailUpdateView(LoginRequiredMixin, UpdateView):
#     form_class = UserDetailChangeForm
#     template_name = 'accounts/detail-update-view.html'
#
#     def get_object(self):
#         return self.request.user
#
#     def get_context_data(self, *args, **kwargs):
#         context = super(UserDetailUpdateView, self).get_context_data(*args, **kwargs)
#         context['title'] = 'Change Your Account Details'
#         return context
#
#     def get_success_url(self):
#         return reverse("account:home")

def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        "form": form
    }
    next_ = request.GET.get('next')
    next_post = request.POST.get('next')
    redirect_path = next_ or next_post or None
    if form.is_valid():
        username  = form.cleaned_data.get("username")
        password  = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            try:
                del request.session['guest_email_id']
            except:
                pass
            if is_safe_url(redirect_path, request.get_host()):
                return redirect(redirect_path)
            else:
                return redirect("/")
        else:
            # Return an 'invalid login' error message.
            print("Error")
    return render(request, "accounts/login.html", context)


