from django.db import models
from datetime import datetime, timedelta



class Certificados(models.Model):
    username = models.CharField(max_length=30, unique=True, null=False)
    name = models.CharField(max_length=255, null=False)
    description = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    expiration = models.IntegerField(null=True)
    expiration_at = models.DateTimeField(null=True)

    def save(self, *args, **kwargs):
        expiration_at = expiration_at
        print(expiration_at)
    
    class Meta:
        db_table = 'Certificados'
        
    def __str__(self):
        return self.username
    

class test(models.Model):
    expiration = models.IntegerField()
    expiration_at = models.DateTimeField()
    
    #expiration = 10
    #expiration_at = 4/4/2022 + 10days
        
