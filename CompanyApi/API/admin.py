from django.contrib import admin
from API.models import Company,Employee,Student,School

# Register your models here.
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'type')
    search_fields = ('name', 'location' , 'type')
    list_filter = ('name','type')

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'company')
    search_fields = ('name', 'email')

class SchoolAdmin(admin.ModelAdmin):
    list_display = ('name','city')
    search_fields = ('name','city')
    
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name','roll', 'school')
    search_fields = ('name','roll')
        

admin.site.register(Company,CompanyAdmin)
admin.site.register(Employee,EmployeeAdmin)
admin.site.register(Student,StudentAdmin)
admin.site.register(School,SchoolAdmin)