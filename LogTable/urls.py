from django.contrib import admin
from django.urls import path,include
from LogTable.views import userView1,userwith_id,login,login1,logView,roleView

urlpatterns = [
    path('user/', userView1.as_view()),
    path('user/<id>', userwith_id.as_view()),
    path('login/', login.as_view()),
    path('login1/', login1.as_view()),
    path('logs/', logView.as_view()),
    path('role/', roleView.as_view()),
    # path('auth/', obtain_auth_token),

]