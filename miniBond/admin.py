from django.contrib import admin

from miniBond.models import *

admin.site.register(Platform)
admin.site.register(RatingOrganization)
admin.site.register(PlatformRating)
admin.site.register(PromotionAgency)
admin.site.register(PromotionInfo)

# Register your models here.
