from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import User
from .serializers import UserSerializer,RegistrationSerializer
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view,permission_classes
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view
from django.contrib.auth.hashers import check_password
from rest_framework_jwt.settings import api_settings


class UserView(generics.RetrieveUpdateDestroyAPIView):

    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_object(self):
        obj = get_object_or_404(User,id=self.request.user.id)
        return obj

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@swagger_auto_schema(methods=['POST'])
def ChangePassword(request):
    user = request.user
    if request.data.get('password') is None:
        return Response({"message":"Password not sended"})
    user.set_password(request.data.get('password'))
    return Response()


@api_view(['POST'])
def Registration(request):
    serializer = RegistrationSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def Authorization(request):
    qq = {}
    if request.data.get('email'):
        qq['email'] = request.data.get('email')
    if request.data.get('username'):
        qq['username'] = request.data.get('username')
    user = User.objects.filter(**qq)
    if not user.exists():
        return Response({"message":"Cant find with email or username"})
    user = user.first()
    print(user.password)
    if not check_password(request.data.get('password'),user.password):
        return Response({"message":"Password is not correct"})
    payload = api_settings.JWT_PAYLOAD_HANDLER
    token = api_settings.JWT_ENCODE_HANDLER
    user = payload(user)
    data = token(user)
    return Response({'token':data})