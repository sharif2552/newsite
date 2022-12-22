
from django.urls import path
from products import views

urlpatterns = [
    path('', views.index ,name='home'),
    path('about', views.about, name='about'),
    path("contact/", views.contact, name='contact'),
    path("index/", views.index),
    path('base/',views.base),
    path('new/',views.formtest),
    path('thanks/', views.success),
    path('new2', views.formtest2),

]
