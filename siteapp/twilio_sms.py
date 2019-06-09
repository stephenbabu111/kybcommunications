from twilio.rest import Client
from siteapp.credentials import account_side,auth_token,my_cell,my_twilio


def twilio():
    client = Client(account_side,auth_token)
    my_msg=views.regconf_view(request).msg

    #my_msg= 'your message goes here...'

    message=client.messages.create(from_=my_twilio, to=my_cell, body=my_msg)