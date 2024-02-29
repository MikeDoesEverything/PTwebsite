from . import views
from django.urls import path


urlpatterns = [
    path("", views.index),
    path("contact-us/", views.contact_us),
    path("design-page/", views.design_page),
    path("about/", views.about),
    path("training-plans/", views.training_plans),
    path("games/", views.games),
    path('contact/', views.contact, name='contact'),
    path('success/', views.success, name='success')
]
