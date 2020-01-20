from django.db import models


class Category(models.Model):
    categoryid = models.AutoField(db_column='CategoryID', primary_key=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=32)  # Field name made lowercase.
    userid = models.ForeignKey('AuthUser', models.DO_NOTHING, db_column='UserID')  # Field name made lowercase.
    created = models.DateTimeField(db_column='Created')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Category'


class Debit(models.Model):
    debitid = models.BigAutoField(db_column='DebitID', primary_key=True)  # Field name made lowercase.
    warehouseid = models.ForeignKey('Warehouse', models.DO_NOTHING, db_column='WarehouseID')  # Field name made lowercase.
    productid = models.ForeignKey('Product', models.DO_NOTHING, db_column='ProductID')  # Field name made lowercase.
    qty = models.DecimalField(db_column='Qty', max_digits=10, decimal_places=2)  # Field name made lowercase.
    price = models.DecimalField(db_column='Price', max_digits=10, decimal_places=2)  # Field name made lowercase.
    pricetypeid = models.ForeignKey('Pricetype', models.DO_NOTHING, db_column='PriceTypeID')  # Field name made lowercase.
    discountid = models.ForeignKey('Discount', models.DO_NOTHING, db_column='DiscountID')  # Field name made lowercase.
    statusid = models.ForeignKey('Status', models.DO_NOTHING, db_column='StatusID')  # Field name made lowercase.
    notes = models.TextField(db_column='Notes', blank=True, null=True)  # Field name made lowercase.
    userid = models.ForeignKey('AuthUser', models.DO_NOTHING, db_column='UserID')  # Field name made lowercase.
    created = models.DateTimeField(db_column='Created')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Debit'
        ordering = ['-debitid']

class Product(models.Model):
    productid = models.BigAutoField(db_column='ProductID', primary_key=True)  # Field name made lowercase.
    categoryid = models.ForeignKey(Category, models.DO_NOTHING, db_column='CategoryID')  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=48)  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.
    userid = models.ForeignKey('AuthUser', models.DO_NOTHING, db_column='UserID')  # Field name made lowercase.
    created = models.DateTimeField(db_column='Created')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Product'
