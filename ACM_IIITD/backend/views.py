from django.shortcuts import render
from .models import *


def index(request):
    team = TeamMember.objects.filter(designation__icontains='coordinator')
    return render(request, "index.html", context={
        'team': team
    })


def members(request):
    coordinators = TeamMember.objects.filter(designation__exact='Coordinator')
    faculty_coordinator = TeamMember.objects.filter(
        designation__icontains='Faculty Coordinator')
    members = TeamMember.objects.filter(
        designation__icontains='member')
    web_devs = TeamMember.objects.filter(
        designation__icontains='web developer')
    design_head = TeamMember.objects.filter(
        designation__icontains='Design Head')
    sections = [
        {'heading': 'Faculty Coordinator', 'members': faculty_coordinator},
        {'heading':'Coordinators', 'members':coordinators},
        {'heading': 'Web Developers', 'members': web_devs},
        {'heading': 'Design Head', 'members': design_head},
        {'heading': 'Members', 'members': members},
    ]
    return render(request, "members.html", context={
        'sections': sections,
    })

def blog_home(request):
    blogs = Blog.objects.all()
    return render(request, 'blog.html', {
        'blogs':blogs
    })

def blog(request,id):
    blog = Blog.objects.get(id=id)
    return render(request, 'blog_template.html', {
        'blog':blog
    })