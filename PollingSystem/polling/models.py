from django.db import models

# Create your models here.
class SetChoices(models.Model):
	
	place_name=models.CharField(max_length=250,unique=True,primary_key=True,)
	detail=models.CharField(max_length=500)
	approx_cost=models.CharField(max_length=250)


	def __str__(self):
		return self.place_name

class Voter(models.Model):
	choice=models.ForeignKey(SetChoices,on_delete=models.CASCADE)
	roll_num=models.CharField(max_length=50,unique=True,primary_key=True,)
	def __str__(self):
		return self.roll_num

class MyAdmin(models.Model):
	user_name=models.CharField(max_length=500)
	password=models.CharField(max_length=500)

class SetDate(models.Model):
	last_date=models.DateField(max_length=40)

