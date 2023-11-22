from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse


def Index(request):
    return HttpResponseRedirect(reverse('blog_list'))