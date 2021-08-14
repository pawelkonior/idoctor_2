from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView

from newsletter.forms import NewsletterUserForm
from newsletter.models import NewsletterUser


class NewsletterPage(FormView):
    form_class = NewsletterUserForm
    template_name = 'newsletter/newsletter.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
