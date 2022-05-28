from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from blog_web.models import*
from django.contrib.auth.mixins import LoginRequiredMixin

def detalleposteo(request, id):
    # persona = Persona.objects.get(pk=id)
    posteo = get_object_or_404(detalleposteo(), pk=id)

    return render(request, 'posteo/detalle.html', {'posteo': posteo})


def inicio(request):
    no_blog = Posteo.objects.count()
    blog_web = Posteo.objects.all()
    return render(request, 'inicio.html', {'no_blog': no_blog, 'blog': blog_web})

class Bloglist(ListView):
    model = Posteo
    template_name = "blog_web/blogList.html"


class BlogDetail(DetailView):

    model = Posteo
    template_name = "blog_web/blogDetail.html"

class BlogCreate(LoginRequiredMixin, CreateView):
    model = Posteo
    uccess_url = reverse_lazy("blogList")
    fields = ["autor", "titulo", "categoria", "post"]


class BlogDelete(LoginRequiredMixin, DeleteView):

    model = Posteo
    success_url = reverse_lazy("blogList")

class BlogUpdate(LoginRequiredMixin, UpdateView):

    model = Posteo
    success_url = reverse_lazy("blogList")
    fields = ["autor", "titulo", "categoria", "post"]