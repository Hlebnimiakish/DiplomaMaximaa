from django.urls import path
from tropic_starter.views import *

urlpatterns = [
    path('', HomepageView.as_view(), name='homepage'),
    path('registration/', RegistrationView.as_view(), name='registrationpage'),
    path('login/', LoginView.as_view(), name='loginpage'),
    path('logout/', LogoutView.as_view(), name='logoutpage'),
    path('addpost/', AddPostView.as_view(), name='addpostpage'),
    path('post/<int:id>', ThePostPage_WithCommView.as_view(), name='thepostpage'),
    path('userpage/<int:id>/', UserPageView.as_view(), name='userpage'),
]