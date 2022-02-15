from django.urls import path
from . import views
urlpatterns = [
    path("",views.homepage,name="home"),
    path("about/",views.about,name="about"),
    path("contact/",views.contact,name="contact"),
    path("category/<int:id>",views.category,name="category"),
    path("category/<int:id>/<int:filter_id>/",views.category,name="category"),
    path("category/",views.category,name="category"),
    path("view-card/<int:id>",views.viewCard,name="viewCard"),
]