
""" viewset correspondiente a usuarios del sistema"""

import traceback
from api.models import User
from django.shortcuts import get_object_or_404
from django.contrib.auth.hashers import make_password, check_password
from api.serializers.serializers import UserSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from rest_framework.authentication import  TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    authentication_classes = [ TokenAuthentication ]
    permission_classes = [IsAuthenticated]

    queryset = User.objects.all()       
    serializer_class = UserSerializer

    def get_queryset(self,*args, **kwargs):
        queryset = User.objects.all() 
        pk = kwargs.get('pk') or None

        if (pk):
            queryset = self.queryset.filter(pk=pk)

        return queryset

    def list(self, request):

        # print('request UserViewset ---> ', request)
        filters = request.GET.get('pk')

        queryset = self.get_queryset(filters=filters)
        serializer = self.serializer_class(queryset, many=True)

        # print('esto es lo que retorna el list users ---> ', serializer.data)
        return Response(serializer.data)

    def create(self, request):
        
        # print('Entro al create con la siguiente info', request.data)

        # Request Fields
        username= request.data.get('username')
        first_name= request.data.get('first_name')
        second_name= request.data.get('second_name')
        last_name= request.data.get('last_name')
        second_lastname= request.data.get('second_lastname')
        email= request.data.get('email')
        document= request.data.get('document')
        id_regional= request.data.get('id_regional')
        password= request.data.get('password')
        password_confirm= request.data.get('password_confirm')
        nuxiba_user= request.data.get('nuxiba_user')

        user = self.queryset.filter(email=email)

        # print(' Este es user ---> ',username )

        content = {'message': 'User has been created successfuly'}

        if user:
            content = {'message': 'User is alredy exist'}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)

        if not password or not password_confirm:
            content = {'message': 'Password and password confirm are required'}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)

        if password != password_confirm:
            content = {'message': 'Password and password confirm do not match'}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.create()
            user.username = username
            user.first_name = first_name
            user.second_name = second_name
            user.last_name = last_name
            user.second_lastname = second_lastname
            user.email = email
            user.document = document
            # user.id_regional = id_regional
            user.password = make_password(password_confirm)
            user.nuxiba_user = nuxiba_user
            # user.picture = picture

            if request.FILES:
                picture = request.FILES['picture']
                user.picture = picture
                user.save()

        except Exception as e:
            print(type(e))
            return Response({'message':'Internal server error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        # print('Entro a actualizar dato', request.data)
        user.save()

        serializer = self.serializer_class(self.queryset, many=True)

        return Response(content, status=status.HTTP_200_OK)

    # def retrieve(self, request, pk=None):
    #     pass

    def update(self, request, pk=None):

        users = self.queryset.filter(id=pk)

        # Request Fields
        username= request.data.get('username')
        first_name= request.data.get('first_name')
        second_name= request.data.get('second_name')
        last_name= request.data.get('last_name')
        second_lastname= request.data.get('second_lastname')
        email= request.data.get('email')
        document= request.data.get('document')
        id_regional= request.data.get('id_regional')
        password= request.data.get('password')
        password_confirm= request.data.get('password_confirm')
        nuxiba_user= request.data.get('nuxiba_user')
        picture = None
        # picture= request.FILES['picture']


        # request.FILES ? picture =  picture=request.FILES['picture'] : picture=None
        # picture=request.FILES['picture'] if request.FILES else picture=None

        # print(' Este es request data en user ---> ',request.data )
        # print(' Este es request files en user ---> ',request.FILES )

        content = {'message': 'User information has been update successfuly'}

        if not users:
            content = {'message': 'User not found'}
            return Response(content, status=status.HTTP_404_NOT_FOUND)

        if not password or not password_confirm:
            content = {'message': 'Password and password confirm are required'}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)

        if password != password_confirm:
            content = {'message': 'Password and password confirm do not match'}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)

        try:

            for user in users:
                user.username = username
                user.first_name = first_name
                user.second_name = second_name
                user.last_name = last_name
                user.second_lastname = second_lastname
                user.email = email
                user.document = document
                # user.id_regional = id_regional
                if not check_password(password, user.password):
                    user.password = make_password(password)
                user.nuxiba_user = nuxiba_user
                user.save()

                if request.FILES:
                    picture = request.FILES['picture']
                    user.picture = picture
                    user.save()
                print('usuario modificado')

        except Exception as e:
            print(type(e))
            return Response({'message':'Internal server error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        serializer = self.serializer_class(self.queryset, many=True)

        return Response(content, status=status.HTTP_200_OK)


    # def partial_update(self, request, pk=None):
    #     pass

    # def destroy(self, request, pk=None):
    #     pass