from django.contrib import admin
from .models import Supplier, Product, RawMaterial, ProductionOrder, ProductionStage, QualityCheck, Package, Shipment

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ['name', 'contact_person', 'email', 'phone_number', 'address']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'supplier', 'unit_price']

@admin.register(RawMaterial)
class RawMaterialAdmin(admin.ModelAdmin):
    list_display = ['name', 'product', 'quantity_received', 'date_received', 'batch_number', 'storage_location']

@admin.register(ProductionOrder)
class ProductionOrderAdmin(admin.ModelAdmin):
    list_display = ['product', 'quantity_to_produce', 'start_date', 'status', 'priority', 'completed_quantity']

@admin.register(ProductionStage)
class ProductionStageAdmin(admin.ModelAdmin):
    list_display = ['order', 'name', 'start_time', 'end_time', 'worker']

@admin.register(QualityCheck)
class QualityCheckAdmin(admin.ModelAdmin):
    list_display = ['production_stage', 'check_type', 'passed', 'remarks']

@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ['production_order', 'quantity', 'packaging_type', 'packaged_by', 'packaging_date']

@admin.register(Shipment)
class ShipmentAdmin(admin.ModelAdmin):
    list_display = ['package', 'shipping_method', 'destination', 'shipping_date']
