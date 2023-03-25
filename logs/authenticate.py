# import jwt
# from rest_framework.authentication import BaseAuthentication
# from django.middleware.csrf import CsrfViewMiddleware
# from rest_framework import exceptions
# from django.conf import settings
# from django.comtrib.auth import get_user_model

# class SafeAuthentication(BaseAuthentication):


#     def _reject(self, request, reason):
#         try:
#             data= request.data 
#             print('hello')
#             try:
#                 # User.objects.get(uniqueid=request.data['user']).exists():
#                 user = User.objects.filter(uniqueid=data['username']).first()
#                 print(user)
#                 if user.password == data['password']:
#                 # if 1<10:
#                     user1 = User.objects.filter(uniqueid=data['username']).first()
#                     refresh =RefreshToken.for_user(user1)

#                     return Response({'status': 200,'refresh':str(refresh),
#                     'access':str(refresh.access_token)})
#                 else:
#                     return Response('password not matched')
#             except User.DoesNotExist:
#                 return Response('user not found')
            
#         except Exception:
#             return Response('wrong attempt')

        


#     def authenticate(self,request):
#         User = get_user_model()
#         authorization_header=request.header.get('Authorization')

#         if not authorization_header:
#             return None
#         try:
#             access_token=authorization_header.split(' ')[1]
#             payload =jwt.decode(access_token,settings.SECRET_KEY,algorithms=['HS256'])

#         except jwt.ExpiredSignatureError:
#             raise exceptions.AuthenticationFailed('acceess token expired')
#         except IndexError:
#             raise exceptions.AuthenticationFailed('Token prefix missing')
    
#             self.enforce_csrf(request)
#             return (user, None)
            

#     def enforce_csrf(self, request):



import jwt
from django.conf import settings
from django.contrib.auth import get_user_model
from rest_framework import authentication
from rest_framework.exceptions import AuthenticationFailed, ParseError
# from .models import User
User = get_user_model()

class JWTAuthentication(authentication.BaseAuthentication):
    def authenticate(self,request):
        jwt_token=request.META.get('HTTP_AUTHORIZATION')
        if jwt_token is None:
            return None
        jwt_token=JWTAuthentication.get_the_token_from_header(jwt_token)

        try:
            payload=jwt.decode(jwt_token,settings.SECRET_KEY,algorithms=['HS256'])
        except jwt.exceptions.InvalidSignatureError:
            raise AuthenticationFailed('Invalid signature')
        except:
            raise ParseError()
        username=payload.get('user_identifier')
        if username is None:
            raise AuthenticationFailed('user identifer not found')
        user=User.objects.filter(username=username).first()
        if user is None:
            raise AuthenticationFailed('User not found')
        return user,payload

    def authenticate_header(self, request):
        return 'Bearer'

@classmethod
    def create_jwt(cls, user):
        
        payload = {
            'user_identifier': user.username,
            'exp': int((datetime.now() + timedelta(hours=settings.JWT_CONF['TOKEN_LIFETIME_HOURS'])).timestamp()),
            
            'iat': datetime.now().timestamp(),
            'username': user.username,
            'phone_number': user.phone_number
        }

        # Encode the JWT with your secret key
        jwt_token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')

        return jwt_token

    @classmethod
    def get_the_token_from_header(cls, token):
        token = token.replace('Bearer', '').replace(' ', '')  # clean the token
        return token