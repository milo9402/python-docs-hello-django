from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.
# from django.contrib.auth.admin import UserAdmin

# importando modelos
from api.models import User

# admin.site.register(User, UserAdmin)

@admin.register(User)
class UserAdmin(UserAdmin):
    # fields = ('first_name' ,'second_name', 'last_name', 'second_lastname', 'email', 'username' ,'document_type', 'document', 'picture', 'password', 'is_admin','is_active')
    
    fieldsets = (
        (None, {
            'fields': ('first_name' ,'second_name', 'last_name', 'second_lastname', 'email', 'username' ,'document_type', 'document', 'picture', 'password', 'is_admin','is_active')
        }),
    )
    
    
    list_display = ('id','first_name' ,'second_name', 'last_name', 'second_lastname', 'email', 'username' ,'document_type', 'document', 'picture', 'password', 'is_admin','is_active',)
