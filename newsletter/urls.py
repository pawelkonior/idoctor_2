from django.urls import path

from newsletter import views

urlpatterns = [
    path('', views.NewsletterPage.as_view(), name='newsletter')
]
