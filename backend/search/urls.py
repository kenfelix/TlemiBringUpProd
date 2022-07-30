from django.urls import path

from search.views import(
    DepartmentSearchListView,
    MemberSearchListView,
    AttendanceSearchListView
)

urlpatterns = [
    path('search/member/', MemberSearchListView.as_view()),
    path('search/department/', DepartmentSearchListView.as_view()),
    path('search/attendance/', AttendanceSearchListView.as_view()),
]