from rest_framework import serializers
from .models import Certificados

class CertificadosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificados
        fields = '__all__'