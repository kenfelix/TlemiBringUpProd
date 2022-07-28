from django.urls import path
from department.views import (
    DepartmentListCreateAPIView,
    DepartmentUpdateAPIView,
)

urlpatterns = [
    path('list/', DepartmentListCreateAPIView.as_view()),
    path('<int:pk>/edit/', DepartmentUpdateAPIView.as_view(), name='department-detail'),
]