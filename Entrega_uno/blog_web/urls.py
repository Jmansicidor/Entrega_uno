from django.urls import path
from blog_web import views


urlpatterns = [
       path("lista", views.bloglist.as_view(), name="blog_list"),
       path("crear/", views.blogCreate.as_view(), name="crear"),
       path("detalles/<pk>/",views.BlogDetail.as_view(), name="detalles")

]
