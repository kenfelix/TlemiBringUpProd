from rest_framework import generics
from rest_framework.response import Response

from search import client


class MemberSearchListView(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        index_name = "tlemi_Members"
        query = request.GET.get('q')
        tag = request.GET.get('tag') or None
        mem_status = request.GET.get('status') or None
        print(f"{query} {tag} {mem_status}")
        if not (query or tag or mem_status):
            return Response('', status=400)
        results = client.perform_search(
            query=query, index_name=index_name, tags=tag, status=mem_status)
        return Response(results)


class DepartmentSearchListView(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        index_name = "tlemi_Department"
        query = request.GET.get('q')
        tags = request.GET.get('tag') or []
        status = request.GET.get('status') or None
        name = request.GET.get('name') or None
        if not (query or tags or status or name):
            return Response('', status=400)
        results = client.perform_search(
            query=query, index_name=index_name, tags=tags, status=status, name=name)
        return Response(results)


class AttendanceSearchListView(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        index_name = "tlemi_Attendance"
        query = request.GET.get('q')
        title = request.GET.get('title') or None
        date = request.GET.get('date') or None
        member = request.GET.get('member') or None
        department = request.GET.get('department') or None
        if not (query or title or date or member or department):
            return Response('', status=400)
        results = client.perform_search(
            query=query, index_name=index_name, title=title, date=date,
            member=member, department=department)
        return Response(results)