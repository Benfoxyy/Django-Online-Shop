from django.urls import path
from .. import views

urlpatterns = [
    path(
        "member/list/",
        views.AdminMemberListView.as_view(),
        name="member-list",
    ),
    path(
        "member/<int:pk>/",
        views.AdminMemberEditView.as_view(),
        name="member-edit",
    ),
]
