from rest_framework.validators import UniqueValidator
from membership.models import Members

unique_fields_validator = UniqueValidator(queryset=Members.objects.all())