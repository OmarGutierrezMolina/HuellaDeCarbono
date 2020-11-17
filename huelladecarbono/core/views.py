from django.views.generic.base import TemplateView
from django.shortcuts import render


class HomePageView(TemplateView):
    template_name = "core/home.html"



class SamplePageView(TemplateView):
    template_name = "core/sample.html"

