from django.db import models


from membership.models import Members
from department.models import Department


class Attendance(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateField(auto_now=False, auto_now_add=False, auto_created=False, null=True)
    member = models.ForeignKey(Members, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)