from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import CertificadosSerializer
from .models import Certificados
from datetime import datetime, timedelta

@api_view(['GET'])
def apiOverview(request):
    routes = {
        'List' : '/list',
        'Detail View' : '/detail/<str:pk>',
        'Create' : '/create/',
        'Update' : '/update/<str:pk>',
        'Delete' : '/delete/<str:pk>',
    }
    return Response(routes)

@api_view(['GET'])
def List(request):
    item = Certificados.objects.all()
    serializer = CertificadosSerializer(item, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def Detail(request, pk):
    item = Certificados.objects.get(id=pk)
    serializer = CertificadosSerializer(item, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def Create(request):
    serializer = CertificadosSerializer(data=request.data)
    
    print('Aqui')
    print(serializer)
    if serializer.is_valid():
        serializer.save()
        print('salvo')
    return Response(serializer.data)

@api_view(['POST'])
def Update(request, pk):
    item = Certificados.objects.get(id=pk)
    serializer = CertificadosSerializer(instance = item, data=request.data)
    if serializer.is_valid():
        serializer.save()
        print('Salvou')
    return Response(serializer.data)

@api_view(['DELETE'])
def Delete(request, pk):
    item = Certificados.objects.get(id=pk)
    item.delete()
    print('Deleted')
    return Response('Item Sucessfully Delete')

@api_view(['GET'])
def GroupByUsername(request, pk):
    item = Certificados.objects.filter(username=pk)
    serializer = CertificadosSerializer(item, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def GroupByName(request, pk):
    item = Certificados.objects.filter(name=pk)
    serializer = CertificadosSerializer(item, many=True)
    return Response(serializer.data)

