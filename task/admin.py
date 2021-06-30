from django.contrib import admin

# Register your models here.
from task.models import WebsiteName, Menu, Sliders, Images, Footer, ManagerLogin

admin.site.register(WebsiteName)
admin.site.register(Menu)
admin.site.register(Sliders)
admin.site.register(Images)
admin.site.register(Footer)
admin.site.register(ManagerLogin)