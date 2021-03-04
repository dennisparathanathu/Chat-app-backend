from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializer import UserSerializer, RegisterSerializer,CustomUserSerializer,MessageSerializer
from django.contrib.auth import login
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from rest_framework.permissions import IsAuthenticated 
from rest_framework.views import APIView
from .serializer import CreatecontactSerializer
from .models import Contact
from rest_framework.authentication import  TokenAuthentication
from django.http import JsonResponse
from rest_framework.decorators import api_view,permission_classes
from django.contrib.auth.models import User
from rest_framework.parsers import FileUploadParser


# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })

class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)

class Createcontactview(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    serializer_class = CreatecontactSerializer

    queryset = Contact.objects.all()

    def post(self,request,format=None):
        serializer.save(userscontact=self.request.user)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getuserdetails(request):
    if request.method =='GET':
        user = request.user
        user_serializer = UserSerializer(user)
        return JsonResponse(user_serializer.data)

        
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getallUsers(request):
    if request.method =='GET':
        users =User.objects.all()
        print(users)
        users_serializer = UserSerializer(users,many=True)
        return JsonResponse(users_serializer.data,safe=False)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getsingleUsers(request,id):
    if request.method =='GET':
        user =User.objects.get(pk=id)
        print(user)
        users_serializer = UserSerializer(user)
        print(users_serializer.data)
        return JsonResponse(users_serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def message(request):
    if request.method =='POST':
        user_serializer = UserSerializer(user)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse(user_serializer.data)
        else:
            return JsonResponse({"msg":"data is not valid"})

class CustomUserView(APIView):
    parser_class = (FileUploadParser,)
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def post(self, request, *args, **kwargs):

      customuser_serializer = CustomUserSerializer(data=request.data)

      if customuser_serializer.is_valid():
          customuser_serializer.save()
          return Response(file_serializer.data, status=status.HTTP_201_CREATED)
      else:
          return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
