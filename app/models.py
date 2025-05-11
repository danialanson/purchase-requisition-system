"""
Definition of models.
"""

from datetime import date
from django.db import models

from django.contrib.auth.models import User

#sharing entity

class PRTable(models.Model):
    pr_id = models.CharField(primary_key=True, max_length=5)
    emp_id = models.CharField(max_length=6, default=None)
    emp_Name = models.CharField(max_length=20, default=None)
    form_Date = models.DateField(default=date.today)
    delv_Date = models.DateField(default=date.today)
    delv_Address = models.CharField(max_length=70)
    class StatusPR(models.TextChoices):
        APPROVED = "Approved"
        REJECTED = "Rejected"
        PENDING = "Pending"

    form_Stats = models.TextField(
        choices = StatusPR.choices,
        default = StatusPR.PENDING
    )
    def str(self):
        return str(self.pr_id)


class PRITable(models.Model):
    item_id = models.CharField(primary_key=True, max_length=6)
    pr_id = models.ForeignKey(PRTable, on_delete=models.CASCADE)
    item_Description = models.TextField(max_length=30)
    item_Quantity = models.IntegerField()
    item_unitPrice = models.DecimalField(max_digits=7, decimal_places=2)
    item_totalPrice = models.DecimalField(max_digits=10, decimal_places=2 )
    def str(self):
        return str(self.item_id)


class QTable(models.Model):
    quotation_ID = models.CharField(primary_key=True, max_length=10)
    purchaser_id = models.CharField(max_length=6, default=None)
    purchaser_Name = models.CharField(max_length=30)
    delv_Address = models.CharField(max_length=70)
    vendor_Name = models.CharField(max_length=50)
    vendor_Address = models.CharField(max_length=70)
    class StatusQuo(models.TextChoices):
        APPROVED = "Approved"
        REJECTED = "Rejected"
        PENDING = "Pending"

    quotation_Stats = models.TextField(
        choices = StatusQuo.choices,
        default = StatusQuo.PENDING
    )
    quotation_Date = models.DateField(default=date.today)
    def str(self):
        return str(self.quotation_ID)


class QITable(models.Model):
    item_id = models.CharField(primary_key=True, max_length=10)
    quotation_ID = models.ForeignKey(QTable, on_delete=models.CASCADE)
    item_Description =  models.TextField(max_length=30)
    item_Quantity = models.IntegerField()
    item_unitPrice = models.DecimalField(max_digits=7, decimal_places=2)
    item_totalPrice = models.DecimalField(max_digits=10, decimal_places=2)
    def str(self):
        return str(self.item_id)

class POTable(models.Model):
    po_id = models.AutoField(primary_key=True, null=False)
    quotation_ID = models.ForeignKey(QTable, on_delete=models.CASCADE)
    fo_id = models.CharField(max_length=6, default=None)    
    fo_Name = models.CharField(max_length=30)
    delv_Address = models.CharField(max_length=70)
    vendor_Name = models.CharField(max_length=50)
    vendor_Address = models.CharField(max_length=70)
    po_Date = models.DateField(default=date.today)
    def str(self):
        return str(self.po_id)

class POITable(models.Model):
    item_id = models.CharField(primary_key=True, max_length=10)
    po_id = models.ForeignKey(POTable, on_delete=models.CASCADE)
    item_Description =  models.TextField(max_length=30)
    item_Quantity = models.IntegerField()
    item_unitPrice = models.DecimalField(max_digits=7, decimal_places=2)
    item_totalPrice = models.DecimalField(max_digits=10, decimal_places=2)
    def str(self):
        return str(self.item_id)