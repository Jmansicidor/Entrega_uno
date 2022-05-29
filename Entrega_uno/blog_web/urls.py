from django.urls import path
from blog_web import views


urlpatterns = [

    path("lista", views.Bloglist.as_view(), name="blog_list"),
    path("crear/", views.BlogCreate.as_view(), name="blog_crear"),
    path("detalle/<pk>/", views.BlogDetail.as_view(), name ="blog_detail"),
    path("editar/<pk>/", views.BlogUpdate.as_view(), name ="blog_update"),
    path("borrar/<pk>/", views.BlogDelete.as_view(), name ="blog_delete"),

    path("lista-persona", views.Personalist.as_view(), name="persona_list"),
    path("crear-persona/", views.PersonaCreate.as_view(), name="persona_crear"),
    path("detalle-persona/<pk>/", views.PersonaDetail.as_view(), name ="persona_detail"),
    path("editar-persona/<pk>/", views.PersonaUpdate.as_view(), name ="persona_update"),
    path("borrar-persona/<pk>/", views.PersonaDelete.as_view(), name ="persona_delete"),
    

]
