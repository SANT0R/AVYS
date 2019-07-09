from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from bys.models import NewUserModel
from bys.models import yayın
from bys.models import proje
from bys.models import faliyet
from bys.models import etkinlik
from bys.models import atıf
from bys.models import patent
from bys.models import ödül
# Register your models here.

admin.site.register(yayın) 
admin.site.register(proje) 
admin.site.register(faliyet) 
admin.site.register(etkinlik) 
admin.site.register(atıf) 
admin.site.register(patent) 
admin.site.register(ödül) 

class NewUserModel_Inline(admin.StackedInline):
    model = NewUserModel
    can_delete = False
    verbose_name_plural = 'Kişisel Bilgiler'
 
class UserAdmin(BaseUserAdmin):
    inlines = (NewUserModel_Inline, )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)


