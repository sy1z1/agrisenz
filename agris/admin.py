from django.contrib import admin
from .models import NPKSensor, AmbientSensor, SoilSensor, Settings, Frequency

@admin.register(NPKSensor)
class NPKSensorDataAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'nitrogen', 'phosphorus', 'potassium')
    list_filter = ('timestamp',)
    ordering = ('-timestamp',)

@admin.register(AmbientSensor)
class AmbientSensorDataAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'A_Temp', 'A_Humid')
    list_filter = ('timestamp',)
    ordering = ('-timestamp',)

@admin.register(SoilSensor)
class SoilSensorDataAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'S_Temp', 'S_Humid')
    list_filter = ('timestamp',)
    ordering = ('-timestamp',)

@admin.register(Settings)
class SettingsDataAdmin(admin.ModelAdmin):
    list_display = ('name', 'value')
    list_filter = ('name',)
    ordering = ('-name',)

@admin.register(Frequency)
class FrequencyAdmin(admin.ModelAdmin):
    list_display = ('value',)  
    search_fields = ('value',)
    ordering = ('value',)
    fields = ('value',) 