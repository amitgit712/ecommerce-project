from django.urls import path

from account import views

app_name = 'account'

urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='create_user'),
    path('token/', views.CreateTokenView.as_view(), name='token'),
]
