from django.core.mail import send_mail
from twilio.rest import Client

def send_otp_by_email(otp):
    print("sending")
    subject = 'Please Confirm Your Account'
    message = 'Your 6 Digit Verification Pin: {}'.format(otp)
    email_from = 'sandra@techversantinfotech.com'
    recipient_list = ['sandra@techversantinfotech.com', ]
    send_mail(subject, message, email_from, recipient_list)


# def send_otp_by_sms(otp):
# Your new Phone Number is +16072089567
def send_otp_by_sms(otp, phone_number):
    # twilio code
    account_sid = 'AC8e647d76c427382dbef2d4508cdaf233'
    auth_token = 'fb4fa02c9d42687544d71d7b185a1bd0'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=f'Hi, your OTP is {otp}. Great job',
        from_='+16072089567',
        # to='+917293355260',
        to=phone_number,
    )

    print(message.sid)
    # return super().save(otp)
