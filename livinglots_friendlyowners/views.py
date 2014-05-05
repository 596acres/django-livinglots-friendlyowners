from django.views.generic import CreateView, TemplateView

from django_monitor.views import MonitorMixin


class BaseAddFriendlyOwnerView(MonitorMixin, CreateView):

    def get_template_names(self):
        return ['livinglots/friendlyowners/add_friendlyowner.html',]


class BaseAddFriendlyOwnerSuccessView(TemplateView):

    def get_template_names(self):
        return ['livinglots/friendlyowners/add_friendlyowner_success.html',]
