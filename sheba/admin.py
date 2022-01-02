from django.contrib import admin
from sheba.models import ComplainBox, Contact, createOTP,post,applyForRelief, donation


admin.site.register(ComplainBox)
admin.site.register(createOTP)
admin.site.register(Contact) 
admin.site.register(post)
admin.site.register(applyForRelief)
admin.site.register(donation)