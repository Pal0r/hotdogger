from django.views.generic import TemplateView


class LandingTemplateView(TemplateView):
    template_name = 'core/landing.html'
