from django.shortcuts import render

from blog_web.models import Persona


def inicio(request):
    no_blog = Persona.objects.count()
    blog_web = Persona.objects.all()
    return render(request, 'inicio.html', {'no_blog': no_blog, 'blog': blog_web})
