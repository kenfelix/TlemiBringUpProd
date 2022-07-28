from rest_framework import serializers

from department.serializers import DepartmentSerializer
from membership.models import Members


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Members
        url = serializers.HyperlinkedIdentityField(
            view_name= 'members-detail',
            lookup_field='pk',
        )

        fields = [
            'pk',
            'url',
            'first_name',
            'last_name',
            'phone_number',
            'status',
        ]


    def validate_phone_number(self, value):
        qs = Members.objects.filter(phone_number__iexact=value)
        if qs.exists():
            raise serializers.ValidationError(
                f"Member with the Phone number {value} already exists.")
        return value


class MemberDetailedSerializer(serializers.ModelSerializer):

    departments = DepartmentSerializer(many=True)

    class Meta:
        model = Members
        fields = [
            'pk',
            'first_name',
            'last_name',
            'phone_number',
            'sex',
            'email',
            'address',
            'date_of_birth',
            'state_of_origin',
            'nationality',
            'departments',
            'member_choice',
            'status',
        ]
