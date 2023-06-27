from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', home, name='home'),
    path('lesson/<str:url>/', lesson, name='lesson'),

    # functionally
    path('lesson/<str:url>/solve/problem/<int:pk>/', solve, name='solve'),

    # auth
    path('login/', login_, name='login'),
    path('signup/', signup, name='signup'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
]