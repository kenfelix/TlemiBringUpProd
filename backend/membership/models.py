from django.db import models

from phonenumber_field.modelfields import PhoneNumberField


class Members(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    sex = models.CharField(max_length=10, blank=True)
    phone_number = PhoneNumberField(blank=True)
    email = models.EmailField(unique=True, null=True)
    address = models.CharField(max_length=50, null=True)
    date_of_birth = models.DateField(auto_now=False, auto_now_add=False, auto_created=False, null=True)
    state_of_origin = models.CharField(max_length=50, null=True)
    nationality = models.CharField(max_length=50, null=True)
    member_choice = models.BooleanField(default=False)
    status = models.CharField(max_length=50, default="member")
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_tag(self):
        return [self.status]
    
    @property
    def fullname(self):
        return "%s %s" %(self.first_name, self.last_name)

