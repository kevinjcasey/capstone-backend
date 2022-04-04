from django.urls import path, include
from . import views

## USER AUTH
from .api import RegisterAPI, LoginAPI, UserAPI
from knox import views as knox_views

urlpatterns = [
  path('api/users', views.UsersList.as_view(), name='users_list'),
  # path('api/users/<int:pk>', views.UsersDetail.as_view(), name='users_detail'),
  path('api/auth/register', RegisterAPI.as_view()),
  path('api/auth/login', LoginAPI.as_view()),
  path('api/auth/user', UserAPI.as_view()),
  path('api/auth', include('knox.urls')),
  path('api/auth/logout', knox_views.LogoutView.as_view(), name = 'knox_logout'), ## This invalidates the token
  path('api/trivia', views.TriviaList.as_view(), name='trivia_list'),
  path('api/trivia/<int:pk>', views.TriviaDetail.as_view(), name='trivia_detail')
]

