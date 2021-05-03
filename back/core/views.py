from django.contrib.auth import authenticate
from django.contrib.auth.models import AnonymousUser
from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Customer, Owner, Admin, CustomUser
from .serializers import RegisterUserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterUserSerializer

    def retrieve(self, request):
        return Response({})

    def list(self, request):
        return Response({})

    def create(self, request):
        """
        Criação de usuários. Envie um POST para esta rota, e inclua na request:
        - username
        - name
        - password
        - email

        E caso queira criar um Owner, envie o:
        - owner == true

        E caso queira criar Admin:
        - admin == true
        - O usuário logado para criar admin deve ser admin também
        """

        print(request.data)

        if not isinstance(request.user, AnonymousUser) and not isinstance(
            request.user, Admin
        ):
            raise Exception("Cannot create user while logged in")

        if isinstance(request.user, Admin) and "admin" in request.data.keys():
            user = Admin(
                username=request.data["username"],
                email=request.data["email"],
                name=request.data["name"],
            )
            user.set_password(request.data["password"])
        elif "admin" in request.data.keys():
            raise Exception("Only admins can create other admins")

        if "owner" in request.data.keys():
            user = Owner(
                username=request.data["username"],
                email=request.data["email"],
                name=request.data["name"],
            )
            user.set_password(request.data["password"])
        else:
            user = Customer(
                username=request.data["username"],
                email=request.data["email"],
                name=request.data["name"],
            )
            user.set_password(request.data["password"])

        if user is not None:
            return Response(
                data={"message": "User has been successfully created"},
                status=201,
            )

        raise Exception("Unknown error, user was not created.")
