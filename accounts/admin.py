from django.contrib import admin
from accounts.models import User, DonorProfile, HelplessProfile,User,StaffProfile

admin.site.register(User)
admin.site.register(DonorProfile)
admin.site.register(HelplessProfile)
admin.site.register(StaffProfile)

