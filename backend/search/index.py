import imp
from algoliasearch_django import AlgoliaIndex
from algoliasearch_django.decorators import register

from membership.models import Members
from department.models import Department
from attendance.models import Attendance

@register(Members)
class MemberIndex(AlgoliaIndex):

    fields = [
        'first_name',
        'last_name',
        'sex',
        'date_of_birth',
        'state_of_origin',
        'nationality',
        'status',
        'departments',
    ]
    settings = {
        'searchableAttributes': [],
        'attributesForFaceting': ['status']
    }

    tags = 'get_tag'


@register(Department)
class DepartmentIndex(AlgoliaIndex):

    fields = [
        'member',
        'name',
        'status',
    ]
    settings = {
        'searchableAttributes': [],
        'attributesForFaceting': ['status', 'name']
    }

    tags = 'get_tag'


@register(Attendance)
class AttendanceIndex(AlgoliaIndex):

    fields = [
        'title',
        'date',
        'member', 
        'department',
    ]
    settings = {
        'searchableAttributes': [],
        'attributesForFaceting': ['title', 'date', 'member', 'department']
    }