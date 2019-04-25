from django.db import models
from datetime import date

class Sportsmen(models.Model):
	name = models.CharField(max_length = 30)
	surname = models.CharField(max_length = 30)
	patronymic = models.CharField(max_length = 30)
	region = models.CharField(max_length = 30)
	dateofbirth = models.DateField(default = date.today())
	category = models.CharField(max_length = 30)

class Compitition(models.Model):
	date = models.DateField(default = date.today())
	place = models.CharField(max_length = 30)
	status = models.CharField(max_length = 30)

class Judge(models.Model):
	judgename = models.CharField(max_length = 30)
	judgesurname = models.CharField(max_length = 30)
	judgepatronymic = models.CharField(max_length = 30)

class Result(models.Model):
	sportsmenid = models.ForeignKey(Sportsmen, on_delete = models.CASCADE)
	competitionid = models.ForeignKey(Compitition, on_delete = models.CASCADE)
	judgeid = models.ForeignKey(Judge, on_delete = models.CASCADE)
	result = models.IntegerField()
	mastername = models.CharField(max_length = 30)
	mastersurname = models.CharField(max_length = 30)
	masterpatronymic = models.CharField(max_length = 30)
	discipline = models.CharField(max_length = 30)