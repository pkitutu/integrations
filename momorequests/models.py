from django.db import models

# Create your models here.
class MomoRequest(models.Model):
	reference_id = models.CharField(max_length=36)
	amount = models.IntegerField()
	currency = models.CharField(max_length=4)
	payer_id_type = models.CharField(max_length=16)
	party_id = models.CharField(max_length=16)
	payer_message = models.CharField(max_length=32)
	payee_note = models.CharField(max_length=32)
	auth_status = models.PositiveSmallIntegerField(default=0,choices=( (0, 'PENDING'),(1, 'SUCCESSFUL') ))
	financial_transaction_id = models.CharField(max_length=16, null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.auth_status