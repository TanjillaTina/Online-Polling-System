from django.contrib import admin
from polling.models import SetChoices,Voter,MyAdmin,SetDate

# Register your models here.
admin.site.register(SetChoices)
admin.site.register(Voter)
admin.site.register(MyAdmin)
admin.site.register(SetDate)
