from django.urls import path
from . import views

urlpatterns = [
  path('api/users', views.UsersList.as_view(), name='users_list'),
  # path('api/users/<int:pk>', views.UsersDetail.as_view(), name='users_detail'),
]

