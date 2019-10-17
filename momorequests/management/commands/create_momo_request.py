import uuid, requests
from sys import version_info

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

from momorequests.models import MomoRequest

class Command(BaseCommand):
	help = "Create new momo request"


	def handle(self, *args, **options):
		self.stdout.write("You are creating a new momo request")

		momo = MomoRequest()

		momo.amount = self.get_input('Enter Amount: ')
		momo.party_id = self.get_input('Enter Phone: ')
		momo.payer_message = self.get_input('Enter Payer Message: ')
		momo.payee_note = self.get_input('Enter Payer Note: ')

		#defaults
		momo.reference_id = str(uuid.uuid4())
		momo.currency = 'UGX'
		momo.payer_id_type = 'MSISDN'
		
		try:
			momo.save()
			self.stdout.write("saved successfully")

			self.collection_request(momo)
		except:
		 	self.stdout.write("Something wrong")

	def get_input(self, text):
		return input(text) if version_info[0] > 2 else raw_input(text)	

	def collection_request(self, momo):
		api_url = "%srequesttopay" %settings.MOMO_API_URL

		headers = {
			'Content-Type': 'application/json', 
			'Ocp-Apim-Subscription-Key': settings.MOMO_SUBSCRIPTION_KEY,
			'X-Reference-Id': momo.reference_id,
			'X-Target-Environment':settings.MOMO_TARGET_ENVIRONMENT
			}

		body = {
		  "amount": momo.amount,
		  "currency": momo.currency,
		  "externalId": momo.pk,
		  "payer": {
		    "partyIdType": momo.payer_id_type,
		    "partyId": momo.party_id
		  },
		  "payerMessage": momo.payer_message,
		  "payeeNote": momo.payee_note
		}

		res =  requests.post(api_url, headers=headers, data=body)
		msge = "collection request succesful" if res.status_code==200 else "collection request failed: E:%s" %res.status_code
		self.stdout.write(msge) 




