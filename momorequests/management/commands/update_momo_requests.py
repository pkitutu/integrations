import math, requests
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

from momorequests.models import MomoRequest

class Command(BaseCommand):
	help = "Update pending momo requests"


	def handle(self, *args, **options):
		self.stdout.write("Looking for pending momo requests")

		limit = settings.DB_FETCH_LIMIT
		
		momos = MomoRequest.objects.filter(auth_status=0)[:limit]

		for momo in momos:
			auth_status = self.get_momo_status(momo)
			if auth_status==1:
				self.update_momo_status(momo)

	def update_momo_status(self, momo):
		momo.auth_status = 1
		momo.save()
		self.stdout.write("status updated to 1 succesfully") 

	def get_momo_status(self, momo):
		api_url = "%srequesttopay/%s" %(settings.MOMO_API_URL, momo.reference_id)

		headers = {
			'Content-Type': 'application/json', 
			'Ocp-Apim-Subscription-Key': settings.MOMO_SUBSCRIPTION_KEY,
			'X-Target-Environment':settings.MOMO_TARGET_ENVIRONMENT
			}

		res =  requests.get(api_url, headers=headers)
		if res.status_code==200:
			self.stdout.write("connection succesful") 
			status = res.json().get('status')
			return 1 if status=='SUCCESSFUL' else 0
		else:
			self.stdout.write("connection failed E:%s" %res.status_code)
			return 0


