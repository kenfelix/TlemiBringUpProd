from django.urls import path
from attendance.views import (
    AttendanceListCreateAPIView
)

urlpatterns = [
    path('list/', AttendanceListCreateAPIView.as_view()),
    # path('<int:pk>/edit/', MemberUpdateAPIView.as_view()),
    # path('<int:pk>/delete/', MemberDeleteAPIView.as_view()),
    # path('<int:pk>/', MemberDetailAPIView.as_view(), name='members-detail'),
]