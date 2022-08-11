from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from apps.core.models import User
from apps.users.serializers.serializer import UserSerializer, AuthTokenSerializar


@api_view(['GET','POST'])
def user_api_view(request):

    # List
    if request.method == 'GET':
        # Obtiene todos los usuarios QuerySet
        users = User.objects.all()
        # Serializa los usuarios
        user_serializer = UserSerializer(users, many=True)
        # Retorna los usuarios serializados
        return Response(user_serializer.data, status=status.HTTP_200_OK)
    
    # Create
    elif request.method == 'POST':
        # Serializa los datos enviados del usuario
        user_serializer = UserSerializer(data=request.data)
        
        # Validation
        # Verifica si el serializador es valido
        if user_serializer.is_valid():
            # Guarda el usuario
            user_serializer.save()
            # Retorna el usuario serializado
            return Response(user_serializer.data, status=status.HTTP_201_CREATED)
        # Retorna el error del serializador
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def user_detail_view(request, pk):

    # Obtiene el usuario con el id dado QuerySet
    user = User.objects.filter(id=pk).first()

    # Validacion
    if user:

        # Retrieve
        if request.method == 'GET':
            
            # Serializa el usuario
            user_serializer = UserSerializer(user)
            # Retorna el usuario serializado
            return Response(user_serializer.data, status=status.HTTP_200_OK)
        
        # Update
        elif request.method == 'PUT':
            # Serializa los datos enviados del usuario
            user_serializer = UserSerializer(user, data=request.data)
            if user_serializer.is_valid():
                # Guarda el usuario
                user_serializer.save()
                # Retorna el usuario serializado
                return Response(user_serializer.data, status=status.HTTP_200_OK)
            
            # Retorna el error del serializador
            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

        # Delete
        elif request.method == 'DELETE':
            # Obtiene el usuario con el id dado
            user = User.objects.filter(id=pk).first()
            # Elimina el usuario
            user.delete()
            # Retorna el usuario serializado
            return Response({'message':'User deleted sussccesfull'}, status=status.HTTP_200_OK)

    else:
        return Response({'message':'User is not exits'}, status=status.HTTP_400_BAD_REQUEST)

