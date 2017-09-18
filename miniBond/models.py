from django.db import models


# Create your models here.
class Platform(models.Model):
	id = models.UUIDField(primary_key=True)
	name = models.CharField(max_length=30)
	website = models.URLField(default='')

	def __str__(self):
		return self.name


class RatingOrganization(models.Model):
	id = models.UUIDField(primary_key=True)
	name = models.CharField(max_length=30)

class LabelText(models.Model):
	id=models.UUIDField(primary_key=True)
	name=models.CharField(max_length=30)

class PlatformLabel(models.Model):
	id = models.UUIDField(primary_key=True)
	platForm = models.OneToOneField(Platform)
	label=models.OneToOneField(LabelText)

class PlatformRating(models.Model):
	id = models.UUIDField(primary_key=True)
	platForm = models.OneToOneField(Platform)
	ratingOrganization = models.OneToOneField(RatingOrganization)
	url = models.URLField(default='')
	ratingValue = models.CharField(max_length=10)


class PromotionAgency(models.Model):
	id = models.UUIDField(primary_key=True)
	name = models.CharField(max_length=30)


class PromotionInfo(models.Model):
	id = models.UUIDField(primary_key=True)
	platForm = models.OneToOneField(Platform)
	promotionAgency = models.OneToOneField(PromotionAgency)
	url = models.URLField(default='')
