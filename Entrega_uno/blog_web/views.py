from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from blog_web.models import*


def detalleposteo(request, id):
    # persona = Persona.objects.get(pk=id)
    posteo = get_object_or_404(detalleposteo(), pk=id)

    return render(request, 'posteo/detalle.html', {'posteo': posteo})


def inicio(request):
    no_blog = Posteo.objects.count()
    blog_web = Posteo.objects.all()
    return render(request, 'inicio.html', {'no_blog': no_blog, 'blog': blog_web})

class bloglist(ListView):
    model = Posteo
    template_name = "blog_web/blogView.html"

class blogCreate(CreateView):
    model = Posteo

class BlogDetail(DetailView):

    model = Posteo
    template_name = "blog_web/blogDetail.html"

