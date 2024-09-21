from django.urls import path
from . import views

urlpatterns = [
     path("", views.index , name="index" ),
     path("calculator/", views.calculator, name = "calculator"),
     path("measurer/" , views.measurer , name = "measurer"),
     path("measurer/<str:name>" , views.test , name = "test")

]
 