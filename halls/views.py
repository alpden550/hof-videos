from django.views.generic import TemplateView


class HallMainPage(TemplateView):
    """View to represent main page."""

    template_name = 'halls/index.html'
