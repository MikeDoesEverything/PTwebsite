from . import views
from django.urls import path


urlpatterns = [
    path("", views.homepage),
    path("contact_us/", views.contact_us)
]
