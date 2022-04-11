from django.db import models
from datetime import datetime, timedelta
from django_filters.rest_framework import DjangoFilterBackend



class Certificados(models.Model):
    # {"username":"test1", "name":"tessst","expiration":10}    
    username = models.CharField(max_length=30, unique=True, null=False)
    name = models.CharField(max_length=255, null=False)
    description = models.TextField(null=True)
    created_at = models.DateTimeField(default=datetime.today())
    updated_at = models.DateTimeField(auto_now=True)
    expiration = models.PositiveIntegerField(null=True, blank=True)
    expiration_at = models.DateTimeField(null=True, blank=True)
    
    groups = models.PositiveSmallIntegerField(blank=True, null=True)
    filter_backends = [DjangoFilterBackend]

    def save(self, *args, **kwargs):
        self.expiration_at = self.created_at + timedelta(days=self.expiration)
        super().save(*args,**kwargs)
    
    class Meta:
        db_table = 'Certificados'
        
    def __str__(self):
        return self.username
    
class Groups(models.Model):
    groups = models.ManyToManyField(Certificados)
    
    class Meta:
        ordering = ['username', 'name']
        
