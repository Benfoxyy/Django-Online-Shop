from django.views.generic import TemplateView

class AdminDashboard(TemplateView):
    template_name = 'dashboard/admin.html'