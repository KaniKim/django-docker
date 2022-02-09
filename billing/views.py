from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class Index(TemplateView, LoginRequiredMixin):
    template_name = "../vue_spa/public/index.html"
