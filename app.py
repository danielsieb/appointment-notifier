import requests
import time
import os
from twilio.rest import Client


headers = {
	'cookie': '_ga=GA1.2.1009536352.1625177308; _gat_gtag_UA_93487216_1=1; _gid=GA1.2.2018426686.1625673971; _ga=GA1.4.1009536352.1625177308; _gat_GSA_ENOR0=1; _gid=GA1.4.2018426686.1625673971; _gat=1; _fbp=fb.1.1625177309031.1212524795; _rdt_uuid=1625780166523.579357f7-fa4f-41fd-b1b8-1d70e8109d59; _ga=GA1.3.1009536352.1625177308; _gid=GA1.3.2018426686.1625673971; _rdt_uuid=1625780166523.579357f7-fa4f-41fd-b1b8-1d70e8109d59; __RequestVerificationToken=NOHmWS_9S68TB-_G19-wJayP_6eDr_xOE6ctxFldLkmlJEoT2POaHXpHLnqzjXkagl2L2TKfVQorYCVKHafZjccLcDU1; ASP.NET_SessionId=011lpkpqbwkddpuyfzwojebu',
	'dnt': '1',
	'x-xsrf-token': '3gDnzs0EKrBUxA2NEBvsPoMZ9GlZDVAnv2wfxM78WMufwjcUP_1PF87b2t5fAjSpTxEl99c2Z5Kpa9S0W_uH_8sLTI41',
	'accept-language': 'en-US',
	'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15',
	'accept': 'application/json, text/javascript, */*; q=0.01',
	'referer': 'https://passportappointment.travel.state.gov/appointment/new/findagency/3AA75EE2C01565855ED429DA07054AA9',
	'authority': 'passportappointment.travel.state.gov',
	'accept-encoding': 'gzip, deflate, br',
}

params = {
	'MIME Type': 'application/x-www-form-urlencoded; charset=UTF-8',
	'latitude': '33.91902821744875',
	'longitude': '-117.87791811882742',
	'dateTravel': '8/1/2021 12:00:00 AM',
	'dateVisaNeeded': '',
	'__RequestVerificationToken': '3gDnzs0EKrBUxA2NEBvsPoMZ9GlZDVAnv2wfxM78WMufwjcUP_1PF87b2t5fAjSpTxEl99c2Z5Kpa9S0W_uH_8sLTI41'
}

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

while 1 == 1:

	try:

		r = requests.post('https://passportappointment.travel.state.gov/appointment/new/findclosestagencies', data= params, headers=headers)

		if r.status_code == 200:
			data = r.json()

			print(time.strftime("%H:%M:%S", time.localtime()))

			sent = False

			for index in data:
				if index is not None and index['IsAvailable'] != False:
					print(time.strftime("%H:%M:%S", time.localtime()))
					print(index['Name'])
					message = client.messages.create(
		                     body="Appointment available for " + index['Name'],
		                     from_='+XXXXXXXXX',
		                     to='+XXXXXXXX'
		                 )
					sent = True
			if sent:
				time.sleep(30)
	except:
		pass

	time.sleep(3)

