from twilio.rest import Client
import os
# we assume we already have a list of phone numbers
# need account_sid
# need auth_token
def sendMessage(text):
    account_sid = "ACa713ce4b1075bc4e7aa84f6ed3656303"
    auth_token = "****************************" 
    twilio_Number = '+134783****'

    client = Client(account_sid, auth_token)

    #our list of numbers
    numbers = ['+1917208****', '+1347733****', '+1347257****', '+151650****', '+1631575****', '+1347418****']

    for person_number in list(numbers):
        message = client.messages.create(
            to=person_number,
            from_=twilio_Number,
            body=text)
        print(message.sid)

sendMessage("Yurrrrrrrr Whole lotta gang sh*t goin' on. GET OUT!!!")
