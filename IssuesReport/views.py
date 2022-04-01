from ast import Delete
from django.shortcuts import render
from .models import Issue 
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from .forms import IssueForm 
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class ListIssue(ListView):
    model = Issue
    template_name = 'listIssue.html'  
    # context_object_name = 'issues'

class AddIssue(LoginRequiredMixin,CreateView):
    model = Issue
    form_class = IssueForm
    template_name = 'issueform.html' 
    success_url = reverse_lazy('listIssue')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # print(dir(self), self.request.user)
        # context['new_data'] = 'asdasd'
        return context


    # def get_success_url(self, **kwargs):
    #     if kwargs != None:
    #         return reverse_lazy('listIssue')
    #     else:
    #         return reverse_lazy('listIssue')

class IssueDetail(DetailView):
    model = Issue 
    template_name = 'issueDetail.html'


class IssueUpdate(LoginRequiredMixin,UpdateView):
    model = Issue
    template_name = 'issueUpdate.html'
    fields = ['issue']




class IssueDelete(LoginRequiredMixin,DeleteView):
    model = Issue 
    template_name = 'issueDelete.html'
    success_url = reverse_lazy('home')
   