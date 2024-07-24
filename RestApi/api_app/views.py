from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import studentSerilizer
from .models import student
from rest_framework import status

# Create your views here.

@api_view(["GET","POST","PUT","PATCH",'DELETE'])
def studentz(request):
    if request.method == 'GET': 
        obj1 = student.objects.all()
        obj2 = studentSerilizer(obj1, many=True)
        return Response(obj2.data)
    elif request.method == 'POST':
        data = request.data
        serializer = studentSerilizer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    
#     elif request.method == "PUT":
#         data = request.data
#         obj3 = student.objects.get(id=data['id'])
#         serializer = studentSerilizer(obj3,data=data,partial=False)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
        
#     elif request.method == 'PATCH':
#         data = request.data
#         obj5 = student.objects.get(id=data['id'])
#         serializer = studentSerilizer(obj5,data=data,partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
        
#     elif request.method == 'DELETE':
#         data = request.data
#         obj_d= student.objects.get(id=data['id'])
#         obj_d.delete()
#         return Response({'message':'student deleted'}) 

@api_view(["GET","PUT","DELETE","PATCH"])
def studentttt(request,pk):
    try: 
        data1= student.objects.get(pk=pk)
    except student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
      
    if request.method == 'GET':        
        serializer = studentSerilizer(data1)
        return Response(serializer.data)
    
    elif request.method == "PUT":
        serializer = studentSerilizer(data1,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == "PATCH":
        serializer = studentSerilizer(data1,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

        
    elif request.method == 'DELETE':

        data1.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 
