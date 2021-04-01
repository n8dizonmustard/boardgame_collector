from django.contrib import admin
# import your models here
from .models import Boardgame, Review, Store

# Register your models here.
admin.site.register(Boardgame)
admin.site.register(Review)
admin.site.register(Store)