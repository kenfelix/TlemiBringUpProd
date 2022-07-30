from django.urls import path
from sms.views import SMSView


urlpatterns = [
    path('', SMSView.as_view())
]