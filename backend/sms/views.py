from re import T
from rest_framework import generics
from rest_framework.response import Response

from sms.utils import twilio_client


class SMSView(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        body = request.GET.get('body')
        phone_number = request.GET.get('phone')
        if not (body or phone_number):
            return Response('phone number or message must not be null')
        msg = twilio_client.messages.create(
            body= body,
            from_='+19124945284',
            to=phone_number
        )
        return Response(msg.status)
