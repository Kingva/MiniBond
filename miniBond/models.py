from django.db import models


# Create your models here.
class Platform(models.Model):
	id = models.UUIDField(primary_key=True)
	name = models.CharField(max_length=30)
	website = models.URLField(default='')
	isValid = models.BooleanField(default=False)

	def __str__(self):
		return self.name


class RatingOrganization(models.Model):
	id = models.UUIDField(primary_key=True)
	name = models.CharField(max_length=30)

	def __str__(self):
		return self.name

class LabelText(models.Model):
	id=models.UUIDField(primary_key=True)
	name=models.CharField(max_length=30)

class PlatformLabel(models.Model):
	id = models.UUIDField(primary_key=True)
	platForm = models.OneToOneField(Platform)
	label=models.OneToOneField(LabelText)


class LinkToWx(models.Model):
	id = models.UUIDField(primary_key=True)
	platForm = models.OneToOneField(Platform)
	wxText=models.TextField()
	isValid = models.BooleanField(default=False)

	def __str__(self):
		return self.platForm.name

class PlatformRating(models.Model):
	id = models.UUIDField(primary_key=True)
	platForm = models.ForeignKey(Platform)
	ratingOrganization = models.ForeignKey(RatingOrganization)
	url = models.URLField(default='')
	ratingValue = models.CharField(max_length=10)

	def __str__(self):
		return self.ratingOrganization.name + "-" + self.platForm.name


class PromotionAgency(models.Model):
	id = models.UUIDField(primary_key=True)
	name = models.CharField(max_length=30)
	def __str__(self):
		return self.name


class PromotionInfo(models.Model):
	id = models.UUIDField(primary_key=True)
	platForm = models.ForeignKey(Platform)
	promotionAgency = models.ForeignKey(PromotionAgency)
	url = models.URLField(default='')
	isValid = models.BooleanField(default=False)

	def __str__(self):
		return self.promotionAgency.name + "-" + self.platForm.name
