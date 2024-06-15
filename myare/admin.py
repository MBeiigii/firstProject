from django.contrib import admin
from .models import Peik, Location,Safar,Cargo_fare,Transaction,CustomerProfile,Delivery,Destination
# Register your models here.


@admin.register(Peik)
class PelakAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Peik._meta.fields]
    search_fields =  ['user','pelak','code_melli','phone']
    list_filter = ['pelak','code_melli','phone']

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Location._meta.fields]
    search_fields =  ['user','name','operator']
    list_filter = ['name','operator']

@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Destination._meta.fields]

@admin.register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Delivery._meta.fields]


@admin.register(Safar)
class SafarAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Safar._meta.fields]
    # search_fields =  []
    # list_filter = []

@admin.register(Cargo_fare)
class Cargo_fareAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Cargo_fare._meta.fields]

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Transaction._meta.fields]


@admin.register(CustomerProfile)
class CustomerProfileAdmin(admin.ModelAdmin):
    list_display = [field.name for field in CustomerProfile._meta.fields]