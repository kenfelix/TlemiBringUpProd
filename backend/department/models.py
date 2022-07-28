from django.db import models
from membership.models import Members

class Department(models.Model):
    member = models.ForeignKey(Members,  related_name='departments', on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=True,)
    status = models.CharField(max_length=50, blank=True)
    class Meta:
        constraints = [
            models.UniqueConstraint(name='unique_member', fields=['name', 'status'])
        ]

    def get_tag(self):
        return [self.status]

    def __str__(self):
        return '%s: %s' % (self.name, self.status)

