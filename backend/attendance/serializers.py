from django.db import IntegrityError
from rest_framework import serializers
from attendance.models import Attendance


class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        
        model = Attendance
        # url = serializers.HyperlinkedIdentityField(
        #     view_name= 'members-detail',
        #     lookup_field='pk',
        # )

        fields = [
            # 'url',
            'title',
            'date',
            'member', 
            'department',
        ]

    # def create(self, validated_data):
    #     try:
    #         data = super().create(validated_data)
    #     except IntegrityError:
    #         raise serializers.ValidationError(
    #             "Department with this Member, Name and Status already exists.")
    #     return data