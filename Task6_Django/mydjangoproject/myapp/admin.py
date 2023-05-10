from django.contrib import admin
from myapp.models import Doctor, Room, Patient

# Register your models here.

class PatientAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'age', 'diagnosis')
    list_filter = ('age', 'diagnosis')
    search_fields = ('last_name', 'diagnosis')
    list_editable = ('diagnosis',)

class DoctorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'specialization', 'experience')
    list_filter = ('specialization', )
    search_fields = ('last_name',)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('number', 'department')
    list_filter = ('department',)

admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(Patient, PatientAdmin)
