from . import views
from django.urls import path


urlpatterns = [
    path("hello/", views.hello),
    path("new/", views.new),
    path("<training_plan_id>", views.trainingplan, name="products_training_plan")
]
