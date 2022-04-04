# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Census(models.Model):
    id = models.AutoField(blank=True, primary_key=True)
    state = models.CharField(max_length=30, blank=True, null=True)
    sex = models.CharField(max_length=1, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    pop2000 = models.IntegerField(blank=True, null=True)
    pop2008 = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.id}, {self.state}, {self.sex}, {self.age}, 2000: {self.pop2000}, 2008: {self.pop2008}"

    class Meta:
        managed = False
        db_table = 'census'


class StateFact(models.Model):
    id = models.CharField(blank=True, primary_key=True, max_length=128)
    name = models.CharField(blank=True, null=True, max_length=128)
    abbreviation = models.CharField(blank=True, null=True, max_length=128)
    country = models.CharField(blank=True, null=True, max_length=128)
    type = models.CharField(blank=True, null=True, max_length=128)
    sort = models.CharField(blank=True, null=True, max_length=128)
    status = models.CharField(blank=True, null=True, max_length=128)
    occupied = models.CharField(blank=True, null=True, max_length=128)
    notes = models.CharField(blank=True, null=True, max_length=128)
    fips_state = models.CharField(blank=True, null=True, max_length=128)
    assoc_press = models.CharField(blank=True, null=True, max_length=128)
    standard_federal_region = models.CharField(blank=True, null=True, max_length=128)
    census_region = models.CharField(blank=True, null=True, max_length=128)
    census_region_name = models.CharField(blank=True, null=True, max_length=128)
    census_division = models.CharField(blank=True, null=True, max_length=128)
    census_division_name = models.CharField(blank=True, null=True, max_length=128)
    circuit_court = models.CharField(blank=True, null=True, max_length=128)

    class Meta:
        managed = False
        db_table = 'state_fact'
