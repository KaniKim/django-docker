from django.views.generic import TemplateView

class Index(TemplateView):
    template_name = "../vue_spa/public/index.html"
