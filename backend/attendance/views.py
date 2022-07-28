from rest_framework import authentication, generics, permissions

from rest_framework import serializers

from attendance.models import Attendance
from attendance.serializers import AttendanceSerializer
from membership.permissions import (
    IsBringUpAdminPermission,
    IsBringUpMemberPermission
)

from department.permissions import IsHODPermission
from membership.models import Members


class AttendanceListCreateAPIView(generics.ListCreateAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [
        permissions.IsAdminUser,
        IsBringUpAdminPermission,
        IsBringUpMemberPermission,
        IsHODPermission
        ]