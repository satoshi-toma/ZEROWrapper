from django.shortcuts import render #, redirect
from django.views.generic.edit import CreateView, FormView
from django.views.generic.base import TemplateView, View
from .forms import UserRegistForm, UserLoginForm
# from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView


class HomeView(TemplateView):
    template_name = 'home.html'


class UserRegistView(CreateView):
    template_name = 'regist.html'
    form_class = UserRegistForm


# LoginViewで行う
# class UserLoginView(FormView):
#     template_name = 'user_login.html'
#     form_class = UserLoginForm

#     def post(self, request, *args, **kwargs):
#         email = request.POST['email']
#         password = request.POST['password']
#         user = authenticate(email=email, password=password)
#         next_url = request.POST['next']
#         if user is not None and user.is_active:
#             login(request, user)
#         if next_url:
#             return redirect(next_url)
#         return redirect('accounts:home')


class UserLoginView(LoginView):
    template_name = 'user_login.html'
    authentication_form = UserLoginForm

    # ログイン状態保持を選択した場合にセッション時間を伸ばす
    def form_valid(self, form):
        keep_login_session = form.cleaned_data['keep_login_session']
        if keep_login_session:
            self.request.session.set_expiry(604800) #1週間保持(604800秒)
        return super().form_valid(form)


# LogoutViewで行う
# class UserLogoutView(View):
    
#     def get(self, request, *args, **kwargs):
#         logout(request)
#         return redirect('accounts:user_login')


class UserLogoutView(LogoutView):
    pass


class UserView(LoginRequiredMixin, TemplateView):
    template_name = 'user.html'