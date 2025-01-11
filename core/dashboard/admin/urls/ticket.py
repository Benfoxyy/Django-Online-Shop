from django.urls import path
from .. import views

urlpatterns = [
    path(
        "ticket/list/",
        views.AdminTicketListView.as_view(),
        name="ticket-list",
    ),
    path(
        "ticket/<int:pk>/",
        views.AdminTicketDetailView.as_view(),
        name="ticket-detail",
    ),
    path(
        "ticket/<int:pk>/delete/",
        views.AdminTicketDeleteView.as_view(),
        name="ticket-delete",
    ),
]
