from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException

account_side='ACc7c5311e80aa31de5454e4ae064ab5b9'
auth_token='2bbf2d0a5db2e5a6a9a9cc48f3b5e2ae'
client=Client(account_side,auth_token)


def is_valid_number(number):

	try:
		response=client.lookups.phone_numbers(number).fetch(type='carrier')

		return True
	except TwilioRestException as e:
		if e.code==20404:
			return False
		else:
			raise e
print(is_valid_number('+91199999999999'))
print(is_valid_number('+916281000840'))

