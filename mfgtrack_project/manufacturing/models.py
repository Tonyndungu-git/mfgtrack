from django.db import models
from django.utils import timezone

class Supplier(models.Model):
    name = models.CharField(max_length=100)
    contact_person = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    address = models.TextField()

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.name

class RawMaterial(models.Model):
    name = models.CharField(max_length=100)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity_received = models.DecimalField(max_digits=10, decimal_places=2)
    date_received = models.DateField(default=timezone.now)
    batch_number = models.CharField(max_length=50)
    storage_location = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class ProductionOrder(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity_to_produce = models.IntegerField()
    start_date = models.DateField(default=timezone.now)
    status = models.CharField(max_length=20, default='pending')
    priority = models.IntegerField(default=1)
    completed_quantity = models.IntegerField(default=0)

    def __str__(self):
        return str(self.product)

class ProductionStage(models.Model):
    order = models.ForeignKey(ProductionOrder, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(null=True, blank=True)
    worker = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.order} - {self.name}"

class QualityCheck(models.Model):
    production_stage = models.ForeignKey(ProductionStage, on_delete=models.CASCADE)
    check_type = models.CharField(max_length=100)
    passed = models.BooleanField(default=False)
    remarks = models.TextField()

    def __str__(self):
        return f"{self.production_stage} - {self.check_type}"

class Package(models.Model):
    production_order = models.ForeignKey(ProductionOrder, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    packaging_type = models.CharField(max_length=50)
    packaged_by = models.CharField(max_length=100)
    packaging_date = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.production_order} - {self.packaging_type}"

class Shipment(models.Model):
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    shipping_method = models.CharField(max_length=50)
    destination = models.CharField(max_length=200)
    shipping_date = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.package} - {self.destination}"
