from django.urls import path
from.views import CreateNewUser, CreateTokenView

app_name = 'user'

urlpatterns = [
    path('create/', CreateNewUser.as_view(), name='create'),
    path('token/', CreateTokenView.as_view(), name='token')
]
