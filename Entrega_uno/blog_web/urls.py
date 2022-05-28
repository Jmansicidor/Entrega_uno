from django.urls import path
from blog_web import views


urlpatterns = [

    path("lista", views.Bloglist.as_view(), name="blog_list"),
    path("crear/", views.BlogCreate.as_view(), name="crear"),
    path("detalle/<pk>/", views.BlogDetail.as_view(), name ="blog_detail"),
    path("editar/<pk>/", views.BlogUpdate.as_view(), name ="blog_update"),
    path("borrar/<pk>/", views.BlogDelete.as_view(), name ="blog_delete"),
    

]
