import os
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException
from twilio.http.http_client import TwilioHttpClient

proxy_client = TwilioHttpClient()
#proxy_client.session.proxies = {'https': os.environ['https_proxy']}

account_side='AC05eda611eefcbb94e829d1c64e90b104'
auth_token='72263233d2d7bbcab4b0ff0c46c549fd'
client=Client(account_side,auth_token,http_client=proxy_client)


def is_valid_number(number):

	try:
		response=client.lookups.phone_numbers(number).fetch(type='carrier')

		return True
	except TwilioRestException as e:
		if e.code==20404:
			return False
		else:
			raise e

