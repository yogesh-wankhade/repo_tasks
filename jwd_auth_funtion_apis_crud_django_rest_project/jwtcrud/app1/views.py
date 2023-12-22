from rest_framework.decorators import api_view, authentication_classes,permission_classes
from rest_framework.response import Response
from rest_framework import status
from .serializers import PersonSerializers
from.models import Person
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.
@api_view(http_method_names=['POST',])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def create_person(request):
    try:
        serializer=PersonSerializers(data=request.data)
        serializer.is_valid(rase_exception=True)
        serializer.save()
        return Response(data=serializer.data,status=status.HTTP_200_OK)
    
    except Exception as e:
        return Response(data={'detail':'Error processing request'},status=status.HTTP_400_BAD_REQUEST)
    
@api_view()
def show_persons(request):
    try:
        persons=Person.objects.all()
        serializer=PersonSerializers(persons,many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
    
    except Exception as e:
        return Response(data={'detail':'Error Fetching data'},status=status.HTTP_400_BAD_REQUEST)
    
@api_view()
def retrive_person(request,pk=None):
    try:
        person=get_object_or_404(Person,pk=pk)
        serializer=PersonSerializers(person)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
    
    except Exception as e:
        return Response(data={'detail':'Error Fetching data'},status=status.HTTP_400_BAD_REQUEST)
    
@api_view(http_method_names=['PUT','PATCH'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def update_person(request,pk=None):
    try:
        person=get_object_or_404(Person,pk=pk)
        if request.method=='PUT':
            serializer=PersonSerializers(data=request.data,instance=person)
        if request.method=='PATCH':
            serializer=PersonSerializers(data=request.data, instance=person,partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data,status=status.HTTP_200_OK)

    except Exception as e:
        return Response(data={'detail':'Error updating data'},status=status.HTTP_400_BAD_REQUESTa)

@api_view(http_method_names=['DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def delete_person(request,pk=None):
    try:
        person=get_object_or_404(Person,pk=pk)
        person.delete()
        return Response(data={'detil':'Person deleated successfully'},status=status.HTTP_200_OK) 

    except Exception as e:
        return Response(data={'detail':'error deleating person'},status=status.HTTP_400_BAD_REQUEST)
           









