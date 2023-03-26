from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializer import *
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.tokens import RefreshToken
import jwt
from datetime import datetime
import time
from rest_framework_simplejwt.authentication import JWTAuthentication


class userView1(APIView):
    # authentication_classes = [JWTAuthentication,]
    # permission_classes = (IsAuthenticated,)

    def get(self,request,format=None):
        users=User.objects.all()
        serialize=UserSerializer(users,many=True)
        return Response(serialize.data)
    
    def post(self, request, format=None):
        serialize=UserSerializer(data=request.data)
        for var in request.data['role']:
            user.role.add(var)
        if serialize.is_valid():
            serialize.save()
        return Response(serialize.data ,202)
    
class userwith_id(APIView):
    def put(self, request, id, format=None):
        user=User.objects.get(uniqueid=id)
        for var in request.data['role']:
            roles=Roles.objects.get(id=var)
            user.role.add(roles)
        serialize=UserSerializer(user,data=request.data,partial=True) 
        if serialize.is_valid():
            serialize.save()
        return Response("data updated")

    def delete(self, request, id, format=None):
        user=User.objects.get(uniqueid=id)
        user.delete()
        return Response("deleted")




class login(APIView):
    def post(self, request,format=None):
        try:
            data= request.data 
            try:
                user = User.objects.filter(uniqueid=data['username']).first()
                if user.password == data['password']:
                    user1 = User.objects.filter(uniqueid=data['username']).first()
                    refresh =RefreshToken.for_user(user1)
                    return Response({'status': 200,'refresh':str(refresh),'access':str(refresh.access_token)})
                else:
                    return Response('password not matched')
            except User.DoesNotExist:
                return Response('user not found')
        except Exception:
            return Response('wrong attempt')

class login1(APIView):

    def get(self,request,format=None):
        auth=request.headers.get('Authorization')
        print(auth)
        auth=auth.split(" ")[1]
        print(auth)
        token =  jwt.decode(auth,"12345", algorithms=["HS256"])
        print(token['user']['uniqueid'])
        users=User.objects.filter(uniqueid=token['user']['uniqueid'])
        login1.log_out(token['user']['uniqueid'])
        return Response('logout')


    def post(self, request,format=None):
        try:
            user = User.objects.filter(uniqueid=request.data['uniqueid']).first()
            print(request.data['password'])
            if request.data['password'] == user.password:
                userserialized=UserSerializer(user,many=False)
                comment=login1.log_in(user.uniqueid)
                if comment == 400:
                    return Response({'message':'user must logout'},201)
                else:  
                    token=jwt.encode({'user':userserialized.data},"12345" , algorithm="HS256")
                    return Response({'token':token},201)
                return Response('login succesful',200)
            else:
                return Response('invalid credentials',401)
        except User.DoesNotExist:
            return Response('invalid credentilas',402)
        return Response("user registered succesfully",200)
            
    def log_in(user):
        user_login = User.objects.filter(uniqueid=user).first()
        logs=LogsTable.objects.filter(uniqueid=user).last()
        print(LogsTable)
        if logs != None:
            print(logs.uniqueid)
            if str(logs.time_out) == '00:00:00':
                # LogsTable.objects.all().delete()
                return 400
                print('no changes ')
            else:
                print(LogsTable.objects.filter(uniqueid=user).last().time_out)
                log=LogsTable(uniqueid=user,time_in= datetime.now().strftime('%H:%M:%S'),user=user_login) 
                log.save()
        else:
            log=LogsTable(uniqueid=user,time_in= datetime.now().strftime('%H:%M:%S'),user=user_login ) 
            print(log)
            log.save()

    def log_out(user):
        logs=LogsTable.objects.filter(uniqueid=user).last()
        log=logSerializer(logs,data={'time_out':datetime.now().strftime('%H:%M:%S')},partial=True)
        print(logs)
        if log.is_valid():
            log.save()

class logView(APIView):
    def get(self,request,format=None):
        users=LogsTable.objects.all()
        serialize=logSerializer(users,many=True)
        return Response(serialize.data)



class roleView(APIView):
    
    def post(self, request, format=None):
        serialize=RoleSerializer(data=request.data)
        if serialize.is_valid():
            serialize.save()
        print(type(request.data['role']))
        return Response(serialize.data ,202)

    def delete(self, request, format=None):
        Roles.objects.all().delete()
        return Response("deletd",200)

    def get(self, request, format=None):
        roles=Roles.objects.all()
        serialize=RoleSerializer(roles,many=True)
        return Response(serialize.data,200)

        