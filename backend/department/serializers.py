from django.db import IntegrityError
from rest_framework import serializers
from department.models import Department


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        
        model = Department
        url = serializers.HyperlinkedIdentityField(
            view_name= 'department-detail',
            lookup_field='pk',
        )

        fields = [
            'url',
            'member',
            'name',
            'status',
        ]

    def create(self, validated_data):
        try:
            data = super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError(
                "Department with this Member, Name and Status already exists.")
        return data