from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from blog_web.models import *
from django.contrib.auth.mixins import LoginRequiredMixin


def detalleposteo(request, id):
    # persona = Persona.objects.get(pk=id)
    posteo = get_object_or_404(detalleposteo(), pk=id)

    return render(request, 'posteo/detalle.html', {'posteo': posteo})


def inicio(request):
    no_blog = Posteo.objects.count()
    blogweb = Posteo.objects.all()
    return render(request, 'blog_web/inicio.html', {'no_blog': no_blog, 'blogweb': blogweb})


def userunited(request):
    no_persona = Persona.objects.count()
    blogwebuserunited = Persona.objects.all()
    return render(request, 'blog_web/usuarioList.html',
                  {'no_persona': no_persona, 'blogwebuserunited': blogwebuserunited})


class Bloglist(ListView):
    model = Posteo
    template_name = "blog_web/blogList.html"


class BlogDetail(DetailView):
    model = Posteo
    template_name = "blog_web/blogDetail.html"


class BlogCreate(LoginRequiredMixin, CreateView):
    model = Posteo
    success_url = reverse_lazy("blog_list")
    fields = ["autor", "titulo", "categoria", "post"]


class BlogDelete(LoginRequiredMixin, DeleteView):
    model = Posteo
    success_url = reverse_lazy("blog_list")


class BlogUpdate(LoginRequiredMixin, UpdateView):
    model = Posteo
    success_url = reverse_lazy("blog_list")
    fields = ["autor", "titulo", "categoria", "post"]


# agregamos la clase persona


class Personalist(ListView):
    model = Persona
    template_name = "blog_web/personaList.html"


class PersonaDetail(DetailView):
    model = Persona
    template_name = "blog_web/personaDetail.html"


class PersonaCreate(LoginRequiredMixin, CreateView):
    model = Persona
    success_url = reverse_lazy("persona_list")
    fields = ["nombre_completo", "edad", "email", "otros_datos"]


class PersonaDelete(LoginRequiredMixin, DeleteView):
    model = Persona
    success_url = reverse_lazy("persona_list")


class PersonaUpdate(LoginRequiredMixin, UpdateView):
    model = Persona
    success_url = reverse_lazy("persona_list")
    fields = ["nombre_completo", "edad", "email"]
