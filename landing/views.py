from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from .admin import *
from .models import *

def index(request):
    posts_images = PostImage.objects.filter(status=True).order_by('-post__pub_date')[:3]
    return render(request, 'landing/index.html', locals())


def about(request):
    return render(request, 'landing/about.html', locals())


def project(request):
    posts_images = PostImage.objects.filter(status=True)
    return render(request, 'landing/projects.html', locals())


def contacts(request):
    return render(request, 'landing/contacts.html', locals())


def detail(request, slug):
    context = Post.objects.get(slug=slug)
    return render(request, 'landing/detail.html', locals())


def about_energoservice(request):
    return render(request, 'landing/about-energoservice.html', locals())


def start(request):
    return render(request, 'landing/start.html', locals())


def partners(request):
    return render(request, 'landing/partners.html', locals())