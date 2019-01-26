from twilio.rest import Client
import os
# we assume we already have a list of phone numbers
# need account_sid
# need auth_token
def sendMessage(text):
    account_sid = "ACa713ce4b1075bc4e7aa84f6ed3656303"
    auth_token = "863e8136971af33e2b8a83e96ab103b3"
    twilio_Number = '+13478366081'

    client = Client(account_sid, auth_token)

    #our list of numbers
    numbers = ['+19172080459', '+13477337209', '+13472579022', '+15165068101', '+16315756224', '+13474185648']

    for person_number in list(numbers):
        message = client.messages.create(
            to=person_number,
            from_=twilio_Number,
            body=text)
        print(message.sid)

sendMessage("Yurrrrrrrr Whole lotta gang sh*t goin' on. GET OUT!!!")
