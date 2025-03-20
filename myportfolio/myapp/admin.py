from django.contrib import admin
from .models import AboutMe, Project,Certificate

admin.site.register(AboutMe)
admin.site.register(Project)


class CertificateAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_issued','file_url')
    
admin.site.register(Certificate,CertificateAdmin)