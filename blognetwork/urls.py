from django.urls import path
from blognetwork.views import SignUpView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    
]