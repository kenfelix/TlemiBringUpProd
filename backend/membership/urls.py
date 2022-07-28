from django.urls import path
from membership.views import (
    MemberDetailAPIView,
    MemberListCreateAPIView,
    MemberUpdateAPIView,
    MemberDeleteAPIView,
)

urlpatterns = [
    path('list/', MemberListCreateAPIView.as_view()),
    path('<int:pk>/edit/', MemberUpdateAPIView.as_view()),
    path('<int:pk>/delete/', MemberDeleteAPIView.as_view()),
    path('<int:pk>/', MemberDetailAPIView.as_view(), name='members-detail'),
]