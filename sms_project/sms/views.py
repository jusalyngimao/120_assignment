from django.shortcuts import render
from django.contrib import messages
from .forms import SmsForm
from .twilio_service import send_sms

# Welcome view for the root page (home)
def welcome_view(request):
    return render(request, "sms/welcome.html")  # Render the welcome page with a link to send SMS

# Send SMS view (handles the SMS form submission)
def send_sms_view(request):
    if request.method == "POST":
        form = SmsForm(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data["phone_number"]
            message = form.cleaned_data["message"]

            sms_sid = send_sms(phone_number, message)

            if sms_sid:
                messages.success(request, f"SMS sent successfully! SID: {sms_sid}")
            else:
                messages.error(request, "Failed to send SMS. Please try again later.")

            return render(request, "sms/send_sms.html", {"form": form, "sms_sid": sms_sid})

        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = SmsForm()

    return render(request, "sms/send_sms.html", {"form": form})
