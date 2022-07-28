from rest_framework import authentication, generics, permissions
from rest_framework.response import Response

from department.models import Department
from department.serializers import DepartmentSerializer
from membership.permissions import (
    IsBringUpAdminPermission,
    IsBringUpMemberPermission
)

from department.permissions import IsHODPermission
from membership.models import Members


class DepartmentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [
        permissions.IsAdminUser,
        IsBringUpAdminPermission,
        IsBringUpMemberPermission,
        IsHODPermission
        ]

    def perform_create(self, serializer):
        if serializer.is_valid():
            member = serializer.validated_data['member']
            department_name = serializer.validated_data['name']

            if member != '':
                member_exist = Department.objects.filter(
                    member=member, name=department_name)

                if member_exist:
                    return Response(serializer.errors, status=500)
        return super().perform_create(serializer)


class DepartmentUpdateAPIView(generics.UpdateAPIView):
    queryset = Members.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [
        permissions.IsAdminUser,
        IsBringUpAdminPermission,
        IsBringUpMemberPermission,
        IsHODPermission
        ]
    lookup_field = 'pk'

    def perform_update(self, serializer):
        serializer.save()
        # instance = serializer.save()
        # if not instance.first_name:
        #     instance.first_name = ''

        # if not instance.last_name:
        #     instance.last_name = ''     