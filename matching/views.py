from django.shortcuts import render
from django.views import generic
from .forms import ContactForm


# Create your views here.
class IndexView(generic.TemplateView):
    template_name = "index.html"    # base.pyのtemplate_nameを定義


class ContactView(generic.TemplateView):
    template_name = "contact.html"
    form_class = ContactForm
