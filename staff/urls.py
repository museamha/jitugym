from django.urls import path
from .views import StaffCreateView, StaffDeleteView,StaffListView

urlpatterns = [
    path("create/", StaffCreateView.as_view(), name="staff-create"),
    path("list/", StaffListView.as_view(), name="staff-delete"),
    path("<int:pk>/delete/", StaffDeleteView.as_view(), name="staff-delete"),
]
