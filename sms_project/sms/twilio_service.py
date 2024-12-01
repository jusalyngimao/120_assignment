import logging
from twilio.rest import Client
from django.conf import settings
from twilio.base.exceptions import TwilioRestException

# Set up logging
logger = logging.getLogger('sms')

def welcome_view(request):
    return render(request, "sms/welcome.html")  # Render the welcome page

def send_sms(to, message):
    try:
        # Initialize the Twilio client with your SID and Auth Token
        client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

        # Send the SMS message to the recipient
        message = client.messages.create(
            body=message,
            from_=settings.TWILIO_PHONE_NUMBER,
            to=to
        )

        logger.info(f"Message sent successfully to {to}. SID: {message.sid}")
        return message.sid
    except TwilioRestException as e:
        logger.error(f"Twilio error: {e}")
        return None  # Returning None to indicate failure
