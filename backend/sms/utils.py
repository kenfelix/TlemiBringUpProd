from twilio.rest import Client
from django_twilio.utils import discover_twilio_credentials


account_sid, auth_token = discover_twilio_credentials()

# Here we'll build a new Twilio_client with different credentials
twilio_client = Client(account_sid, auth_token)