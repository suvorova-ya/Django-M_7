from django.contrib.auth.mixins import LoginRequiredMixin
from  django.contrib.auth.models import User
from django.views.generic.edit import CreateView, UpdateView
from .forms import BaseRegisterForm, ProfileForm
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, reverse, redirect



class BaseRegisterView(CreateView):
    model = User
    form_class = BaseRegisterForm
    success_url = '/'

@login_required
def upgrade_me(request):
    user = request.user
    authors_group = Group.objects.get(name='authors')
    if not request.user.groups.filter(name='authors').exists():
        authors_group.user_set.add(user)
    return redirect('/')

# class ProfileUpdateView(LoginRequiredMixin, UpdateView):
#     form_class = ProfileForm
#     model = User
#     template_name = 'protect/index.html'
#     login_url = '/sign/login'
#     success_url = '/news/'
#
#
#     def get_object(self, **kwargs):
#         return self.request.user
#
#
#     def get_context_data(self, **kwargs):
#         user = self.request.user
#         context = super().get_context_data(**kwargs)
#         context['is_not_author'] = not user.groups.filter(name='authors').exists()
#
#         return context

class IndexView(LoginRequiredMixin,UpdateView):
    model = User
    template_name = 'news_portal/index.html'
    form_class = ProfileForm
    login_url = '/sign/login'
    success_url = '/'

    def get_object(self, **kwargs):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_authors'] = not self.request.user.groups.filter(name='authors').exists()
        return context
