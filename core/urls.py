from django.urls import path

from core.views import LandingTemplateView

urlpatterns = [
    path('', LandingTemplateView.as_view(), name='landing-page')
]