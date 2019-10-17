import uuid
from sys import version_info
from django.core.management.base import BaseCommand, CommandError
from momorequests.models import MomoRequest

class Command(BaseCommand):
	help = "Create new momo request"


	def handle(self, *args, **options):

		self.stdout.write("You are creating a new momo request ")

		momo_request = MomoRequest()

		momo_request.amount = self.get_input('Enter Amount: ')
		momo_request.party_id = self.get_input('Enter Phone: ')
		momo_request.payer_message = self.get_input('Enter Payer Message: ')
		momo_request.payee_note = self.get_input('Enter Payer Note: ')

		#defaults
		momo_request.reference_id = str(uuid.uuid4())
		momo_request.currency = 'UGX'
		momo_request.payer_id_type = 'MSISDN'
		
		try:
			momo_request.save()
			self.stdout.write("saved successfully")
		except:
			self.stdout.write("Something wrong")

	def get_input(self, text):
		return input(text) if version_info[0] > 2 else raw_input(text)		