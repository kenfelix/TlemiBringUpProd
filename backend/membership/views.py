from rest_framework import authentication, generics, permissions

from membership.models import Members
from membership.serializers import MemberSerializer, MemberDetailedSerializer
from membership.permissions import (
    IsBringUpAdminPermission,
    IsBringUpMemberPermission
)
from department.permissions import IsHODPermission


class MemberListCreateAPIView(generics.ListCreateAPIView):
    queryset = Members.objects.all()
    serializer_class = MemberSerializer
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [
        permissions.IsAdminUser,
        IsBringUpAdminPermission,
        IsBringUpMemberPermission,
        ]


class MemberDetailAPIView(generics.RetrieveAPIView):
    queryset = Members.objects.all()
    serializer_class = MemberDetailedSerializer
    permission_classes = [
        permissions.IsAdminUser,
        IsBringUpAdminPermission,
        IsBringUpMemberPermission,
        ]


class MemberUpdateAPIView(generics.UpdateAPIView):
    queryset = Members.objects.all()
    serializer_class = MemberSerializer
    permission_classes = [
        permissions.IsAdminUser,
        IsBringUpAdminPermission,
        IsBringUpMemberPermission,
        ]
    lookup_field = 'pk'

    def perform_update(self, serializer):
        serializer.save()
        # instance = serializer.save()
        # if not instance.first_name:
        #     instance.first_name = ''

        # if not instance.last_name:
        #     instance.last_name = ''


class MemberDeleteAPIView(generics.DestroyAPIView):
    queryset = Members.objects.all()
    serializer_class = MemberSerializer
    permission_classes = [
        permissions.IsAdminUser,
        IsBringUpAdminPermission,
        ]
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        return super().perform_destroy(instance)